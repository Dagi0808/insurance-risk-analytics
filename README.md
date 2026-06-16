<<<<<<< HEAD
# Insurance Risk Analytics & Risk-Based Pricing System

## Project Overview

This project develops an end-to-end insurance risk analytics solution for **ACIS (Automobile Claims Insurance Services)**. The objective is to analyze insurance data, identify key risk drivers, statistically validate pricing factors, and build predictive models to support a dynamic risk-based pricing framework.

The project covers:

- Exploratory Data Analysis (EDA)
- Data quality assessment
- Continuous Integration (CI) setup
- Data Version Control (DVC)
- Statistical hypothesis testing
- Claim severity prediction
- Claim probability modeling
- Risk-based premium optimization
- Model interpretability using SHAP

---

# Business Objective

Insurance companies need accurate risk assessment methods to:

- Identify high-risk customers
- Improve pricing accuracy
- Reduce unexpected claim losses
- Create fair and data-driven premium adjustments

This project provides evidence-based insights for improving insurance segmentation and pricing strategies.

---

# Project Structure

```
insurance-risk-analytics/

│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/
│   └── processed/
│       └── insurance_clean.csv
│
├── notebooks/
│   ├── task_1_eda.ipynb
│   ├── task_3_hypothesis_testing.ipynb
│   └── task_4_modeling.ipynb
│
├── src/
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
│
├── reports/
│   ├── model_comparison.csv
│   └── shap_summary.png
│
├── requirements.txt
├── dvc.yaml
└── README.md
```

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/Dagi0808/insurance-risk-analytics.git

cd insurance-risk-analytics
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Linux/Mac

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Main libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- shap
- scipy
- dvc

---

# Task 1 & 2: Data Understanding, EDA, CI and DVC

## Exploratory Data Analysis

The dataset was analyzed to understand:

- Data distributions
- Missing values
- Outliers
- Claim behavior
- Premium and loss patterns

Key insurance metrics:

### Claim Frequency

The proportion of policies with at least one claim.

Formula:

```
Claim Frequency =
Number of policies with claims /
Total policies
```

---

### Claim Severity

Average claim amount when a claim occurs.

Formula:

```
Claim Severity =
Total Claims /
Number of Claim Events
```

---

### Loss Ratio

Measures profitability:

```
Loss Ratio =
Total Claims /
Total Premium
```

---

## Data Pipeline

The project implements a reproducible pipeline:

```
Raw Data
   |
   |
Data Cleaning
   |
   |
Processed Dataset
   |
   |
EDA
   |
   |
Statistical Testing
   |
   |
Machine Learning Models
```

---

# Continuous Integration (CI)

A GitHub Actions workflow was implemented to automatically:

- Install dependencies
- Validate Python code
- Run automated checks

Workflow location:

```
.github/workflows/ci.yml
```

---

# Data Version Control (DVC)

DVC was configured to track datasets and ensure reproducibility.

Example:

```bash
dvc init

dvc add data/raw

git add .

git commit -m "Add DVC tracking"
```

---

# Task 3: A/B Hypothesis Testing

## Objective

Statistically validate important insurance risk assumptions.

Risk was evaluated using:

- Claim Frequency
- Claim Severity
- Margin

Margin:

```
Margin =
Total Premium - Total Claims
```

---

# Hypotheses Tested

## 1. Province Risk Differences

### Null Hypothesis

```
H0:
There are no significant risk differences across provinces.
```

Test:

Chi-square test

Metric:

Claim Frequency

---

## 2. Zip Code Risk Differences

### Null Hypothesis

```
H0:
There are no significant risk differences between zip codes.
```

Test:

Chi-square test

Metric:

Claim Frequency

---

## 3. Zip Code Profitability Differences

### Null Hypothesis

```
H0:
There is no significant margin difference between zip codes.
```

Test:

Independent t-test

Metric:

Margin

---

## 4. Gender Risk Differences

### Null Hypothesis

```
H0:
There is no significant risk difference between genders.
```

Test:

Chi-square test

Metric:

Claim Frequency

---

## Decision Rule

Significance level:

```
α = 0.05
```

Decision:

