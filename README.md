
#  ACIS Car Insurance Analytics Challenge

This repository contains my full submission for the **AlphaCare Insurance Solutions (ACIS)** Insurance Analytics Challenge (June 2025), focused on car insurance planning and marketing in South Africa. 

The project includes:
- Exploratory Data Analysis (EDA)
- Data Version Control (DVC)
- A/B hypothesis testing
- Predictive modeling for claim severity and premium optimization

---

## Project Objectives

AlphaCare seeks to improve its marketing and pricing strategy by:
- Discovering low-risk policyholders who can be offered lower premiums
- Understanding geographic, demographic, and vehicle-related claim patterns
- Developing risk-based pricing through machine learning

---

## Project Structure


acis-insurance-eda/
├── data/                         
│   └── MachineLearningRating_v3.txt
├── notebooks/                    
│   ├── task1\_eda_analysis.ipynb
│   ├── task3\_hypothesis\_tests.ipynb
│   └── task4\_modeling.ipynb
├── plots/                        
│   ├── loss\_ratio\_by\_province.png
│   └── ...
├── reports/                      
│   ├── task1\_summary.md
│   ├── task3\_findings.md
│   └── final\_blog\_post.md
├── .dvc/                         
├── .gitignore
├── README.md
├── requirements.txt


---

##  Tasks & Deliverables

###  Task 1: Exploratory Data Analysis (EDA)

- Data structure review, null value check
- Descriptive statistics for TotalPremium, TotalClaims, CustomValueEstimate
- Distribution analysis (histograms, boxplots)
- Bivariate relationships (Loss Ratio by Province, Gender, etc.)
- Trend analysis over 18 months
- Outlier detection
- 6 key visualizations saved in `plots/`

**Key Insight**: Gauteng shows significantly higher loss ratios than other provinces, especially among high-end vehicle types.

---

###  Task 2: Data Version Control (DVC)

- Initialized DVC
- Created local remote storage and added dataset using:
  ```bash
  dvc init
  dvc remote add -d localstorage /path/to/storage
  dvc add data/insurance.csv
  dvc push

    Dataset is fully versioned and reproducible.

📍Benefit: Enables complete auditability of results and consistent experimentation.
Task 3: A/B Hypothesis Testing

Hypotheses tested:

    H₀: No risk differences across provinces  rejected
    H₀: No risk differences between zip codes  rejected
    H₀: No margin difference between zip codes  not rejected
    H₀: No risk difference between women and men  not rejected

Tests Used:

    ANOVA
    T-tests / Welch’s test
    Chi-squared test
    Effect size measures (Cohen’s d)

Business Implication: Risk-based segmentation is valid by region, but not strongly justified by gender. Zipcode-level risk segmentation needs further refinement.
 Task 4: Predictive Modeling
1. Risk (Claim Severity) Model

    Target: TotalClaims where claims > 0

    Models used:
        Linear Regression
        Random Forest Regressor
        XGBoost Regressor

    Metrics:
        RMSE, R²

    Interpretation: SHAP used to analyze top features

2. Premium Prediction Model

Target: CalculatedPremiumPerTerm

Combined risk score using:

Premium = P(Claim) * Expected Claim + Expense + Margin

3. Binary Classifier for Claim Probability

    Target: Binary claim_occurred (TotalClaims > 0)

    Models:
        Logistic Regression
        Random Forest Classifier
        XGBoost Classifier

    Metrics:
        Accuracy, AUC, Precision, Recall, F1

Insight:

    Key risk factors include:
        Province, VehicleType, Make, CustomValueEstimate, and NumberOfVehiclesInFleet

    Older vehicles and high-value makes (BMW, Audi) predict higher claims.

 How to Run
1. Clone the Repository


2. Install Requirements

python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt

3. Setup DVC (if needed)

dvc pull       # fetch data from local or remote storage

4. Launch Notebooks

