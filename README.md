# 🎓 Student Dropout Prediction

A Logistic Regression model that predicts whether a student is at risk of dropping out,
with a Streamlit app that returns a dropout probability and a risk level (Low / Medium / High).

Live app: https://student-dropout-prediction-2026.streamlit.app/

## Problem
Identify students who may need extra support early, using academic, demographic,
socioeconomic and enrollment data.

## Data
Predict Students' Dropout and Academic Success dataset (4,424 students, 36 features).
Target: `Dropout` = 1, `Enrolled` / `Graduate` = 0. About 32.1% of students dropped out.

## Method
1. Cleaning (missing values, duplicates) and binary target creation
2. Exploratory analysis of grades, scholarship, tuition status and debt
3. Pipeline: One-Hot Encoding + Standard Scaling + Logistic Regression
4. Evaluation: accuracy, precision, recall, F1, ROC-AUC, confusion matrix

## Results

| Metric    | Score |
|-----------|-------|
| Accuracy  | 0.889 |
| Precision | 0.878 |
| Recall    | 0.761 |
| F1-score  | 0.815 |
| ROC-AUC   | 0.932 |

**Interpretation:** The model correctly identifies about 76% of students who go on to
drop out (recall), and 88% of the students it flags are genuine dropouts (precision).
For an early-warning system, missed dropouts (false negatives) are the costlier error,
so recall is the metric to watch.

## Key findings
- **Academic performance is the strongest signal.** Students who dropped out averaged a grade
  of 7.26 in the 1st semester and 5.90 in the 2nd, versus 12.24 and 12.28 for other students.
  They also passed far fewer curricular units (2.55 and 1.94 per semester, versus 5.73 and 5.62).
  Second-semester grades and approved units had the strongest correlation with dropout.
- **Financial factors matter.** 86.6% of students whose tuition fees were not up to date dropped
  out, versus 24.7% of those who were. Debtors dropped out at 62.0% (versus 28.3%), while
  scholarship holders dropped out far less (12.2% versus 38.7%).
- **Demographics add smaller effects.** Male students dropped out more often than female
  students (45.1% versus 25.1%), and older age at enrollment was positively associated with dropout.

These are associations, not proven causes.

## Risk levels used in the app

| Dropout probability | Risk level |
|---------------------|------------|
| Below 40%           | Low        |
| 40% to 70%          | Medium     |
| 70% or above        | High       |

## Application features
- Readable dropdowns for course, nationality, qualifications and occupations
- Built-in example students (strong, borderline, struggling) for quick testing
- Dropout probability, risk level and a suggested action for each student

## Project files
- `app.py`: Streamlit application
- `labels.py`: readable names for the dataset's numeric category codes
- `dropout_model.pkl`: trained Logistic Regression pipeline
- `metadata.json`: feature list, dropdown options and model metrics
- `requirements.txt`: dependencies
- `Student_Dropout_Prediction.ipynb`: full notebook (EDA, training, evaluation)

## Run locally

    pip install -r requirements.txt
    streamlit run app.py

## Use case
An early-warning system: advisors enter student data, and students with a high
dropout probability are flagged early for counselling, tutoring or financial support.

## Limitations
- The model is trained on data from a single institution, so results may not transfer elsewhere.
- Predictions are probabilities, not certainties, and should support human decisions, not replace them.

## Author
Saira Batool

## Data source
Realinho, V., Machado, J., Baptista, L., Martins, M.V. (2022). Predicting Student
Dropout and Academic Success. Data, 7(11), 146. Dataset on the UCI Machine Learning Repository.