```
p-value < 0.05 → Reject H0

p-value >= 0.05 → Fail to reject H0
```

---

# Task 4: Statistical Modeling & Risk-Based Pricing

## Objective

Build predictive models to estimate claim severity and support dynamic pricing.

---

# Claim Severity Prediction

Only policies with claims were used:

```
TotalClaims > 0
```

Target:

```
TotalClaims
```

---

# Feature Engineering

Created additional predictive features:

## Age Risk Groups

Customers were segmented into:

- Young
- Adult
- Middle Age
- Senior


## Transaction Features

Created:

- Transaction Year
- Transaction Month


## Historical Claim Risk

Previous claim behavior was transformed into a risk indicator.

---

# Data Preparation

Performed:

- Missing value handling
- Categorical encoding
- Feature transformation
- Train/test splitting

Dataset split:

```
80% Training
20% Testing
```

---

# Regression Models

Three models were evaluated:

## 1. Linear Regression

Baseline regression model.

---

## 2. Random Forest Regression

Ensemble model capable of capturing nonlinear relationships.

---

## 3. XGBoost Regression

Gradient boosting model optimized for predictive performance.

---

# Model Evaluation

Metrics:

## RMSE

Measures prediction error.

Lower values indicate better performance.

---

## R² Score

Measures explained variance.

Higher values indicate better prediction ability.

---

## Model Comparison

Results are stored in:

```
reports/model_comparison.csv
```

Example:

| Model | RMSE | R² |
|---|---|---|
| Linear Regression | - | - |
| Random Forest | - | - |
| XGBoost | - | - |

---

# Model Interpretability (SHAP)

SHAP was used to identify the most influential features.

Output:

```
reports/shap_summary.png
```

Important risk factors include:

- Risk Score
- Past Claims
- Vehicle Type
- Customer Age
- Income Level

---

# Business Interpretation

SHAP analysis provides evidence that:

- Customers with higher risk scores generate higher expected claim costs.
- Previous claim history is a strong predictor of future losses.
- Vehicle and customer characteristics influence insurance risk.

These findings support:

- Risk-based segmentation
- Premium adjustment
- Improved underwriting decisions

---

# Risk-Based Premium Framework

The proposed premium calculation:

```
Premium =
(P(Claim) × Predicted Severity)
+
Expense Loading
+
Profit Margin
```

Components:

## Claim Probability Model

Predicts probability of a customer submitting a claim.

---

## Severity Model

Predicts expected claim cost.

---

## Final Premium

Combines expected risk cost with business requirements.

---

# Reusable Modules

## EDA Utilities

```
src/eda_utils.py
```

Contains:

- Missing value analysis
- Province summaries
- Loss ratio calculations

---

## Hypothesis Testing

```
src/hypothesis_tests.py
```

Contains:

- Chi-square testing
- T-tests
- Hypothesis decisions

---

## Modeling Utilities

```
src/modeling.py
```

Contains:

- Model training functions
- Evaluation functions

---

# Reproducibility

To reproduce the analysis:

```bash
dvc pull

pip install -r requirements.txt

jupyter notebook
```

Run notebooks in order:

1. Task 1 EDA
2. Task 3 Hypothesis Testing
3. Task 4 Modeling

---

# Conclusion

This project delivers a complete insurance analytics pipeline combining:

- Statistical evidence
- Machine learning prediction
- Model explainability
- Business-focused pricing recommendations

The final solution enables ACIS to move from traditional pricing approaches toward a transparent, data-driven risk-based pricing system.
=======
## Task 4: Statistical Modeling & Risk-Based Pricing

### Claim Severity Models

Three regression models were evaluated:

| Model | RMSE | R2 |
|---|---|---|
| Linear Regression | ... | ... |
| Random Forest | ... | ... |
| XGBoost | ... | ... |

XGBoost achieved the best performance and was selected as the final severity model.

### SHAP Interpretation

The most influential risk factors were:

1. RiskScore
2. PastClaims
3. VehicleType
4. AnnualIncome
5. CustomValueEstimate

Business interpretation:

Higher risk scores and previous claim history increase predicted claim severity, supporting risk-based premium adjustments.
>>>>>>> task-4
