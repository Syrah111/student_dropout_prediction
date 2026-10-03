import json
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Student Dropout Risk Predictor", page_icon="🎓", layout="wide")


@st.cache_resource
def load_assets():
    model = joblib.load("dropout_model.pkl")
    with open("metadata.json") as f:
        meta = json.load(f)
    return model, meta


model, meta = load_assets()
options, defaults = meta["cat_options"], meta["defaults"]

# ---------- Readable labels (codes follow the dataset's data dictionary) ----------
YES_NO = {0: "No", 1: "Yes"}
GENDER = {0: "Female", 1: "Male"}
ATTENDANCE = {1: "Daytime", 0: "Evening"}
MARITAL = {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced",
           5: "Facto union", 6: "Legally separated"}
COURSE = {33: "Biofuel Production Technologies", 171: "Animation & Multimedia Design",
          8014: "Social Service (evening)", 9003: "Agronomy", 9070: "Communication Design",
          9085: "Veterinary Nursing", 9119: "Informatics Engineering", 9130: "Equinculture",
          9147: "Management", 9238: "Social Service", 9254: "Tourism", 9500: "Nursing",
          9556: "Oral Hygiene", 9670: "Advertising & Marketing Management",
          9773: "Journalism & Communication", 9853: "Basic Education",
          9991: "Management (evening)"}

# ---------- Example students for quick testing ----------
def academic(enrolled, evaluated, approved, grade, without):
    d = {}
    for sem in ("1st", "2nd"):
        p = f"Curricular units {sem} sem"
        d.update({f"{p} (credited)": 0, f"{p} (enrolled)": enrolled,
                  f"{p} (evaluations)": evaluated, f"{p} (approved)": approved,
                  f"{p} (grade)": grade, f"{p} (without evaluations)": without})
    return d


SCENARIOS = {
    "Custom (manual entry)": {},
    "Strong student": {**academic(6, 6, 6, 15.0, 0), "Tuition fees up to date": 1,
                       "Debtor": 0, "Scholarship holder": 1, "Age at enrollment": 19},
    "Borderline student": {**academic(6, 8, 2, 11.0, 0), "Tuition fees up to date": 1, "Debtor": 0, "Scholarship holder": 0, "Age at enrollment": 21},
    "Struggling student": {**academic(6, 8, 1, 8.0, 2), "Tuition fees up to date": 0,
                           "Debtor": 1, "Scholarship holder": 0, "Age at enrollment": 30},
}


def apply_scenario():
    for key, value in SCENARIOS[st.session_state["scenario"]].items():
        st.session_state[key] = value


# ---------- Input helpers ----------
row = {}


def select(label, col, labels=None):
    opts = options[col]
    idx = opts.index(defaults[col]) if defaults[col] in opts else 0
    fmt = (lambda v: labels.get(v, f"Code {v}")) if labels else (lambda v: f"Code {v}")
    row[col] = st.selectbox(label, opts, index=idx, format_func=fmt, key=col)


def int_input(label, col, lo, hi):
    val = int(min(max(defaults[col], lo), hi))
    row[col] = st.number_input(label, min_value=lo, max_value=hi, value=val, step=1, key=col)


def float_input(label, col, lo, hi, step=0.1):
    val = float(min(max(defaults[col], lo), hi))
    row[col] = st.number_input(label, min_value=float(lo), max_value=float(hi),
                               value=val, step=float(step), key=col)


from labels import MARITAL, COURSE, APP_MODE, PREV_QUAL, NATIONALITY, QUALIFICATION, OCCUPATION


def select(label, col, labels=None):
    opts = list(options[col])
    fmt = (lambda v: labels.get(v, f"Code {v}")) if labels else (lambda v: str(v))
    idx = opts.index(defaults[col]) if defaults[col] in opts else 0
    row[col] = st.selectbox(label, opts, index=idx, format_func=fmt, key=col)


# ---------- Sidebar ----------
with st.sidebar:
    st.header("⚙️ Quick Test Cases")
    st.selectbox("Load an example student", list(SCENARIOS), key="scenario",
                 on_change=apply_scenario)
    st.divider()
    st.subheader("📈 Model performance")
    m = meta["metrics"]
    st.write(f"Accuracy: **{m['accuracy']}**")
    st.write(f"Recall: **{m['recall']}**")
    st.write(f"ROC-AUC: **{m['roc_auc']}**")
    st.caption("Risk levels: Low < 40% · Medium 40–70% · High ≥ 70%")

