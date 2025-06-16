# Task 3 Summary – Hypothesis Testing

This report summarizes the hypothesis testing performed on risk and margin differences across different demographic and geographic insurance policy segments.

---

## Hypotheses and Tests Performed

| Hypothesis ID | Null Hypothesis (H₀) | Metric Used | Test Type | Result |
|---------------|-----------------------|-------------|-----------|--------|
| H₀₁ | No risk difference across provinces | Claim Frequency | ANOVA | [pending] |
| H₀₂ | No claim severity difference across zip codes | Claim Severity | ANOVA | Rejected |
| H₀₃ | No margin difference across zip codes | Margin | ANOVA | Failed to Reject |
| H₀₄ | No risk difference between genders | Claim Frequency | Chi-squared | Rejected |

---

## Detailed Results

### H₀₂: Claim Severity vs Zip Codes
- F-statistic: 2.562  
- p-value: < 0.00001  
Result: Rejected  
Interpretation: There are statistically significant differences in claim severity across zip codes. Certain areas consistently show higher or lower claims, which suggests room for location-based premium adjustment.

---

### H₀₃: Margin vs Zip Codes
- F-statistic: 0.910  
- p-value: 0.97031  
Result: Failed to Reject  
Interpretation: There's no strong evidence that profit margin significantly differs between zip codes. Margin may be more influenced by other factors (e.g., vehicle type, client profile).

---

### H₀₄: Gender vs Claim Frequency
- Chi2 statistic: 7.256  
- p-value: 0.02657  
Result: Rejected  
Interpretation: Statistically significant difference exists between men and women in how often they file claims. Gender may influence risk and should be analyzed further for fairness and compliance.

---

## Business Implications

- Location-Based Pricing: Zip codes strongly influence claim severity. Consider refining premium strategy by regional risk clusters.
- Gender-Based Risk: A measurable difference exists, but fairness policies and regulatory frameworks must be considered before acting on it.
- No Margin Difference by Zip: Profitability is uniform across zip codes, meaning margin-based targeting may be less impactful.

---

## Next Steps

- Combine these findings with machine learning models (Task 4)
- Use segmentation logic to build features for premium prediction
- Use results to inform premium strategy and marketing targets

---

Prepared by:  
[Your Name]  
Marketing Analytics Engineer  
B5W3 – AlphaCare Insurance Solutions
