from user_input import collect_user_details

from credit_score import calculate_credit_score

from report import generate_credit_report

from file_handler import (
    save_credit_report,
    view_saved_reports
)


# Step 1: Collect user information

user = collect_user_details()


# Step 2: Calculate credit score

result = calculate_credit_score(user)


# Step 3: Generate complete report

report = generate_credit_report(user, result)


# Step 4: Save report

save_credit_report(report)


# Step 5: Display saved reports

view_saved_reports()