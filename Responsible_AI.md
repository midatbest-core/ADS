# Responsible AI Report

## 1. Project Overview

This project uses machine learning for e-commerce revenue prediction, including model interpretation, regional performance auditing, and drift monitoring.

## 2. Model Performance

Evaluation results on a sample of up to 5,000 records:

- MAE: 17.3158
- RMSE: 65.5402
- R² Score: 0.6799

These metrics represent the evaluated sample and do not guarantee future performance.

## 3. Explainability

SHAP feature importance identified the following features as having the highest mean absolute SHAP values:

1. Product: 33.542090
2. Unit price: 27.813210
3. Quantity: 22.526556
4. Product category: 9.280398
5. Day: 4.216606

Feature importance indicates contribution to model predictions and does not establish causation.

## 4. Fairness Audit

Regional MAE and R² values were analyzed.

Performance varies across regions. Several R² values were unavailable (NaN), which may be related to group-level data limitations.

Further evaluation should consider sample sizes, data distribution, and regional representation before deployment.

## 5. Privacy and Consent

- Use data only for authorized purposes.
- Avoid exposing personal or sensitive customer information.
- Apply access controls and secure storage.
- Minimize unnecessary data collection.
- Verify consent and applicable privacy requirements before real-world deployment.

## 6. Drift Monitoring

Population Stability Index (PSI) was used to compare reference and current data distributions.

Observed results:

- Quantity: 0.413242, High drift
- Unit price: 0.584721, High drift
- Year: 0.208788, Moderate drift
- Month: 1.217075, High drift
- Day: 0.159971, Moderate drift

These results are monitoring signals. The row-based split may reflect temporal or ordering effects and does not independently prove model degradation.

## 7. Model Limitations

- Predictions may contain errors.
- Performance differs across regions.
- Some regional metrics are unavailable.
- Historical data may not represent future transactions.
- SHAP importance does not establish causality.
- The model should not be the sole basis for high-impact decisions.

## 8. Monitoring Recommendations

- Track prediction errors over time.
- Monitor feature distribution changes.
- Review regional performance.
- Investigate missing metrics.
- Periodically retrain and evaluate the model.
- Check data quality and privacy compliance.

## 9. Conclusion

Responsible deployment requires transparency, privacy protection, fairness analysis, drift monitoring, and continuous evaluation.
