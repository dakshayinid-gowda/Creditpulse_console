# ==========================================================
# CREDITPULSE - INTELLIGENT RECOMMENDATION ENGINE
# ==========================================================

from explanation import generate_explanation


# ==========================================================
# 1. PRIORITY ORDER
# ==========================================================

PRIORITY_ORDER = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4
}


# ==========================================================
# 2. CREATE RECOMMENDATION
# ==========================================================

def create_recommendation(
    factor,
    priority,
    problem,
    recommendation,
    reason,
    action_steps,
    points_lost=0
):

    return {

        "factor": factor,

        "priority": priority,

        "problem": problem,

        "recommendation": recommendation,

        "reason": reason,

        "action_steps": action_steps,

        "points_lost": points_lost

    }


# ==========================================================
# 3. GENERATE PERSONALIZED RECOMMENDATIONS
# ==========================================================

def generate_recommendations(user_data, score_details):

    recommendations = []

    # Obtain factor-wise scoring analysis

    factors = generate_explanation(
        user_data,
        score_details
    )

    factor_losses = {

        factor["name"]: factor["lost"]

        for factor in factors

    }

    # ------------------------------------------------------
    # PAYMENT HISTORY
    # ------------------------------------------------------

    payment = user_data["payment_history"]

    if payment < 50:

        recommendations.append(
            create_recommendation(

                "Payment History",

                "Critical",

                "Very poor on-time payment percentage.",

                "Prioritize overdue payments and pay future EMIs "
                "and credit card bills before their due dates.",

                "Payment history carries the highest weight "
                "in the CreditPulse scoring model.",

                [
                    "Review overdue payments.",
                    "Create a monthly bill payment schedule.",
                    "Set reminders before payment due dates.",
                    "Consider automatic payments where appropriate."
                ],

                factor_losses.get("Payment History", 0)

            )
        )

    elif payment < 70:

        recommendations.append(
            create_recommendation(

                "Payment History",

                "Critical",

                "On-time payment percentage is below 70%.",

                "Improve payment consistency and avoid missing "
                "future payment deadlines.",

                "Payment history contributes up to 210 points "
                "in the educational scoring model.",

                [
                    "Identify missed or delayed payments.",
                    "Pay outstanding dues where possible.",
                    "Set payment reminders.",
                    "Maintain a consistent payment schedule."
                ],

                factor_losses.get("Payment History", 0)

            )
        )

    elif payment < 90:

        recommendations.append(
            create_recommendation(

                "Payment History",

                "High",

                "Payment consistency needs improvement.",

                "Aim to make all eligible payments on time.",

                "A stronger payment history earns more points "
                "in the CreditPulse model.",

                [
                    "Track all payment due dates.",
                    "Maintain sufficient funds for scheduled payments.",
                    "Avoid unnecessary payment delays."
                ],

                factor_losses.get("Payment History", 0)

            )
        )

    # ------------------------------------------------------
    # CREDIT UTILIZATION
    # ------------------------------------------------------

    utilization = user_data["credit_utilization"]

    if utilization > 90:

        recommendations.append(
            create_recommendation(

                "Credit Utilization",

                "Critical",

                "Credit utilization is extremely high.",

                "Work towards reducing outstanding credit balances.",

                "Very high utilization significantly reduces "
                "the utilization component of the model.",

                [
                    "Review outstanding credit card balances.",
                    "Create a repayment budget.",
                    "Reduce unnecessary credit spending.",
                    "Avoid using most of your available credit."
                ],

                factor_losses.get("Credit Utilization", 0)

            )
        )

    elif utilization > 70:

        recommendations.append(
            create_recommendation(

                "Credit Utilization",

                "Critical",

                "A large percentage of available credit is being used.",

                "Gradually reduce outstanding balances and "
                "avoid unnecessary credit usage.",

                "Credit utilization contributes up to 180 points "
                "in the scoring model.",

                [
                    "Review current outstanding balances.",
                    "Plan regular repayments.",
                    "Avoid unnecessary credit purchases."
                ],

                factor_losses.get("Credit Utilization", 0)

            )
        )

    elif utilization > 30:

        recommendations.append(
            create_recommendation(

                "Credit Utilization",

                "High",

                "Credit utilization is above 30%.",

                "Work towards reducing your credit utilization.",

                "Lower utilization earns more points "
                "under the CreditPulse model.",

                [
                    "Monitor monthly credit usage.",
                    "Pay outstanding balances regularly.",
                    "Avoid unnecessary credit spending."
                ],

                factor_losses.get("Credit Utilization", 0)

            )
        )

    # ------------------------------------------------------
    # CREDIT HISTORY AGE
    # ------------------------------------------------------

    age = user_data["credit_age"]

    if age < 2:

        recommendations.append(
            create_recommendation(

                "Credit History Age",

                "Medium",

                "Your credit history is relatively short.",

                "Maintain existing credit accounts responsibly.",

                "The model awards more points as credit history age "
                "increases, up to its 10-year scoring threshold.",

                [
                    "Maintain existing accounts responsibly.",
                    "Avoid unnecessary account closures.",
                    "Build a consistent repayment history over time."
                ],

                factor_losses.get("Credit History Age", 0)

            )
        )

    elif age < 5:

        recommendations.append(
            create_recommendation(

                "Credit History Age",

                "Low",

                "Your credit history has room to mature.",

                "Continue maintaining your existing credit accounts.",

                "Credit history age contributes up to 90 points "
                "in the educational model.",

                [
                    "Maintain responsible credit habits.",
                    "Avoid unnecessary account closures.",
                    "Allow your existing credit history to mature."
                ],

                factor_losses.get("Credit History Age", 0)

            )
        )

    # ------------------------------------------------------
    # RECENT LOAN ENQUIRIES
    # ------------------------------------------------------

    enquiries = user_data["loan_enquiries"]

    if enquiries >= 7:

        recommendations.append(
            create_recommendation(

                "Recent Loan Enquiries",

                "Critical",

                "A very high number of recent loan enquiries.",

                "Avoid unnecessary credit applications.",

                "Frequent enquiries reduce the enquiry component "
                "of the CreditPulse scoring model.",

                [
                    "Review recent credit applications.",
                    "Apply for credit only when necessary.",
                    "Compare available loan options before applying."
                ],

                factor_losses.get("Recent Loan Enquiries", 0)

            )
        )

    elif enquiries >= 5:

        recommendations.append(
            create_recommendation(

                "Recent Loan Enquiries",

                "High",

                "Several recent loan enquiries were reported.",

                "Reduce unnecessary credit applications.",

                "The model awards zero enquiry points "
                "when enquiries reach five or more.",

                [
                    "Review recent loan applications.",
                    "Avoid unnecessary applications.",
                    "Apply for new credit only when required."
                ],

                factor_losses.get("Recent Loan Enquiries", 0)

            )
        )

    elif enquiries >= 3:

        recommendations.append(
            create_recommendation(

                "Recent Loan Enquiries",

                "Medium",

                "Recent loan enquiries are relatively frequent.",

                "Be selective when applying for new credit.",

                "Fewer recent enquiries receive a better score "
                "under the educational scoring model.",

                [
                    "Check whether new credit is necessary.",
                    "Compare loan options before applying.",
                    "Avoid repeated applications."
                ],

                factor_losses.get("Recent Loan Enquiries", 0)

            )
        )

    # ------------------------------------------------------
    # CREDIT MIX
    # ------------------------------------------------------

    credit_types = user_data["credit_types"]

    if credit_types == 0:

        recommendations.append(
            create_recommendation(

                "Credit Mix",

                "Low",

                "No credit types have been reported.",

                "Build a responsible credit history only if "
                "credit is genuinely needed.",

                "The educational model awards more points "
                "for a wider range of reported credit types.",

                [
                    "Understand your existing financial profile.",
                    "Use credit responsibly if required.",
                    "Do not borrow unnecessarily to improve this factor."
                ],

                factor_losses.get("Credit Mix", 0)

            )
        )

    elif credit_types == 1:

        recommendations.append(
            create_recommendation(

                "Credit Mix",

                "Low",

                "Limited credit diversity is reported.",

                "Continue managing your existing credit responsibly.",

                "The model assigns more points to a wider credit mix, "
                "but taking unnecessary loans is not recommended.",

                [
                    "Maintain existing accounts responsibly.",
                    "Understand different credit products.",
                    "Avoid unnecessary borrowing."
                ],

                factor_losses.get("Credit Mix", 0)

            )
        )

    # ------------------------------------------------------
    # 4. SORT BY PRIORITY AND POINTS LOST
    # ------------------------------------------------------

    recommendations.sort(

        key=lambda item: (

            PRIORITY_ORDER[item["priority"]],

            -item["points_lost"]

        )

    )

    # ------------------------------------------------------
    # 5. GENERAL RECOMMENDATION
    # ------------------------------------------------------

    if not recommendations:

        recommendations.append(

            create_recommendation(

                "Overall Credit Profile",

                "Low",

                "No major weaknesses identified.",

                "Continue maintaining responsible financial habits.",

                "Your financial factors are performing well "
                "under the CreditPulse educational model.",

                [
                    "Continue paying bills on time.",
                    "Monitor credit utilization.",
                    "Review your financial profile periodically."
                ],

                0

            )

        )

    return recommendations


