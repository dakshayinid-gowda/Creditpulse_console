# CreditPulse – Explainable Credit Score Estimation Engine

**CreditPulse** is a Python-based, menu-driven console application that estimates a customer's credit score using a weighted scoring model. It helps users understand their credit profile, identify financial weaknesses, analyze risk, and explore ways to improve their estimated credit score.

The application focuses on explainable scoring, meaning users can understand how each financial factor contributes to their final score.

---

## 1. Project Overview

Many young earners and first-time borrowers struggle to understand their credit profiles and why their loan applications may be rejected.

CreditPulse addresses this problem by providing an educational credit score estimation system that:

- Calculates an estimated credit score between 300 and 900.
- Evaluates important financial factors.
- Explains the reasons behind the calculated score.
- Identifies the two biggest factors reducing the score.
- Provides personalized financial recommendations.
- Simulates how changes in credit utilization affect the estimated score.
- Generates and saves credit reports.

---

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| CSV | Saving customer credit reports |
| Python Modules | Modular application development |
| PowerShell / Terminal | Running the application |

**Project Type:** Menu-Driven Console Application

**Database:** Not required

**GUI:** Not required

**Web Application:** Not required

---

## 3. Key Features

### 1. Customer Registration
Collects customer financial information, including:
- Customer name
- On-time payment percentage
- Credit utilization percentage
- Age of oldest credit account
- Recent loan enquiries
- Number of different credit types

### 2. Credit Score Calculation
Calculates an estimated credit score between 300 and 900 using a fixed weighted scoring model.

### 3. Credit Classification
Classifies customers into four categories:

| Score Range | Classification |
|---|---|
| 750–900 | Excellent |
| 650–749 | Good |
| 500–649 | Fair |
| 300–499 | Poor |

### 4. Explainable Score Analysis
Explains how each financial factor contributes to the final credit score.

### 5. Financial Risk Analysis
Identifies financial weaknesses and evaluates the customer's estimated risk level.

### 6. Personalized Recommendations
Provides suggestions to improve weak financial factors, such as payment history, credit utilization, and credit mix.

### 7. What-If Credit Score Simulator
Allows users to enter a proposed credit utilization percentage and compare the original and simulated scores.

### 8. Complete Credit Report
Generates a detailed report containing customer information, score breakdown, classification, weaknesses, risk analysis, and recommendations.

### 9. CSV Report Storage
Saves generated credit reports in a CSV file for future reference.

### 10. Saved Report Viewer
Displays previously saved customer credit reports.

---

## 4. Credit Scoring Methodology

CreditPulse uses a weighted scoring model with a maximum score of 900.

| Factor | Maximum Points |
|---|---:|
| Base Score | 300 |
| Payment History | 210 |
| Credit Utilization | 180 |
| Credit Age | 90 |
| Recent Loan Enquiries | 60 |
| Credit Mix | 60 |
| **Total** | **900** |

### Scoring Formulas

**Payment History**

Payment Score = (On-Time Payment Percentage / 100) × 210

**Credit Utilization**

- Utilization up to 10%: 180 points.
- Utilization from above 10% to below 100%: points decrease linearly.
- Utilization at 100%: 0 points.

Formula for utilization above 10%:

Utilization Score = ((100 − Utilization) / 90) × 180

**Credit Age**

Credit Age Score = min(Credit Age / 10, 1) × 90

**Recent Loan Enquiries**

Enquiry Score = max(0, (5 − Number of Enquiries) / 5) × 60

**Credit Mix**

Credit Mix Score = min(Number of Credit Types / 3, 1) × 60

**Final Credit Score**

Final Score = Base Score + All Factor Scores

The final score is rounded to the nearest whole number.

---

## 5. Project Structure

```text
CreditPulse_Console/
│
├── main.py
│
├── user_input.py
├── credit_score.py
├── explanation.py
├── recommendations.py
├── simulator.py
├── report.py
├── file_handler.py
│
├── credit_reports.csv
│
├── test_user_input.py
├── test_credit_score.py
├── test_explanation.py
├── test_recommendations.py
├── test_simulator.py
├── test_report.py
├── test_file_handler.py
│
└── README.md
```

---

## 6. Installation and Setup

### Prerequisites

- Python 3.10 or above recommended.
- Visual Studio Code or another Python editor.
- Windows PowerShell or terminal.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project

```bash
cd CreditPulse_Console
```

### Step 3: Run the Application

```bash
python main.py
```

No external Python packages are required if the project uses only Python's standard library.

---

## 7. Application Menu

The application provides the following menu options:

| Option | Function |
|---|---|
| 1 | Enter / Update Customer Details |
| 2 | Calculate Credit Score |
| 3 | View Credit Classification |
| 4 | Explain Credit Score |
| 5 | Analyze Financial Risk |
| 6 | View Personalized Recommendations |
| 7 | What-If Credit Score Simulator |
| 8 | Generate Complete Credit Report |
| 9 | Save Credit Report |
| 10 | View Saved Reports |
| 11 | View Customer Profile |
| 12 | View Decision Trace |
| 13 | View Simulation Summary |
| 14 | View Application Statistics |
| 15 | Exit |

---

## 8. Sample Test Case

**Customer Details**

| Parameter | Value |
|---|---:|
| Customer Name | Rahul |
| Payment History | 65% |
| Credit Utilization | 80% |
| Credit Age | 1 year |
| Recent Loan Enquiries | 6 |
| Credit Types | 1 |

**Expected Result**

- Estimated Credit Score: 506
- Credit Classification: Fair

**What-If Simulation**

If credit utilization is reduced from 80% to 20%:

- Original Score: 506
- Simulated Score: 626
- Estimated Improvement: 120 points

---

## 9. Advantages

- Simple and beginner-friendly console interface.
- Explainable and transparent scoring methodology.
- Modular Python architecture.
- Personalized recommendations.
- What-if credit score simulation.
- CSV-based report storage.
- No database or external service dependency.

---

## 10. Future Enhancements

Possible future improvements include:

- 30-day personalized credit improvement planner.
- Month-by-month credit score tracking.
- Multiple customer profile management.
- Advanced financial health analysis.
- Exporting reports as PDF.
- Additional what-if simulation scenarios.
- More detailed decision trace explanations.

---

## 11. Limitations and Disclaimer

CreditPulse is an educational credit score estimation project.

Its scoring formula is a simplified, self-designed weighted model. It does not represent the official scoring methodology of CIBIL, Experian, Equifax, TransUnion, or any other credit bureau.

Actual credit scores may differ depending on credit bureau data, lender policies, and proprietary scoring methods.

The recommendations are educational suggestions and should not be considered professional financial advice.

---

## 12. Author

**Project Name:** CreditPulse – Explainable Credit Score Estimation Engine

**Domain:** Banking and FinTech

**Programming Language:** Python

**Project Type:** Menu-Driven Console Application

---

### Made with Python
**CreditPulse – Understand Your Credit. Improve Your Financial Future.**