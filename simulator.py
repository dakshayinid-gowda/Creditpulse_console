# ==========================================================
# CREDITPULSE - ADVANCED WHAT-IF CREDIT SCORE SIMULATOR
# ==========================================================

from copy import deepcopy

from credit_score import (
    calculate_credit_score,
    classify_credit_score
)


# ==========================================================
# 1. DISPLAY SIMULATION HEADER
# ==========================================================

def display_simulator_header():

    print("\n")
    print("=" * 65)
    print("             CREDITPULSE - WHAT-IF SIMULATOR")
    print("=" * 65)

    print("\nExplore how improving your credit utilization")
    print("can affect your estimated credit score.")

    print("\nThis simulator uses CreditPulse's educational")
    print("weighted scoring model.")

    print("=" * 65)


# ==========================================================
# 2. GET ORIGINAL SCORE
# ==========================================================

def get_original_score(user_data):

    original_result = calculate_credit_score(user_data)

    original_score = original_result.get("final_score", 0)

    return original_result, original_score


# ==========================================================
# 3. GET NEW CREDIT UTILIZATION
# ==========================================================

def get_new_utilization(current_utilization):

    while True:

        try:

            print(
                f"\nCurrent Credit Utilization: "
                f"{current_utilization}%"
            )

            new_utilization = float(
                input("Enter your proposed utilization (0-100): ")
            )

            if new_utilization < 0 or new_utilization > 100:

                print("\nPlease enter a value between 0 and 100.")
                continue

            if new_utilization == current_utilization:

                print("\nYou entered the same utilization percentage.")
                print("Try entering a different value.")

                continue

            return new_utilization

        except ValueError:

            print("\nInvalid input. Please enter a number.")


# ==========================================================
# 4. DISPLAY SCORE COMPARISON
# ==========================================================

def display_score_comparison(
    original_score,
    simulated_score,
    original_classification,
    simulated_classification
):

    improvement = simulated_score - original_score

    print("\n")
    print("=" * 65)
    print("                 SIMULATION RESULTS")
    print("=" * 65)

    print("\n              ORIGINAL       SIMULATED")

    print(
        f"Credit Score     {original_score:<14}"
        f"{simulated_score}"
    )

    print(
        f"Classification  {original_classification:<14}"
        f"{simulated_classification}"
    )

    print("\n" + "-" * 65)

    if improvement > 0:

        print(f"\nGreat! Your estimated score increased by {improvement} points.")

    elif improvement < 0:

        print(
            f"\nYour estimated score decreased by "
            f"{abs(improvement)} points."
        )

    else:

        print("\nYour estimated credit score remains unchanged.")

    print("=" * 65)

    return improvement


# ==========================================================
# 5. DISPLAY IMPROVEMENT ANALYSIS
# ==========================================================

def display_improvement_analysis(
    old_utilization,
    new_utilization,
    improvement
):

    utilization_change = old_utilization - new_utilization

    print("\n")
    print("=" * 65)
    print("                 IMPROVEMENT ANALYSIS")
    print("=" * 65)

    print(f"\nPrevious Utilization : {old_utilization}%")
    print(f"New Utilization      : {new_utilization}%")

    print(f"Utilization Reduced  : {utilization_change:.2f}%")

    print(f"Estimated Score Gain : {improvement} points")

    print("\n--- ANALYSIS ---")

    if new_utilization <= 10:

        print("Excellent! Your simulated utilization is very low.")

    elif new_utilization <= 30:

        print("Good! Your simulated utilization is within a")
        print("commonly recommended low-utilization range.")

    elif new_utilization <= 50:

        print("Your utilization has improved, but there is")
        print("still room for improvement.")

    else:

        print("Your utilization remains relatively high.")
        print("Consider reducing outstanding credit balances.")

    if improvement > 0:

        print("\nYour proposed change improves your estimated score.")

    elif improvement < 0:

        print("\nYour proposed change reduces your estimated score.")

    else:

        print("\nYour proposed change does not affect your estimated score.")

    print("=" * 65)


# ==========================================================
# 6. RUN WHAT-IF SIMULATION
# ==========================================================

def simulate_credit_score(user_data):

    if not user_data:

        print("\nPlease enter customer details first.")
        return None

    display_simulator_header()

    # Calculate original score
    original_result, original_score = get_original_score(user_data)

    original_classification = classify_credit_score(
        original_score
    )

    # Get current utilization
    current_utilization = float(
        user_data["credit_utilization"]
    )

    # Ask for proposed utilization
    new_utilization = get_new_utilization(
        current_utilization
    )

    # Create a copy so original customer details remain unchanged
    simulated_user_data = deepcopy(user_data)

    # Modify only credit utilization
    simulated_user_data["credit_utilization"] = new_utilization

    # Calculate simulated score
    simulated_result = calculate_credit_score(
        simulated_user_data
    )

    simulated_score = simulated_result.get("final_score", 0)

    simulated_classification = classify_credit_score(
        simulated_score
    )

    # Display comparison
    improvement = display_score_comparison(
        original_score,
        simulated_score,
        original_classification,
        simulated_classification
    )

    # Display analysis
    display_improvement_analysis(
        current_utilization,
        new_utilization,
        improvement
    )

    # Return complete simulation details
    simulation_report = {

        "original_score": original_score,

        "simulated_score": simulated_score,

        "original_classification": original_classification,

        "simulated_classification": simulated_classification,

        "original_utilization": current_utilization,

        "simulated_utilization": new_utilization,

        "score_improvement": improvement,

        "simulated_user_data": simulated_user_data,

        "simulated_score_details": simulated_result

    }

    return simulation_report


# ==========================================================
# 7. DISPLAY SIMULATION SUMMARY
# ==========================================================

def display_simulation_summary(simulation_report):

    if not simulation_report:

        print("\nNo simulation results available.")
        return

    print("\n")
    print("=" * 65)
    print("                  SIMULATION SUMMARY")
    print("=" * 65)

    print(
        "\nOriginal Score:",
        simulation_report["original_score"]
    )

    print(
        "Simulated Score:",
        simulation_report["simulated_score"]
    )

    print(
        "Score Improvement:",
        simulation_report["score_improvement"]
    )

    print(
        "Original Classification:",
        simulation_report["original_classification"]
    )

    print(
        "New Classification:",
        simulation_report["simulated_classification"]
    )

    print("\nThis is an educational estimate, not an official")
    print("credit bureau score prediction.")

    print("=" * 65)