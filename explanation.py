# ==========================================================
# CREDITPULSE - ADVANCED EXPLAINABLE DECISION ENGINE
# ==========================================================

from credit_score import classify_credit_score


# ==========================================================
# 1. DETERMINE FACTOR PERFORMANCE
# ==========================================================

def get_performance_status(percentage):

    if percentage >= 90:
        return "Excellent"

    elif percentage >= 80:
        return "Good"

    elif percentage >= 60:
        return "Moderate"

    else:
        return "Needs Improvement"


# ==========================================================
# 2. GENERATE DECISION TRACE
# ==========================================================

def generate_decision_trace(user_data):

    traces = []

    # Payment History Rules

    payment = user_data["payment_history"]

    if payment >= 90:

        traces.append(
            "Payment history is strong (90% or above)."
        )

    elif payment >= 70:

        traces.append(
            "Payment history is moderate (70% to below 90%)."
        )

    else:

        traces.append(
            "Payment history is weak (below 70%)."
        )

    # Credit Utilization Rules

    utilization = user_data["credit_utilization"]

    if utilization <= 10:

        traces.append(
            "Credit utilization is excellent (10% or below)."
        )

    elif utilization <= 30:

        traces.append(
            "Credit utilization is within the preferred range of this model."
        )

    elif utilization <= 70:

        traces.append(
            "Credit utilization is moderately high (above 30%)."
        )

    else:

        traces.append(
            "Credit utilization is very high (above 70%)."
        )

    # Credit Age Rules

    age = user_data["credit_age"]

    if age >= 10:

        traces.append(
            "Credit history age has reached the model's maximum scoring threshold."
        )

    elif age >= 5:

        traces.append(
            "Credit history is reasonably established (5 years or more)."
        )

    elif age >= 2:

        traces.append(
            "Credit history is relatively short (2 to below 5 years)."
        )

    else:

        traces.append(
            "Credit history is very limited (below 2 years)."
        )

    # Loan Enquiry Rules

    enquiries = user_data["loan_enquiries"]

    if enquiries == 0:

        traces.append(
            "No recent loan enquiries were reported."
        )

    elif enquiries < 3:

        traces.append(
            "Recent loan enquiry count is relatively low."
        )

    elif enquiries < 5:

        traces.append(
            "Recent loan enquiry count is moderately high."
        )

    else:

        traces.append(
            "Five or more recent loan enquiries reduce the enquiry component to zero."
        )

    # Credit Mix Rules

    credit_types = user_data["credit_types"]

    if credit_types >= 3:

        traces.append(
            "Credit mix has reached the model's maximum scoring threshold."
        )

    elif credit_types == 2:

        traces.append(
            "Two credit types are considered in the credit mix component."
        )

    elif credit_types == 1:

        traces.append(
            "Only one credit type is reported."
        )

    else:

        traces.append(
            "No credit types are reported."
        )

    return traces


# ==========================================================
# 3. GENERATE FACTOR-WISE EXPLANATION
# ==========================================================

def generate_explanation(user_data, score_details):

    factors = [

        {
            "name": "Payment History",

            "earned": score_details["payment_score"],

            "maximum": 210,

            "description":
                "Measures consistency in paying EMIs and credit bills.",

            "value": user_data["payment_history"],

            "unit": "%"
        },

        {
            "name": "Credit Utilization",

            "earned": score_details["utilization_score"],

            "maximum": 180,

            "description":
                "Measures the percentage of available credit being used.",

            "value": user_data["credit_utilization"],

            "unit": "%"
        },

        {
            "name": "Credit History Age",

            "earned": score_details["age_score"],

            "maximum": 90,

            "description":
                "Measures the age of the oldest credit account.",

            "value": user_data["credit_age"],

            "unit": " years"
        },

        {
            "name": "Recent Loan Enquiries",

            "earned": score_details["enquiry_score"],

            "maximum": 60,

            "description":
                "Measures the number of recent credit enquiries.",

            "value": user_data["loan_enquiries"],

            "unit": ""
        },

        {
            "name": "Credit Mix",

            "earned": score_details["mix_score"],

            "maximum": 60,

            "description":
                "Measures the diversity of credit types.",

            "value": user_data["credit_types"],

            "unit": ""
        }

    ]

    # Calculate factor performance

    for factor in factors:

        factor["lost"] = round(
            factor["maximum"] - factor["earned"],
            2
        )

        factor["percentage"] = round(
            (factor["earned"] / factor["maximum"]) * 100,
            2
        )

        factor["status"] = get_performance_status(
            factor["percentage"]
        )

    # Sort by highest points lost

    factors.sort(
        key=lambda factor: factor["lost"],
        reverse=True
    )

    return factors


# ==========================================================
# 4. DISPLAY FACTOR-WISE ANALYSIS
# ==========================================================

