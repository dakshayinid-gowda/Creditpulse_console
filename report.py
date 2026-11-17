# ==========================================================
# CREDITPULSE - ADVANCED CREDIT REPORT & RISK ANALYZER
# ==========================================================

from credit_score import classify_credit_score

from explanation import generate_explanation

from recommendations import generate_recommendations


# ==========================================================
# 1. FINANCIAL RISK ANALYSIS
# ==========================================================

def analyze_financial_risk(user_data, score_details):

    risk_factors = []

    risk_details = []

    risk_indicator_score = 0

    # ----------------------------------------------
    # PAYMENT HISTORY RISK
    # ----------------------------------------------

    payment = user_data["payment_history"]

    if payment < 50:

        severity = "Critical"

        points = 30

        reason = "Very poor payment history."

    elif payment < 70:

        severity = "High"

        points = 20

        reason = "Payment consistency is weak."

    elif payment < 90:

        severity = "Moderate"

        points = 10

        reason = "Payment history needs improvement."

    else:

        severity = None

    if severity:

        risk_factors.append("Poor payment history")

        risk_details.append({

            "factor": "Payment History",

            "severity": severity,

            "risk_points": points,

            "reason": reason

        })

        risk_indicator_score += points

    # ----------------------------------------------
    # CREDIT UTILIZATION RISK
    # ----------------------------------------------

    utilization = user_data["credit_utilization"]

    if utilization > 90:

        severity = "Critical"

        points = 25

        reason = "Credit utilization is extremely high."

    elif utilization > 70:

        severity = "High"

        points = 20

        reason = "A large portion of available credit is being used."

    elif utilization > 50:

        severity = "Moderate"

        points = 10

        reason = "Credit utilization is relatively high."

    else:

        severity = None

    if severity:

        risk_factors.append("High credit utilization")

        risk_details.append({

            "factor": "Credit Utilization",

            "severity": severity,

            "risk_points": points,

            "reason": reason

        })

        risk_indicator_score += points

    # ----------------------------------------------
    # CREDIT HISTORY AGE RISK
    # ----------------------------------------------

    age = user_data["credit_age"]

    if age < 1:

        severity = "High"

        points = 15

        reason = "Credit history is extremely limited."

    elif age < 2:

        severity = "Moderate"

        points = 10

        reason = "Credit history is relatively short."

    else:

        severity = None

    if severity:

        risk_factors.append("Limited credit history")

        risk_details.append({

            "factor": "Credit History Age",

            "severity": severity,

            "risk_points": points,

            "reason": reason

        })

        risk_indicator_score += points

    # ----------------------------------------------
    # RECENT LOAN ENQUIRY RISK
    # ----------------------------------------------

    enquiries = user_data["loan_enquiries"]

    if enquiries >= 7:

        severity = "Critical"

        points = 20

        reason = "A very high number of recent enquiries."

    elif enquiries >= 5:

        severity = "High"

        points = 15

        reason = "Several recent loan enquiries were reported."

    elif enquiries >= 3:

        severity = "Moderate"

        points = 10

        reason = "Recent credit enquiries are relatively frequent."

    else:

        severity = None

    if severity:

        risk_factors.append("Frequent recent loan enquiries")

        risk_details.append({

            "factor": "Recent Loan Enquiries",

            "severity": severity,

            "risk_points": points,

            "reason": reason

        })

        risk_indicator_score += points

    # ----------------------------------------------
    # OVERALL RISK CLASSIFICATION
    # ----------------------------------------------

    final_score = score_details["final_score"]

    if final_score >= 750:

        risk_level = "Low"

    elif final_score >= 650:

        risk_level = "Moderate"

    elif final_score >= 500:

        risk_level = "High"

    else:

        risk_level = "Very High"

    # Keep indicator within 0-100

    risk_indicator_score = min(
        risk_indicator_score,
        100
    )

    return {

        "risk_level": risk_level,

        "risk_factors": risk_factors,

        "risk_details": risk_details,

        "risk_indicator_score": risk_indicator_score

    }


# ==========================================================
# 2. DISPLAY RISK ANALYSIS
# ==========================================================

def display_risk_analysis(risk_analysis):

    print("\n" + "=" * 70)

    print("                 FINANCIAL RISK ANALYSIS")

    print("=" * 70)

    print(
        "\nOverall Risk Level:",
        risk_analysis["risk_level"]
    )

    print(
        "Risk Indicator Score:",
        risk_analysis["risk_indicator_score"],
        "/ 100"
    )

    if risk_analysis["risk_details"]:

        print("\nIDENTIFIED RISK FACTORS")

        print("-" * 70)

        for index, risk in enumerate(
            risk_analysis["risk_details"],
            start=1
        ):

            print(f"\n{index}. {risk['factor']}")

            print("Severity:", risk["severity"])

            print("Risk Points:", risk["risk_points"])

            print("Reason:", risk["reason"])

    else:

        print("\nNo risk triggers identified.")

        print("Your financial factors do not trigger")
        print("any of the current risk detection rules.")

    print("\n" + "=" * 70)


# ==========================================================
# 3. DISPLAY TOP TWO WEAKNESSES
# ==========================================================

def display_top_weaknesses(factors):

    print("\n" + "=" * 70)

    print("              TOP TWO SCORE-LOWERING FACTORS")

    print("=" * 70)

    weaknesses = [

        factor for factor in factors

        if factor["lost"] > 0

    ]

    if not weaknesses:

        print("\nExcellent!")

        print("No score-lowering factors identified.")

        return

    for index, factor in enumerate(
        weaknesses[:2],
        start=1
    ):

        print(f"\n{index}. {factor['name']}")

        print("Points Lost:", factor["lost"])

        print("Performance:", factor["percentage"], "%")

        print("Explanation:", factor["description"])

    if len(weaknesses) == 1:

        print("\nOnly one score-lowering factor was found.")


