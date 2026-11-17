from user_input import collect_user_details

from simulator import simulate_credit_score


# Collect original financial information

user = collect_user_details()


# Run what-if simulation

simulate_credit_score(user)