# CREDIT SCORE CALCULATION MODULE


def calculate_payment_score(payment_history):

    return (payment_history / 100) * 210


def calculate_utilization_score(utilization):

    if utilization <= 10:

        normalized = 1

    elif utilization >= 100:

        normalized = 0

    else:

        normalized = (100 - utilization) / 90

    return normalized * 180


def calculate_age_score(credit_age):

    return min(credit_age / 10, 1) * 90


def calculate_enquiry_score(enquiries):

    return max(0, (5 - enquiries) / 5) * 60


def calculate_credit_mix_score(credit_types):

    return min(credit_types / 3, 1) * 60


# MAIN SCORE CALCULATION

def calculate_credit_score(user_data):

    payment_score = calculate_payment_score(
        user_data["payment_history"]
    )

    utilization_score = calculate_utilization_score(
        user_data["credit_utilization"]
    )

    age_score = calculate_age_score(
        user_data["credit_age"]
    )

    enquiry_score = calculate_enquiry_score(
        user_data["loan_enquiries"]
    )

    mix_score = calculate_credit_mix_score(
        user_data["credit_types"]
    )

    total_score = (
        300
        + payment_score
        + utilization_score
        + age_score
        + enquiry_score
        + mix_score
    )

    final_score = int(total_score + 0.5)

    final_score = max(300, min(900, final_score))

    return {
        "payment_score": round(payment_score, 2),
        "utilization_score": round(utilization_score, 2),
        "age_score": round(age_score, 2),
        "enquiry_score": round(enquiry_score, 2),
        "mix_score": round(mix_score, 2),
        "final_score": final_score
    }


# SCORE CLASSIFICATION

def classify_credit_score(score):

    if score >= 750:

        return "Excellent"

    elif score >= 650:

        return "Good"

    elif score >= 500:

        return "Fair"

    else:

        return "Poor"


# DISPLAY SCORE

def display_credit_score(score_details):

    print("\n" + "=" * 50)

    print("             CREDIT SCORE RESULT")

    print("=" * 50)

    print("Payment History Score:",
          score_details["payment_score"])

    print("Credit Utilization Score:",
          score_details["utilization_score"])

    print("Credit Age Score:",
          score_details["age_score"])

    print("Loan Enquiry Score:",
          score_details["enquiry_score"])

    print("Credit Mix Score:",
          score_details["mix_score"])

    print("-" * 50)

    print("FINAL CREDIT SCORE:",
          score_details["final_score"])

    print("CLASSIFICATION:",
          classify_credit_score(
              score_details["final_score"]
          ))

    print("=" * 50)