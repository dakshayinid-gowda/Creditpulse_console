from user_input import collect_user_details, display_user_details

from credit_score import (
    calculate_credit_score,
    display_credit_score
)

# Collect user information
user = collect_user_details()

# Display user information
display_user_details(user)

# Calculate credit score
result = calculate_credit_score(user)

# Display calculated score
display_credit_score(result)