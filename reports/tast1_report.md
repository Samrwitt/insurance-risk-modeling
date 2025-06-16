#  Task 1 Summary – Exploratory Data Analysis (EDA)

This report summarizes the key insights and findings from Task 1 of the B5W3 Insurance Risk Analytics project for AlphaCare Insurance Solutions.


---

##  Dataset Overview

- **Source**: South African insurance records (Feb 2014 – Aug 2015)
- **Rows**: [Insert row count here]
- **Columns**: 51
- **Key Features**:
  - Client Info: Gender, Citizenship, Marital Status, etc.
  - Location Info: Province, Zip Code
  - Vehicle Info: Make, Type, Year, Engine Specs
  - Policy Info: Cover Type, Premium, Claims

---

##  Key Questions Explored

- How does **risk (loss ratio)** vary by **province, gender, and vehicle type**?
- What **vehicle characteristics** are associated with high claims?
- Are there **regional or seasonal patterns** in claims or premiums?

---

##  Highlighted Insights

### 🔹 1. Loss Ratio by Province
- Provinces like **Gauteng** show consistently **higher loss ratios**, suggesting elevated regional risk.
- Western Cape and Limpopo are relatively **low-risk**.

### 🔹 2. Vehicle Type Risk
- **Panel vans and SUVs** have wide variance in claim amounts.
- Several vehicle types show extreme claim outliers (handled with log scaling).

### 🔹 3. Monthly Trends
- A notable increase in both premiums and claims toward late 2014 and mid-2015.
- Suggests potential seasonal or economic influence.

---

##  Data Quality Observations

- Some columns had **missing values** and **zero premiums**, which were flagged for cleaning.
- Outliers were found in `TotalClaims`, `CustomValueEstimate` — especially among luxury vehicles.

---

## Creative Visualizations

- **Bar chart**: Loss Ratio by Province (for pricing adjustments)
- **Boxplot**: Claims by Vehicle Type (risk segmentation)
- **Line chart**: Monthly Claim Trends (marketing cycles or seasonality)

---

## Business Interpretation

- **Geo-based premium adjustments** may be justified to address high-risk areas.
- **Vehicle type** should influence risk profiling — particularly commercial-type vehicles.
- Monthly trends can inform **campaign timing** and **resource allocation**.

---

##  Next Steps

- Integrate DVC for reproducibility (Task 2)
- Statistically test the risk hypotheses (Task 3)
- Train predictive models for claim severity and premium optimization (Task 4)

---

Prepared by:  
**[Your Name]**  
Marketing Analytics Engineer  
B5W3 – AlphaCare Insurance Solutions
