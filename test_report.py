from user_input import collect_user_details

from credit_score import calculate_credit_score

from report import generate_credit_report


# Step 1: Collect user information

user = collect_user_details()


# Step 2: Calculate credit score

result = calculate_credit_score(user)


# Step 3: Generate complete credit report

report = generate_credit_report(user, result)