# ---------- Header ----------
st.title("🎓 Student Dropout Risk Predictor")
st.write("An early-warning tool: enter a student's details to estimate their probability "
         "of dropping out and identify who may need extra support.")
st.divider()

# ---------- Student information ----------
st.header(" Student Information")
c1, c2, c3 = st.columns(3)
with c1:
    select("Marital status", "Marital status", MARITAL)
    select("Application mode", "Application mode", APP_MODE)
    int_input("Application order", "Application order", 0, 9)
with c2:
    select("Course", "Course", COURSE)
    select("Attendance", "Daytime/evening attendance", ATTENDANCE)
    select("Previous qualification", "Previous qualification", PREV_QUAL)
with c3:
    select("Nationality", "Nacionality", NATIONALITY)
    int_input("Age at enrollment", "Age at enrollment", 15, 70)
    select("Gender", "Gender", GENDER)

# ---------- Family ----------
st.header(" Family Background")
c1, c2, c3, c4 = st.columns(4)
with c1:
    select("Mother's qualification", "Mother's qualification", QUALIFICATION)
with c2:
    select("Father's qualification", "Father's qualification", QUALIFICATION)
with c3:
    select("Mother's occupation", "Mother's occupation", OCCUPATION)
with c4:
    select("Father's occupation", "Father's occupation", OCCUPATION)

# ---------- Socioeconomic ----------
st.header(" Socioeconomic Status")
c1, c2, c3, c4, c5, c6 = st.columns(6)
with c1:
    select("Displaced", "Displaced", YES_NO)
with c2:
    select("Special needs", "Educational special needs", YES_NO)
with c3:
    select("Debtor", "Debtor", YES_NO)
with c4:
    select("Tuition up to date", "Tuition fees up to date", YES_NO)
with c5:
    select("Scholarship", "Scholarship holder", YES_NO)
with c6:
    select("International", "International", YES_NO)

# ---------- Academic ----------
st.header(" Academic Performance")
cols = st.columns(2)
for sem, col in zip(("1st", "2nd"), cols):
    p = f"Curricular units {sem} sem"
    with col:
        st.subheader(f"{sem} Semester")
        int_input("Credited units", f"{p} (credited)", 0, 60)
        int_input("Enrolled units", f"{p} (enrolled)", 0, 60)
        int_input("Evaluations", f"{p} (evaluations)", 0, 60)
        int_input("Approved units", f"{p} (approved)", 0, 60)
        float_input("Average grade (0–20)", f"{p} (grade)", 0.0, 20.0, 0.1)
        int_input("Without evaluations", f"{p} (without evaluations)", 0, 60)

# ---------- Economic ----------
st.header(" Economic Indicators")
c1, c2, c3 = st.columns(3)
with c1:
    float_input("Unemployment rate (%)", "Unemployment rate", 0.0, 40.0, 0.1)
with c2:
    float_input("Inflation rate (%)", "Inflation rate", -5.0, 15.0, 0.1)
with c3:
    float_input("GDP", "GDP", -10.0, 10.0, 0.01)

st.divider()

# ---------- Prediction ----------
if st.button("🔮 Predict Dropout Risk", type="primary", use_container_width=True):
    input_df = pd.DataFrame([{**defaults, **row}])[meta["features"]]
    probability = float(model.predict_proba(input_df)[0][1])
    prediction = int(model.predict(input_df)[0])

    if probability >= 0.70:
        level, icon, advice = "High Risk", "🔴", "Recommend immediate outreach: academic counselling, tutoring and financial-aid review."
    elif probability >= 0.40:
        level, icon, advice = "Medium Risk", "🟡", "Monitor closely and offer mentoring or study-support resources."
    else:
        level, icon, advice = "Low Risk", "🟢", "No immediate concern. Continue routine monitoring."

    st.subheader("📊 Prediction Result")
    r1, r2 = st.columns(2)
    r1.metric("Dropout Probability", f"{probability * 100:.2f}%")
    r2.metric("Risk Level", f"{icon} {level}")
    st.progress(probability)

    if prediction == 1:
        st.warning("The model predicts that this student is **at risk** of dropping out.")
    else:
        st.success("The model predicts that this student is **not at risk** of dropping out.")
    st.info(advice)
