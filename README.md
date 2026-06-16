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