from user_input import collect_user_details

from credit_score import calculate_credit_score

from recommendations import display_recommendations


# Collect user information

user = collect_user_details()


# Calculate credit score

result = calculate_credit_score(user)


# Generate personalized recommendations

display_recommendations(user, result)