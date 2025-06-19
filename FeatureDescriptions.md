# Feature Descriptions: Alzheimer's Risk Screening Tool

This document provides descriptions and typical value ranges for the input features used in our machine learning model for Alzheimer's detection.

---

### 1. *Age*
- *Description:* Patient’s age in years.
- *Typical Range:* 50 – 100  
- *Importance:* Age is a major risk factor for dementia-related disorders.

---

### 2. *Gender (M/F)*
- *Description:* Biological sex of the patient.
- *Values:* 1 = Male, 0 = Female  
- *Importance:* Alzheimer's prevalence can vary slightly with gender.

---
### 3. *Years of Education (EDUC)*
- *Description:* Number of years the person spent in formal education.
- *Typical Range:* 0 – 25  
- *Importance:* Higher education levels may offer cognitive reserve against decline.

---

### 4. *Socioeconomic Status (SES)*
- *Description:* An index measuring economic and social position.
- *Typical Range:* 1 (Low) – 5 (High)  
- *Importance:* Linked to access to healthcare and cognitive stimulation.

---

### 5. *Mini-Mental State Exam (MMSE)*
- *Description:* A 30-point test assessing cognitive function.
- *Typical Range:* 0 – 30  
- *Interpretation:*  
  - 24–30 = Normal  
  - 20–23 = Mild impairment  
  - 10–19 = Moderate impairment  
  - <10 = Severe impairment

---

### 6. *Estimated Total Intracranial Volume (eTIV)*
- *Description:* Estimated volume of the entire cranial space.
- *Typical Range:* 1100 – 2000 cm³  
- *Importance:* Lower eTIV values may correlate with atrophy in dementia.

---

### 7. *Normalized Whole Brain Volume (nWBV)*
- *Description:* Fraction of brain volume compared to total cranial volume.
- *Typical Range:* 0.65 – 0.90  
- *Importance:* Lower values suggest brain shrinkage associated with Alzheimer’s.

---

### 8. *Atlas Scaling Factor (ASF)*
- *Description:* A scaling factor for brain size normalization.
- *Typical Range:* 0.80 – 1.50  
- *Importance:* Adjusts for individual differences in brain dimensions.

---

> ⚠ *Note:* These ranges are based on observed data in the OASIS dataset and clinical studies. They are not diagnostic thresholds.