from user_input import collect_user_details

from credit_score import calculate_credit_score

from explanation import display_explanation


# Collect financial information

user = collect_user_details()


# Calculate credit score

result = calculate_credit_score(user)


# Generate explanation

display_explanation(user, result)