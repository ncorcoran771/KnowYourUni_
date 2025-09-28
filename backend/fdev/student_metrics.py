import os, json
import numpy as np
import pandas as pd
import warnings

from pathlib import Path

HERE = Path(__file__).resolve().parent       # folder of student_metrics.py (or main.py)
DATA_DIR = (HERE / ".." / "umbc_data" / "csv").resolve()  # adjust .. as needed


def study_buddy_finder(
	student_id: str,
	top_n: int = 10,
	sort_by: str = "overall",   # "mean" | "max" | "cand_func"
	data_dir: str = DATA_DIR,
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
    data_dir: str = DATA_DIR,
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


# We'll provide a demo that the user can run with their actual CSV.
# This cell creates a small synthetic dataset to demonstrate the visualization
# and defines a reusable function `plot_avg_grades_by_department_and_term` that
# works with a real completed_courses.csv at data_dir.
import pandas as pd
import numpy as np
import re
import os
import matplotlib.pyplot as plt
from datetime import datetime, timezone
import warnings
import json
from sklearn.linear_model import LinearRegression

def clean_nan_columns(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, float).copy()
    m = np.nanmean(a, axis=0)
    i = np.isnan(a)
    a[i] = m[np.nonzero(i)[1]]
    return a

def makepreds(vals):

    #need to hand clean data first
    data = vals.T.values

    data = clean_nan_columns(data)

    num_depts = data.shape[1]
    f_cnt = 3
    feats = np.zeros((data.shape[0], f_cnt), dtype=np.float32)
    ytrue = np.zeros((data.shape[0]), dtype=np.float32)
    preds = []

    for d in range(num_depts):

        for n in range(f_cnt):
            for m in range(f_cnt,data.shape[0]):
                #print(f"OPERATION: ln ( {data[m, n]} / {data[m-n, n]} )")
                #print(f"OPERATION: m= {m}, n={n}")
                feats[m, n] = np.log(data[m, d]/data[m-n-1, d])

        for m in range(data.shape[0]-1):
            ytrue[m] = np.log(data[m+1, d]/data[m, d])

        X = feats[f_cnt:-1]
        y = ytrue[f_cnt:-1]

        lr = LinearRegression().fit(X, y)
        pred = lr.predict(feats[-1:,:])

        #logical fail safe! not for the long term, only for
        #short term product assurance, and not Logan Kelsch
        #can validate this only appeared once but visually
        #destroys the hook of this ML!!!!! ask Logan about it!
        loc_mean = np.mean(data[:,d])
        min_range = min(data[-1,d], loc_mean)
        max_range = max(data[-1,d], loc_mean)
        if(pred < min_range-0.5 or pred > max_range+0.5):
            pred = loc_mean

        #append and get out of here goodness 5:53am
        preds.append(np.exp(pred)*data[-1:,d])

    return np.array(preds)


# ---------- Helpers ----------
GRADE_RANK = {
    "A+": 4.33, "A": 4, "A-": 3.67,
    "B+": 3.33,  "B": 3,  "B-": 2.67,
    "C+": 2.33,  "C": 2,  "C-": 1.67,
    "D+": 1.33,  "D": 1,  "D-": 0.67,
    "F": 0
}

TERM_ORDER = {"Winter": 0, "Spring": 1, "Summer": 2, "Fall": 3}
TERMS_SEQ   = ["Winter", "Spring", "Summer", "Fall"]  # for next-term inference
warnings.filterwarnings("ignore")


def _term_sort_key(term: str):
    """
    Convert a term string like 'Spring2024' into a tuple for sorting: (year, season_order).
    If parsing fails, put it at the end, preserving input order via 9999.
    """
    if not isinstance(term, str):
        return (9999, 9)
    m = re.match(r"([A-Za-z]+)\s*([0-9]{4})", term) or re.match(r"([A-Za-z]+)([0-9]{4})", term)
    if not m:
        return (9999, 9)
    season, year = m.group(1), int(m.group(2))
    season_key = TERM_ORDER.get(season.capitalize(), 9)
    return (year, season_key)

def _parse_term(term: str):
    m = re.match(r"([A-Za-z]+)\s*([0-9]{4})", term) or re.match(r"([A-Za-z]+)([0-9]{4})", term)
    if not m:
        return None, None
    return m.group(1).capitalize(), int(m.group(2))

def _next_term_label(last_term: str) -> str:
    season, year = _parse_term(last_term)
    if season is None:
        # fallback: append '+' if unknown format
        return f"{last_term}+1"
    idx = TERMS_SEQ.index(season) if season in TERMS_SEQ else 1
    if idx == len(TERMS_SEQ) - 1:  # Fall -> Winter next year
        return f"{TERMS_SEQ[0]}{year + 1}"
    else:
        return f"{TERMS_SEQ[idx + 1]}{year}"

def _grade_to_numeric(g):
    if pd.isna(g):
        return np.nan
    g = str(g).strip()
    return GRADE_RANK.get(g, np.nan)


def dyn_agg_gpa_forecasting(
    dept_letter: str = 'Z'  # when agg == "course_in_department", e.g., "C" or "B"
):
    """
    Build time series, predict next term, and return JSON for frontend.
    - Always includes an OVERALL/UNIVERSITY series.
    - agg="department": rows are dept letters ('C','B'), averaged per term.
    - agg="course_in_department": filter to dept_letter and rows are course IDs, averaged per term.

    Returns: forecast_json (dict) with meta + series (history + dashed forecast segment)
    """
    # ---- Load data ----
    if os.path.join(DATA_DIR, 'completed_courses.csv') is None or not os.path.exists(os.path.join(DATA_DIR, 'completed_courses.csv')):
        raise FileNotFoundError("Provide completed_courses.csv or df_completed.")
    df_completed = pd.read_csv(
        os.path.join(DATA_DIR, 'completed_courses.csv'),
        dtype={":END_ID(Course)": "string", "term": "string", "grade": "string"}
    )
    if not os.path.exists(os.path.join(DATA_DIR, 'courses.csv')):
        raise FileNotFoundError(os.path.join(DATA_DIR, 'courses.csv'))
    df_courses = pd.read_csv(
        os.path.join(DATA_DIR, 'courses.csv'),
        dtype={"id:ID(Course)": "string", "name": "string", "department": "string"}
    )

    # ---- Prepare base long table ----
    df = df_completed.dropna(subset=[":END_ID(Course)", "grade", "term"]).copy()
    df[":END_ID(Course)"] = df[":END_ID(Course)"].astype(str)
    df["dept_letter"] = df[":END_ID(Course)"].str.slice(0, 1)
    # level is 6th char (index 5); guard short strings
    df["level_digit"] = df[":END_ID(Course)"].str.slice(5, 6).str.extract(r"(\d)").fillna("0").astype(int)
    df["grade_numeric"] = df["grade"].apply(_grade_to_numeric)

    # ---- Department title map from courses.csv (first match wins) ----
    # Example: for 'C' → "Computer Science", for 'B' → "Biology"
    df_courses["dept_letter"] = df_courses["id:ID(Course)"].astype(str).str.slice(0, 1)
    dept_titles = (
        df_courses.dropna(subset=["dept_letter", "department"])
                  .drop_duplicates(subset=["dept_letter"])
                  .set_index("dept_letter")["department"]
                  .to_dict()
    )

    # ---- Aggregation selection → build plot_wide (rows × terms), labels, metadata ----
    if dept_letter not in ['B','C']:
        agg = 'Course'
        grouped = (
            df.groupby(["dept_letter", "term"], as_index=False)
              .agg(avg_grade=("grade_numeric", "mean"), count=("grade_numeric", "size"))
        )
        ordered_terms = sorted(grouped["term"].unique(), key=_term_sort_key)
        plot_wide = (
            grouped.pivot(index="dept_letter", columns="term", values="avg_grade")
                   .reindex(columns=ordered_terms)
        )
        row_labels = plot_wide.index.tolist()
        # Titles for each row (department)
        row_titles = {dl: dept_titles.get(dl, f"Dept {dl}") for dl in row_labels}
        row_kind = "department"
        row_course_map = {}  # not used in this mode

    elif dept_letter in ['B','C']:
        agg = 'Department'
        if not dept_letter:
            raise ValueError("Provide dept_letter (e.g., 'C' or 'B') when agg='course_in_department'.")
        df_f = df.loc[df["dept_letter"] == dept_letter].copy()
        if df_f.empty:
            raise ValueError(f"No rows found for department letter '{dept_letter}'.")
        grouped = (
            df_f.groupby([":END_ID(Course)", "term"], as_index=False)
                .agg(avg_grade=("grade_numeric", "mean"), count=("grade_numeric", "size"))
        )
        ordered_terms = sorted(grouped["term"].unique(), key=_term_sort_key)
        plot_wide = (
            grouped.pivot(index=":END_ID(Course)", columns="term", values="avg_grade")
                   .reindex(columns=ordered_terms)
        )
        row_labels = plot_wide.index.tolist()  # course IDs
        # Map course_id -> (course_name, department_title)
        course_meta = (
            df_courses.set_index("id:ID(Course)")[["name", "department"]]
                      .to_dict(orient="index")
        )
        row_titles = {
            cid: course_meta.get(cid, {}).get("name", cid) for cid in row_labels
        }
        row_course_map = {
            cid: {
                "course_id": cid,
                "course_name": course_meta.get(cid, {}).get("name"),
                "department_title": course_meta.get(cid, {}).get("department"),
                "department_letter": dept_letter,
            }
            for cid in row_labels
        }
        row_kind = "course"
    else:
        raise ValueError("agg must be 'department' or 'course_in_department'.")

    # ---- Overall / University series (one row) ----
    overall = (
        df.groupby("term", as_index=False)
          .agg(avg_grade=("grade_numeric", "mean"))
          .set_index("term")
    )
    # Align to the same term set
    overall = overall.reindex(ordered_terms)
    overall_wide = pd.DataFrame([overall["avg_grade"].values], index=["UNIV"], columns=ordered_terms)

    # ---- Predictions (your makepreds) ----
    preds_main = makepreds(plot_wide)                     # shape (rows,)
    preds_overall = makepreds(overall_wide)               # shape (1,)

    # Next term
    last_term = ordered_terms[-1] if ordered_terms else "Spring2025"
    next_term = _next_term_label(last_term)

    # ---- Build JSON series for main rows ----
    series = []
    for i, key in enumerate(plot_wide.index.tolist()):
        row_vals = plot_wide.iloc[i]
        history = [{"term": str(t), "value": float(v), "isPred": False}
                   for t, v in row_vals.items() if pd.notna(v)]
        pred_val = float(preds_main[i]) if i < len(preds_main) and pd.notna(preds_main[i]) else None
        forecast_segment = (
            [{"term": str(last_term), "value": history[-1]["value"], "isPred": False},
             {"term": next_term, "value": pred_val, "isPred": True}]
        ) if history and pred_val is not None else []

        entry = {
            "key": str(key),
            "kind": row_kind,  # "department" or "course"
            "title": row_titles.get(key, str(key)),
            "history": history,
            "forecast_segment": forecast_segment,
            "next_point": ({"term": next_term, "value": pred_val, "isPred": True} if pred_val is not None else None),
        }
        # attach metadata depending on mode
        if row_kind == "department":
            entry["department_letter"] = str(key)
            entry["department_title"] = row_titles.get(key, f"Dept {key}")
        else:
            entry.update(row_course_map.get(key, {}))
        series.append(entry)

    # ---- Add OVERALL / UNIVERSITY series ----
    ov_vals = overall_wide.iloc[0]
    ov_hist = [{"term": str(t), "value": float(v), "isPred": False} for t, v in ov_vals.items() if pd.notna(v)]
    ov_pred = float(preds_overall[0]) if preds_overall is not None and len(preds_overall) else None
    ov_seg = (
        [{"term": str(last_term), "value": ov_hist[-1]["value"], "isPred": False},
         {"term": next_term, "value": ov_pred, "isPred": True}]
    ) if ov_hist and ov_pred is not None else []
    series.append({
        "key": "UNIV",
        "kind": "overall",
        "title": "University",
        "history": ov_hist,
        "forecast_segment": ov_seg,
        "next_point": ({"term": next_term, "value": ov_pred, "isPred": True} if ov_pred is not None else None),
    })

    # ---- Meta + payload ----
    forecast_json = {
        "meta": {
            "metric": "avg_gpa",
            "terms": [str(t) for t in ordered_terms],
            "next_term": next_term,
            "units": "GPA (0-4.00)",
            "agg": agg,
            "dept_letter": dept_letter,
            "generated_at": datetime.now(timezone.utc).isoformat()
        },
        "series": series
    }
    return forecast_json


def students_to_json() -> str:
    """
    Reads:
      - students.csv
      - student_degree.csv
    Produces JSON array with, per student:
      - Student ID          -> students['id:ID(Student)']
      - Name                -> students['name']
      - Expected Graduation -> students['expectedGraduation']
      - Major               -> student_degree[':END_ID(Degree)'] via :START_ID(Student) match
      - Financial Aid       -> students['financialAidStatus']
    """
    # --- Load CSVs ---
    this_path_ = os.path.join(DATA_DIR, "students.csv")
    othr_path_ = os.path.join(DATA_DIR, "student_degree.csv")

    if not os.path.exists(this_path_):
        raise FileNotFoundError(f"Missing students.csv at {this_path_}")
    if not os.path.exists(othr_path_):
        raise FileNotFoundError(f"Missing student_degree.csv at {othr_path_}")

    students = pd.read_csv(
        this_path_,
        dtype={
            "id:ID(Student)": "string",
            "name": "string",
            "expectedGraduation": "string",
            "financialAidStatus": "string",
        }
    )

    sdeg = pd.read_csv(
        othr_path_,
        dtype={
            ":START_ID(Student)": "string",
            ":END_ID(Degree)": "string",
        }
    )

    # --- Validate required columns (friendly error if schema differs) ---
    req_students = ["id:ID(Student)", "name", "expectedGraduation", "financialAidStatus"]
    missing_students = [c for c in req_students if c not in students.columns]
    if missing_students:
        raise KeyError(f"students.csv missing columns: {missing_students}")

    req_sdeg = [":START_ID(Student)", ":END_ID(Degree)"]
    missing_sdeg = [c for c in req_sdeg if c not in sdeg.columns]
    if missing_sdeg:
        raise KeyError(f"student_degree.csv missing columns: {missing_sdeg}")

    # --- Collapse degrees per student (handle multi-degree students) ---
    degs_per_student = (
        sdeg.dropna(subset=[":START_ID(Student)", ":END_ID(Degree)"])
            .groupby(":START_ID(Student)")[":END_ID(Degree)"]
            .apply(lambda s: sorted({str(x) for x in s if pd.notna(x)}))
            .rename("majors")
            .reset_index()
    )

    # --- Join onto students by ID ---
    merged = students.merge(
        degs_per_student,
        left_on="id:ID(Student)",
        right_on=":START_ID(Student)",
        how="left"
    )

    # If no degree rows, set empty list
    merged["majors"] = merged["majors"].apply(lambda x: x if isinstance(x, list) else [])

    # For convenience also expose a single "major" string (first major or "")
    merged["major"] = merged["majors"].apply(lambda lst: lst[0] if lst else "")

    # --- Build JSON rows with requested keys ---
    out_rows = []
    for _, r in merged.iterrows():
        out_rows.append({
            "student_id": str(r["id:ID(Student)"]) if pd.notna(r["id:ID(Student)"]) else "",
            "name":       str(r["name"]) if pd.notna(r["name"]) else "",
            "expected_graduation": str(r["expectedGraduation"]) if pd.notna(r["expectedGraduation"]) else "",
            "financial_aid_status": str(r["financialAidStatus"]) if pd.notna(r["financialAidStatus"]) else "",
            "majors": r["majors"],        # all majors (list of strings)
        })

    return json.dumps(out_rows, indent=2)

# Example: print the JSON
if __name__ == "__main__":
    print(students_to_json())