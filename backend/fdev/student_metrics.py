import os, json
import numpy as np
import pandas as pd

def study_buddy_finder(
	student_id: str,
	top_n: int = 10,
	sort_by: str = "overall",   # "mean" | "max" | "cand_func"
	data_dir: str = "../umbc_data/csv",
):
	def _read_csv(path, **kwargs):
		df = pd.read_csv(path, **kwargs)
		df.columns = [c.strip() for c in df.columns]
		return df

	def _to_numeric_clean(series):
		s = series.astype(str).str.replace(",", "", regex=False).str.strip()
		return pd.to_numeric(s, errors="coerce")

	# ---- Paths
	perf_path   = os.path.join(data_dir, "performance_similarity.csv")
	learn_path  = os.path.join(data_dir, "learning_style_similarity.csv")
	students_p  = os.path.join(data_dir, "students.csv")
	for p in [perf_path, learn_path, students_p]:
		if not os.path.exists(p):
			raise FileNotFoundError(p)

	# ---- Load
	perf  = _read_csv(perf_path, dtype={":START_ID(Student)": "string", ":END_ID(Student)": "string"})
	learn = _read_csv(learn_path, dtype={":START_ID(Student)": "string", ":END_ID(Student)": "string"})
	students = _read_csv(students_p, dtype={"id:ID(Student)": "string"})

	# ---- Students map
	sid_col = "id:ID(Student)"
	name_col = next((c for c in ["name", "Name", "full_name", "Full Name"] if c in students.columns), None)
	if name_col is None:
		raise KeyError("Could not find a name column in students.csv (tried: 'name','Name','full_name','Full Name').")
	id_to_name = dict(zip(students[sid_col], students[name_col]))
	focal_name = id_to_name.get(student_id, student_id)

	# ---- Column handles
	s_col = ":START_ID(Student)"
	e_col = ":END_ID(Student)"
	perf_sim = "similarity:float"
	learn_sim = "similarity:float"

	# ---- PERFORMANCE (START==student → END as collID)
	perf_self = perf.loc[perf[s_col] == student_id, [e_col, perf_sim]].copy()
	perf_self.rename(columns={e_col: "collID", perf_sim: "perf_similarity"}, inplace=True)
	perf_self["perf_similarity"] = _to_numeric_clean(perf_self["perf_similarity"])
	perf_self = perf_self.dropna(subset=["collID", "perf_similarity"])

	# ---- LEARNING (either side matches → take other ID)
	mask = (learn[s_col] == student_id) | (learn[e_col] == student_id)
	learn_self = learn.loc[mask, [s_col, e_col, learn_sim]].copy()
	learn_self["collID"] = np.where(learn_self[s_col] == student_id, learn_self[e_col], learn_self[s_col])
	learn_self = learn_self[["collID", learn_sim]].rename(columns={learn_sim: "learn_similarity"})
	learn_self["learn_similarity"] = _to_numeric_clean(learn_self["learn_similarity"])
	learn_self = learn_self.dropna(subset=["collID", "learn_similarity"])

	# ---- Merge both sources
	combined_wide = pd.merge(perf_self, learn_self, on="collID", how="outer")

	if combined_wide.empty:
		payload = {
			"student_id": student_id,
			"student_name": focal_name,
			"sort_by": sort_by,
			"top_n": 0,
			"results": [],
		}
		return json.dumps(payload, ensure_ascii=False, indent=2)

	# ---- Collapse duplicates per collID
	agg_func = {"mean": "mean", "max": "max"}.get(sort_by, "mean")
	keep_cols = [c for c in ["perf_similarity","learn_similarity"] if c in combined_wide.columns]
	combined_wide = (
		combined_wide.groupby("collID", as_index=False)
		.agg({k: agg_func for k in keep_cols})
	)

	# ---- STRICT requirement: both perf & learn must exist
	combined_wide = combined_wide.dropna(subset=["perf_similarity", "learn_similarity"], how="any")
	if combined_wide.empty:
		payload = {
			"student_id": student_id,
			"student_name": focal_name,
			"sort_by": sort_by,
			"top_n": 0,
			"results": [],
		}
		return json.dumps(payload, ensure_ascii=False, indent=2)

	# ---- Add names + display label
	combined_wide["collName"] = combined_wide["collID"].map(id_to_name)
	combined_wide["display"] = combined_wide.apply(
		lambda r: (r["collName"] if pd.notna(r["collName"]) else r["collID"]),
		axis=1
	)

	# ---- Combined score (now safe: both values exist)
	if sort_by == "mean":
		combined_wide["combined"] = combined_wide[["perf_similarity","learn_similarity"]].mean(axis=1)
	elif sort_by == "max":
		combined_wide["combined"] = combined_wide[["perf_similarity","learn_similarity"]].max(axis=1)
	elif sort_by == "cand_func":
		p = combined_wide["perf_similarity"]
		l = combined_wide["learn_similarity"]
		combined_wide["combined"] = ((p**0.5) * l)**0.5
	else:  # mean
		combined_wide["combined"] = combined_wide[["perf_similarity","learn_similarity"]].mean(axis=1)

	combined_wide["combined"] = pd.to_numeric(combined_wide["combined"], errors="coerce")
	combined_wide = combined_wide[np.isfinite(combined_wide["combined"])]

	# ---- Sort & top N
	combined_wide = combined_wide.sort_values("combined", ascending=False).head(top_n)

	# ---- Build JSON payload
	results = []
	for _, r in combined_wide.iterrows():
		results.append({
			"coll_id": r["collID"],
			"coll_name": r["collName"] if pd.notna(r["collName"]) else None,
			"perf_similarity": float(r["perf_similarity"]),
			"learn_similarity": float(r["learn_similarity"]),
			"overall": float(r["combined"]),
		})

	payload = {
		"student_id": student_id,
		"student_name": focal_name,
		"sort_by": sort_by,
		"top_n": len(results),
		"results": results,
	}

	return json.dumps(payload, ensure_ascii=False, indent=2)