# ==========================================================
# 6. DISPLAY RECOMMENDATIONS
# ==========================================================

def display_recommendations(user_data, score_details):

    recommendations = generate_recommendations(
        user_data,
        score_details
    )

    print("\n" + "=" * 70)

    print("           CREDITPULSE PERSONALIZED IMPROVEMENT PLAN")

    print("=" * 70)

    print("\nCustomer:", user_data["name"])

    print(
        "Estimated Credit Score:",
        score_details["final_score"],
        "/ 900"
    )

    print(
        "Total Recommendations:",
        len(recommendations)
    )

    # ------------------------------------------------------
    # DISPLAY INDIVIDUAL RECOMMENDATIONS
    # ------------------------------------------------------

    for index, item in enumerate(
        recommendations,
        start=1
    ):

        print("\n" + "-" * 70)

        print(f"RECOMMENDATION {index}")

        print("-" * 70)

        print("Factor       :", item["factor"])

        print("Priority     :", item["priority"])

        print("Problem      :", item["problem"])

        print(
            "Points Lost  :",
            item["points_lost"]
        )

        print(
            "Suggestion   :",
            item["recommendation"]
        )

        print(
            "Reason       :",
            item["reason"]
        )

        print("\nACTION STEPS:")

        for step_number, step in enumerate(
            item["action_steps"],
            start=1
        ):

            print(f"  {step_number}. {step}")

    # ------------------------------------------------------
    # PRIORITY SUMMARY
    # ------------------------------------------------------

    critical = sum(
        1 for item in recommendations
        if item["priority"] == "Critical"
    )

    high = sum(
        1 for item in recommendations
        if item["priority"] == "High"
    )

    medium = sum(
        1 for item in recommendations
        if item["priority"] == "Medium"
    )

    low = sum(
        1 for item in recommendations
        if item["priority"] == "Low"
    )

    print("\n" + "=" * 70)

    print("                  PRIORITY SUMMARY")

    print("=" * 70)

    print("Critical Recommendations:", critical)

    print("High Recommendations    :", high)

    print("Medium Recommendations  :", medium)

    print("Low Recommendations     :", low)

    # ------------------------------------------------------
    # FINAL ACTION PLAN
    # ------------------------------------------------------

    print("\n" + "=" * 70)

    print("                 YOUR CREDIT ACTION PLAN")

    print("=" * 70)

    if critical > 0:

        print("\n1. Address critical financial weaknesses first.")

        print("2. Focus on payment consistency and high utilization.")

        print("3. Follow the action steps provided above.")

    elif high > 0:

        print("\n1. Focus on high-priority recommendations.")

        print("2. Improve payment and credit usage habits.")

    elif medium > 0:

        print("\n1. Work on moderate improvement areas.")

        print("2. Maintain responsible credit habits.")

    else:

        print("\nYour financial profile is performing well.")

        print("Continue maintaining responsible credit habits.")

    print("\nNOTE:")

    print("These suggestions are educational recommendations.")

    print("They do not guarantee a particular credit score.")

    print("=" * 70)

    return recommendations