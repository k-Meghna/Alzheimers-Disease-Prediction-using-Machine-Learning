# 🧠 Alzheimer's Disease Prediction using Machine Learning

This project aims to predict the likelihood of Alzheimer's Disease using patient data from the [OASIS Longitudinal Dataset](https://www.oasis-brains.org/). The project covers data cleaning, analysis, model building, evaluation using performance metrics, ROC  curves and visualization using Python.

## 📝 Project Objective
The goal is to use machine learning classifiers to identify early patterns associated with dementia and support preliminary Alzheimer’s risk screening.

This tool is **not** intended for clinical use but rather for educational and demonstrative purposes.

---

## 📁 Dataset
- **Source:** OASIS Longitudinal Dataset
- **File:** `oasis_longitudinal.csv`
- **Total Records:** 373 entries × 15 features
- **Target Variable:** `Group` (encoded as 0 = Nondemented, 1 = Demented)

### 📌 Features Used in Modeling:
| Feature | Description |
|---------|-------------|
| M/F     | Gender (Male=1, Female=0) |
| Age     | Age in years |
| EDUC    | Years of education |
| SES     | Socioeconomic Status |
| MMSE    | Mini-Mental State Exam score |
| eTIV    | Estimated Total Intracranial Volume |
| nWBV    | Normalized Whole Brain Volume |
| ASF     | Atlas Scaling Factor |

---

## 🧹 Preprocessing
- Filled missing values in `SES` with median and `MMSE` with mean.
- Merged 'Converted' into 'Demented' category in `Group`.
- Encoded categorical columns: 
  - `Group`: Demented = 1, Nondemented = 0
  - `M/F`: Male = 1, Female = 0
- Dropped irrelevant fields: `Subject ID`, `MRI ID`, `Hand`.

---

## 🔍 Exploratory Data Analysis (EDA)
- Gender distribution across groups via stacked bar chart.
- KDE plots for Age and MMSE vs. Dementia groups.
- Outlier detection using IQR for numeric features.

---

## 📊 Machine Learning Models

Dataset was split into **70% training / 30% testing** with **stratification** to preserve class balance.

---

### ✅ 1. Support Vector Machine (SVM)
- **Kernel:** Linear
- **C Parameter:** 0.1

### ✅ 2. Decision Tree Classifier
- **Criterion:** Entropy
- **Max Depth:** 5

### ✅ 3. Random Forest Classifier
- **Estimators:** 200
- **Max Depth:** 8
- **Criterion:** Gini
- **Max Features:** sqrt

---

## 🧪 Evaluation Metrics
Each model was evaluated using:
- Confusion Matrix
- Classification Report: Precision, Recall, F1-score
- Accuracy Score
- ROC Curve and AUC

---

## 📈 Key Observations
- Demented cases are more frequent among 70–80 age group.
- Nondemented individuals scored higher MMSE scores.
- Random Forest achieved the best performance overall.

---

## 🛠 Libraries Used
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `sklearn` - SVC, DecisionTreeClassifier, RandomForestClassifier, metrics

---

## 🗂 Project Structure
- `Alzheimer's Final.py` – Full script with preprocessing, modeling, and evaluation logic.
- `oasis_longitudinal.csv` – Raw dataset.
- Visual Plots generated inline using `matplotlib` and `seaborn`.

---

## 🚀 Future Enhancements
- Incorporate feature scaling and PCA.
- Explore cross-validation, ensemble stacking and hyperparameter tuning using GridSearchCV.
- Build interactive front-end with Streamlit

---

## ⚠️ Disclaimer
This tool is built for educational purposes only and not a substitute for medical diagnosis. Please consult a certified healthcare provider for any clinical concerns.

---

### 👩‍💻📌 Author
**Meghna Kattekola**  
M.S. in Data Analytics Engineering  
George Mason University

                       ---***---