def display_factor_analysis(factors):

    print("\n" + "=" * 65)

    print("                  FACTOR-WISE ANALYSIS")

    print("=" * 65)

    for factor in factors:

        print("\nFactor:", factor["name"])

        print(
            "Input Value:",
            str(factor["value"]) + factor["unit"]
        )

        print(
            "Points Earned:",
            factor["earned"],
            "/",
            factor["maximum"]
        )

        print(
            "Performance:",
            str(factor["percentage"]) + "%"
        )

        print(
            "Status:",
            factor["status"]
        )

        print(
            "Points Lost:",
            factor["lost"]
        )

        print(
            "Explanation:",
            factor["description"]
        )

        print("-" * 65)


# ==========================================================
# 5. IDENTIFY TOP TWO WEAKNESSES
# ==========================================================

def display_top_weaknesses(factors):

    print("\n" + "=" * 65)

    print("                TOP TWO SCORE-LOWERING FACTORS")

    print("=" * 65)

    weaknesses = [

        factor for factor in factors

        if factor["lost"] > 0

    ]

    if not weaknesses:

        print("\nExcellent!")

        print("No score-lowering factors identified.")

        print("All five factors achieved their maximum points.")

        return

    for index, factor in enumerate(
        weaknesses[:2],
        start=1
    ):

        print(f"\n{index}. {factor['name']}")

        print("Points Lost:", factor["lost"])

        print("Performance:", factor["percentage"], "%")

        print("Status:", factor["status"])

        print("Reason:", factor["description"])

    if len(weaknesses) == 1:

        print("\nOnly one score-lowering factor was identified.")


# ==========================================================
# 6. IDENTIFY POSITIVE FINANCIAL FACTORS
# ==========================================================

def display_positive_factors(factors):

    print("\n" + "=" * 65)

    print("                  POSITIVE FINANCIAL FACTORS")

    print("=" * 65)

    positive_factors = [

        factor for factor in factors

        if factor["percentage"] >= 80

    ]

    if not positive_factors:

        print("\nNo factors currently meet the 80% strong-performance threshold.")

        return

    for factor in positive_factors:

        print("\n+", factor["name"])

        print(
            "Performance:",
            factor["percentage"],
            "%"
        )

        print(
            "Points Earned:",
            factor["earned"],
            "/",
            factor["maximum"]
        )


# ==========================================================
# 7. DISPLAY DECISION TRACE LOGS
# ==========================================================

def display_decision_trace(user_data):

    traces = generate_decision_trace(user_data)

    print("\n" + "=" * 65)

    print("                  DECISION TRACE LOGS")

    print("=" * 65)

    print(
        "\nThe following rules were evaluated "
        "to generate the factor scores:"
    )

    for index, trace in enumerate(
        traces,
        start=1
    ):

        print(f"\nRule {index}: {trace}")

    print("\n" + "-" * 65)

    print("Decision trace completed successfully.")


# ==========================================================
# 8. FINAL CREDIT SCORE INTERPRETATION
# ==========================================================

def display_final_interpretation(classification):

    print("\n" + "=" * 65)

    print("                  FINAL SCORE INTERPRETATION")

    print("=" * 65)

    if classification == "Excellent":

        print("\nYour financial profile performs excellently")

        print("under the CreditPulse educational scoring model.")

        print("Continue maintaining responsible credit habits.")

    elif classification == "Good":

        print("\nYour financial profile is performing well.")

        print("Some factors may still be improved.")

    elif classification == "Fair":

        print("\nYour financial profile needs improvement.")

        print("Focus on the factors losing the most points.")

    else:

        print("\nYour financial profile has significant")

        print("areas for improvement under this model.")

        print("Review the recommendations carefully.")


# ==========================================================
# 9. MAIN EXPLAINABILITY FUNCTION
# ==========================================================

def display_explanation(user_data, score_details):

    factors = generate_explanation(
        user_data,
        score_details
    )

    final_score = score_details["final_score"]

    classification = classify_credit_score(
        final_score
    )

    print("\n")

    print("=" * 65)

    print("              CREDITPULSE EXPLAINABLE ENGINE")

    print("=" * 65)

    print("\nCustomer:", user_data["name"])

    print("Estimated Credit Score:", final_score, "/ 900")

    print("Credit Classification:", classification)

    # Factor analysis

    display_factor_analysis(factors)

    # Weakness identification

    display_top_weaknesses(factors)

    # Positive factor identification

    display_positive_factors(factors)

    # Decision trace

    display_decision_trace(user_data)

    # Final interpretation

    display_final_interpretation(classification)

    print("\n" + "=" * 65)

    print("           END OF EXPLAINABLE ANALYSIS")

    print("=" * 65)