# ==========================================================
# 4. DISPLAY POSITIVE FACTORS
# ==========================================================

def display_positive_factors(factors):

    print("\n" + "=" * 70)

    print("                POSITIVE FINANCIAL FACTORS")

    print("=" * 70)

    positive_factors = [

        factor for factor in factors

        if factor["percentage"] >= 80

    ]

    if not positive_factors:

        print("\nNo factors currently meet the 80%")
        print("strong-performance threshold.")

        return

    for factor in positive_factors:

        print("\n+", factor["name"])

        print("Performance:", factor["percentage"], "%")

        print(
            "Points Earned:",
            factor["earned"],
            "/",
            factor["maximum"]
        )


# ==========================================================
# 5. COMPLETE CREDIT REPORT
# ==========================================================

def generate_credit_report(user_data, score_details):

    # Generate factor analysis

    factors = generate_explanation(
        user_data,
        score_details
    )

    # Generate recommendations

    recommendations = generate_recommendations(
        user_data,
        score_details
    )

    # Generate risk analysis

    risk_analysis = analyze_financial_risk(
        user_data,
        score_details
    )

    # Generate classification

    classification = classify_credit_score(
        score_details["final_score"]
    )

    # ----------------------------------------------
    # REPORT HEADER
    # ----------------------------------------------

    print("\n\n")

    print("=" * 70)

    print("                         CREDITPULSE")

    print("             ADVANCED CREDIT ANALYSIS REPORT")

    print("=" * 70)

    # ----------------------------------------------
    # 1. CUSTOMER PROFILE
    # ----------------------------------------------

    print("\n1. CUSTOMER FINANCIAL PROFILE")

    print("-" * 70)

    print("Customer Name         :", user_data["name"])

    print(
        "Payment History       :",
        user_data["payment_history"],
        "%"
    )

    print(
        "Credit Utilization    :",
        user_data["credit_utilization"],
        "%"
    )

    print(
        "Credit History Age    :",
        user_data["credit_age"],
        "Years"
    )

    print(
        "Recent Loan Enquiries :",
        user_data["loan_enquiries"]
    )

    print(
        "Credit Types          :",
        user_data["credit_types"]
    )

    # ----------------------------------------------
    # 2. CREDIT SCORE SUMMARY
    # ----------------------------------------------

    print("\n2. CREDIT SCORE SUMMARY")

    print("-" * 70)

    print(
        "Estimated Credit Score:",
        score_details["final_score"],
        "/ 900"
    )

    print("Classification:", classification)

    # ----------------------------------------------
    # 3. FACTOR-WISE ANALYSIS
    # ----------------------------------------------

    print("\n3. INDIVIDUAL FACTOR ANALYSIS")

    print("-" * 70)

    print(
        f"{'Factor':<27}"
        f"{'Earned':<12}"
        f"{'Maximum':<12}"
        f"{'Lost':<10}"
    )

    print("-" * 70)

    for factor in factors:

        print(
            f"{factor['name']:<27}"
            f"{factor['earned']:<12}"
            f"{factor['maximum']:<12}"
            f"{factor['lost']:<10}"
        )

    # ----------------------------------------------
    # 4. TOP WEAKNESSES
    # ----------------------------------------------

    print("\n4. WEAKNESS DETECTION")

    display_top_weaknesses(factors)

    # ----------------------------------------------
    # 5. POSITIVE FACTORS
    # ----------------------------------------------

    print("\n5. POSITIVE FINANCIAL FACTORS")

    display_positive_factors(factors)

    # ----------------------------------------------
    # 6. FINANCIAL RISK ANALYSIS
    # ----------------------------------------------

    print("\n6. FINANCIAL RISK ANALYSIS")

    display_risk_analysis(risk_analysis)

    # ----------------------------------------------
    # 7. PERSONALIZED RECOMMENDATIONS
    # ----------------------------------------------

    print("\n7. PERSONALIZED IMPROVEMENT PLAN")

    print("-" * 70)

    if recommendations:

        for index, item in enumerate(
            recommendations,
            start=1
        ):

            print(f"\nRECOMMENDATION {index}")

            print("Factor:", item["factor"])

            print("Priority:", item["priority"])

            print("Problem:", item["problem"])

            print(
                "Suggestion:",
                item["recommendation"]
            )

            print("Reason:", item["reason"])

    else:

        print("No recommendations are currently required.")

    # ----------------------------------------------
    # 8. FINAL SUMMARY
    # ----------------------------------------------

    print("\n" + "=" * 70)

    print("                    FINAL CREDIT SUMMARY")

    print("=" * 70)

    print("Customer:", user_data["name"])

    print(
        "Estimated Credit Score:",
        score_details["final_score"]
    )

    print("Credit Rating:", classification)

    print("Financial Risk:", risk_analysis["risk_level"])

    print(
        "Risk Indicator:",
        risk_analysis["risk_indicator_score"],
        "/ 100"
    )

    print("\nThank you for using CREDITPULSE!")

    # ----------------------------------------------
    # DISCLAIMER
    # ----------------------------------------------

    print("\nDISCLAIMER")

    print("-" * 70)

    print(
        "This report uses an educational weighted scoring model."
    )

    print(
        "It is not an official CIBIL or credit bureau report."
    )

    print(
        "Risk indicators are rule-based project estimates."
    )

    print(
        "The results do not guarantee loan approval."
    )

    print("=" * 70)

    # ----------------------------------------------
    # RETURN REPORT DATA
    # ----------------------------------------------

    return {

        "user_data": user_data,

        "score_details": score_details,

        "classification": classification,

        "factors": factors,

        "risk_analysis": risk_analysis,

        "recommendations": recommendations

    }