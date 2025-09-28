import os, json
import numpy as np
import pandas as pd
import warnings


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



def suggest_next_semester_classes(
    student_id: str,
    top_k: int = 20,
    data_dir: str = "../umbc_data/csv",
):
    
    warnings.filterwarnings("ignore")
    # ---------- helpers ----------
    def _read_csv(name, dtypes=None):
        path = os.path.join(data_dir, name)
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        df = pd.read_csv(path, dtype=dtypes or {})
        df.columns = [c.strip() for c in df.columns]
        return df

    grade_rank = {"A+":12,"A":11,"A-":10,"B+":9,"B":8,"B-":7,"C+":6,"C":5,"C-":4,"D+":3,"D":2,"D-":1,"F":0,"E":0}
    def grade_meets(actual, minimum):
        a = grade_rank.get(str(actual).strip(), -1)
        m = grade_rank.get(str(minimum).strip(), 999)
        return a >= m

    def norm_range(x, lo, hi):
        try: x = float(x)
        except Exception: return np.nan
        if hi == lo: return 0.0
        return (x - lo) / (hi - lo)

    pace_map = {"Accelerated": 1.0, "Standard": 0.75, "Part-time": 0.5}
    mode_map = {"In-person": 0.25, "Hybrid": 0.50, "Online": 0.75}

    # ---------- load data ----------
    enrolled   = _read_csv("enrolled_courses.csv",        {":START_ID(Student)":"string", ":END_ID(Course)":"string"})
    leads_to   = _read_csv("leads_to.csv",                {":START_ID(Course)":"string",  ":END_ID(Course)":"string"})
    prereqs    = _read_csv("prerequisites.csv",           {":START_ID(Course)":"string",  ":END_ID(Course)":"string"})
    completed  = _read_csv("completed_courses.csv",       {":START_ID(Student)":"string", ":END_ID(Course)":"string"})
    teaching   = _read_csv("teaching.csv",                {":START_ID(Faculty)":"string", ":END_ID(Course)":"string"})
    faculty    = _read_csv("faculty.csv",                 {"id:ID(Faculty)":"string"})
    courses    = _read_csv("courses.csv",                 {"id:ID(Course)":"string"})
    students   = _read_csv("students.csv",                {"id:ID(Student)":"string"})

    # ---------- seeds: current + completed (UNION) ----------
    cur = (
        enrolled.loc[enrolled[":START_ID(Student)"]==student_id, [":END_ID(Course)"]]
        .rename(columns={":END_ID(Course)":"course_id"})
        .dropna().drop_duplicates()
    )
    done = (
        completed.loc[completed[":START_ID(Student)"]==student_id, [":END_ID(Course)","grade"]]
        .rename(columns={":END_ID(Course)":"completed_course"})
        .dropna().drop_duplicates()
    )
    seeds = pd.DataFrame({"course_id": pd.unique(pd.concat([cur["course_id"], done["completed_course"]], ignore_index=True))})

    # ---------- leads_to from seeds ----------
    nxt = (
        leads_to.loc[leads_to[":START_ID(Course)"].isin(seeds["course_id"]), [":END_ID(Course)"]]
        .rename(columns={":END_ID(Course)":"candidate_course"})
        .dropna().drop_duplicates()
    )

    if nxt.empty:
        out = {"student_id": student_id, "results": []}
        return json.dumps(out, indent=2)

    # ---------- prerequisites filtering ----------
    pr = prereqs.loc[
        prereqs[":END_ID(Course)"].isin(nxt["candidate_course"]),
        [":START_ID(Course)", ":END_ID(Course)", "minGrade"]
    ].rename(columns={":START_ID(Course)":"prereq_course", ":END_ID(Course)":"candidate_course"})
    if pr.empty:
        eligible_courses = set(nxt["candidate_course"])
    else:
        prj = pr.merge(done, left_on="prereq_course", right_on="completed_course", how="left")
        prj["met"] = prj.apply(lambda r: grade_meets(r.get("grade"), r.get("minGrade")), axis=1)
        all_met = prj.groupby("candidate_course")["met"].all().reset_index()
        eligible_courses = set(all_met.loc[all_met["met"], "candidate_course"])

    eligible_courses -= set(done["completed_course"].tolist())

    eligible = pd.DataFrame({"course_id": list(eligible_courses)})

    
    if eligible.empty:
        out = {"student_id": student_id, "results": []}
        return json.dumps(out, indent=2)

    # ---------- expand to classes via teaching ----------
    classes = teaching.loc[
        teaching[":END_ID(Course)"].isin(eligible["course_id"]),
        [":START_ID(Faculty)", ":END_ID(Course)"]
    ].rename(columns={":START_ID(Faculty)":"faculty_id", ":END_ID(Course)":"course_id"}).dropna().drop_duplicates()


    if classes.empty:
        out = {"student_id": student_id, "results": []}
        return json.dumps(out, indent=2)

    # ---------- faculty avgRating ----------
    fac = faculty[["id:ID(Faculty)", "avgRating:float"]].rename(
        columns={"id:ID(Faculty)":"faculty_id", "avgRating:float":"avgRating"}
    )
    fac["avgRating"] = pd.to_numeric(fac["avgRating"], errors="coerce")
    classes = classes.merge(fac, on="faculty_id", how="left")
    classes["avgRating"].fillna(1.0, inplace=True)

    stu = students.loc[students["id:ID(Student)"] == student_id].copy()
    if stu.empty:
        raise ValueError(f"Student {student_id} not found in students.csv")

    s = stu.iloc[0]

    # NEW: robustly get the student's name from students.csv
    name_col = "name" if "name" in students.columns else next(
        (c for c in ["Name", "full_name", "Full Name"] if c in students.columns),
        None
    )
    student_name = str(s.get(name_col)) if name_col and pd.notna(s.get(name_col)) else None
    s_learning = str(s.get("learningStyle","")).strip()
    s_load  = pd.to_numeric(s.get("preferredCourseLoad"), errors="coerce")  # [2,5]
    s_pace  = pace_map.get(str(s.get("preferredPace","")).strip(), np.nan)
    s_mode  = mode_map.get(str(s.get("preferredInstructionMode","")).strip(), np.nan)

    crs = courses[["id:ID(Course)", "avgTimeCommitment:int", "avgDifficulty:float", "instructionModes"]].rename(
        columns={
            "id:ID(Course)":"course_id",
            "avgTimeCommitment:int":"avgTimeCommitment",
            "avgDifficulty:float":"avgDifficulty",
        }
    )
    crs["avgTimeCommitment"] = pd.to_numeric(crs["avgTimeCommitment"], errors="coerce")
    crs["avgDifficulty"]     = pd.to_numeric(crs["avgDifficulty"], errors="coerce")

    # ---------- learner success column per course (robust detection) ----------
    def _normalize(s: str) -> str:
        return "" if s is None else str(s).strip()

    s_learning_norm = _normalize(s_learning)

    # candidates we will search for, case-insensitive and with optional :float suffix
    def _cands(base: str) -> list[str]:
        return [
            f"{base}LearnerSuccess",
            f"{base}LearnerSuccess:float",
            f"{base.replace(' ', '')}LearnerSuccess",
            f"{base.replace(' ', '')}LearnerSuccess:float",
        ]

    # build a case-insensitive lookup of courses columns
    lower_cols = {c.lower(): c for c in courses.columns}

    # try exact-style matches first
    chosen_col = None
    for cand in _cands(s_learning_norm):
        if cand.lower() in lower_cols:
            chosen_col = lower_cols[cand.lower()]
            break

    # if not found, try any column that contains 'learnersuccess' and also the style token
    if not chosen_col:
        tokens = [s_learning_norm.lower().replace(" ", ""), s_learning_norm.lower()]
        ls_cols = [c for c in courses.columns if "learnersuccess" in c.lower()]
        best = [c for c in ls_cols if any(t in c.lower() for t in tokens)]
        if len(best) == 1:
            chosen_col = best[0]

    # final fallback: if exactly one *any* LearnerSuccess column exists, use it
    if not chosen_col:
        ls_cols = [c for c in courses.columns if "learnersuccess" in c.lower()]
        if len(ls_cols) == 1:
            chosen_col = ls_cols[0]

    if chosen_col:
        succ = courses[["id:ID(Course)", chosen_col]].rename(
            columns={"id:ID(Course)": "course_id", chosen_col: "learner_success"}
        )
        succ["learner_success"] = pd.to_numeric(succ["learner_success"], errors="coerce")
    else:
        # neutral multiplier when we can't find a column
        succ = pd.DataFrame(columns=["course_id", "learner_success"])


    classes = classes.merge(crs, on="course_id", how="left").merge(succ, on="course_id", how="left")

    # ---------- coefficients ----------
    coef_success = classes["learner_success"].fillna(1.0)

    s_load_n = norm_range(s_load, 2, 5)
    time_n   = classes["avgTimeCommitment"].apply(lambda v: norm_range(v, 2, 11))
    coef_load_time = (1.0 - (s_load_n - time_n) ** 2).fillna(1.0).clip(lower=0.0)

    diff_n = classes["avgDifficulty"].apply(lambda v: norm_range(v, 3, 10))
    coef_pace_diff = (1.0 - ((s_pace * diff_n) ** 2 if not np.isnan(s_pace) else pd.Series(1.0, index=diff_n.index))).fillna(1.0).clip(lower=0.0)

    def avg_mode_value(modes: str):
        if not isinstance(modes, str) or not modes:
            return np.nan
        vals = [mode_map.get(p.strip(), np.nan) for p in modes.split(";")]
        vals = [v for v in vals if not np.isnan(v)]
        return np.mean(vals) if vals else np.nan

    c_mode = classes["instructionModes"].apply(avg_mode_value)
    coef_mode = (1.0 - ((s_mode * c_mode) ** 2 if not np.isnan(s_mode) else pd.Series(1.0, index=c_mode.index))).fillna(1.0).clip(lower=0.0)

    classes["initial_score"]   = classes["avgRating"].fillna(0.0)
    classes["coef_success"]    = coef_success
    classes["coef_load_time"]  = coef_load_time
    classes["coef_pace_diff"]  = coef_pace_diff
    classes["coef_mode"]       = coef_mode
    classes["final_score"] = (
        classes["initial_score"]
        * classes["coef_success"]
        * classes["coef_load_time"]
        * classes["coef_pace_diff"]
        * classes["coef_mode"]
    )

    # ---------- sort & top_k ----------
    classes = classes.replace([np.inf,-np.inf], np.nan).dropna(subset=["final_score"])
    ranked = classes.sort_values("final_score", ascending=False).head(top_k).copy()

    # Optional friendly labels (if present)
    if "name" in courses.columns:
        course_names = courses[["id:ID(Course)","name"]].rename(
            columns={"id:ID(Course)":"course_id","name":"course_name"}
        )
        ranked = ranked.merge(course_names, on="course_id", how="left")
    if "name" in faculty.columns:
        faculty_names = faculty[["id:ID(Faculty)","name"]].rename(
            columns={"id:ID(Faculty)":"faculty_id","name":"faculty_name"}
        )
        ranked = ranked.merge(faculty_names, on="faculty_id", how="left")

    # ---------- output ----------
    results = []
    for _, r in ranked.iterrows():
        results.append({
            "course_id": r.get("course_id"),
            "course_name": r.get("course_name") if pd.notna(r.get("course_name")) else None,
            "faculty_id": r.get("faculty_id"),
            "faculty_name": r.get("faculty_name") if pd.notna(r.get("faculty_name")) else None,
            "initial_prof_rating": float(r.get("avgRating") or 0.0),
            "coefficients": {
                "learner_success": float(r.get("coef_success") or 0.0),
                "load_vs_time": float(r.get("coef_load_time") or 0.0),
                "pace_vs_difficulty": float(r.get("coef_pace_diff") or 0.0),
                "instruction_mode": float(r.get("coef_mode") or 0.0),
            },
            "course_attrs": {
                "avgTimeCommitment": None if pd.isna(r.get("avgTimeCommitment")) else float(r.get("avgTimeCommitment")),
                "avgDifficulty": None if pd.isna(r.get("avgDifficulty")) else float(r.get("avgDifficulty")),
                "instructionModes": None if pd.isna(r.get("instructionModes")) else str(r.get("instructionModes")),
                "learner_success": None if pd.isna(r.get("learner_success")) else float(r.get("learner_success")),
            },
            "final_score": float(r["final_score"]),
        })

    payload = {
        "student_id": student_id,
        "student_name": student_name or student_id,  # fallback to ID if name missing
        "count": len(results),
        "results": results,
    }
    
    return json.dumps(payload, indent=2)
