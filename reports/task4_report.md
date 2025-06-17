# Task 4 Summary – Predictive Modeling

This report summarizes the modeling pipeline developed to predict claim severity (total claim amount) for insurance policies. The model aims to support risk-based pricing and profitability forecasting at AlphaCare Insurance Solutions.

---

## Objective

To develop a predictive model that estimates the expected claim cost for policies that have previously reported a claim. This allows the business to:

- Evaluate the risk associated with new clients
- Support dynamic premium adjustment
- Reduce loss ratios by better targeting

---

## Methodology

- **Data Source**: Cleaned subset of 2014–2015 insurance records from South Africa
- **Target Variable**: `TotalClaims` (for rows where `TotalClaims > 0`)
- **Features Used**: 
  - `CustomValueEstimate` (client's car valuation)

- **Data Cleaning**:
  - Converted `CustomValueEstimate` to numeric
  - Removed rows with missing or invalid values
  - Final dataset: [Insert sample count after cleaning]

- **Model Used**: Linear Regression

- **Evaluation Metrics**:
  - Root Mean Squared Error (RMSE)
  - R² Score

---

## Results

Extracted from `metrics.json`:

- **RMSE**: [Insert value]
- **R² Score**: [Insert value]

> RMSE indicates the average prediction error in currency units.  
> R² shows how much variance in claim amounts is explained by the feature.

---

## Interpretation

- **CustomValueEstimate** is a meaningful but limited predictor of claim amount.
- The linear model offers a baseline, but future iterations should include more variables (e.g., `VehicleType`, `Province`, `SumInsured`) and advanced models (e.g., Random Forest, XGBoost).
- The current pipeline is versioned using DVC and reproducible.

---

## Next Steps

- Add more features: vehicle age, region, client demographics
- Improve model performance with tree-based methods
- Build a parallel model to predict **claim probability**
- Combine severity and probability models for **premium optimization**

---

Prepared by:  
[Your Name]  
Marketing Analytics Engineer  
B5W3 – AlphaCare Insurance Solutions
