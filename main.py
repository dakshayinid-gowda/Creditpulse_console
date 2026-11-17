# ==========================================================
# CREDITPULSE
# Explainable Credit Score Estimation Engine
# Main Application
# ==========================================================

from user_input import (
    collect_user_details,
    display_user_details
)

from credit_score import (
    calculate_credit_score,
    classify_credit_score
)

from explanation import (
    display_explanation,
    display_decision_trace
)

from report import (
    analyze_financial_risk,
    display_risk_analysis,
    generate_credit_report
)

from recommendations import (
    generate_recommendations,
    display_recommendations
)

from simulator import (
    simulate_credit_score,
    display_simulation_summary
)

from file_handler import (
    save_credit_report,
    view_saved_reports,
    get_saved_report_count
)


# ==========================================================
# GLOBAL APPLICATION DATA
# ==========================================================

user_data = None
score_details = None
credit_report = None
simulation_report = None


# ==========================================================
# 1. DISPLAY APPLICATION HEADER
# ==========================================================

def display_header():

    print("\n")
    print("=" * 65)
    print("                  CREDITPULSE")
    print("       EXPLAINABLE CREDIT SCORE ENGINE")
    print("=" * 65)

    print("Understand your credit. Identify risks. Improve your score.")

    print("=" * 65)


# ==========================================================
# 2. DISPLAY MAIN MENU
# ==========================================================

def display_menu():

    print("\n")
    print("=" * 65)
    print("                     MAIN MENU")
    print("=" * 65)

    print("1.  Enter / Update Customer Details")
    print("2.  Calculate Credit Score")
    print("3.  View Credit Classification")
    print("4.  Explain Credit Score")
    print("5.  Analyze Financial Risk")
    print("6.  View Personalized Recommendations")
    print("7.  What-If Credit Score Simulator")
    print("8.  Generate Complete Credit Report")
    print("9.  Save Credit Report")
    print("10. View Saved Reports")
    print("11. View Customer Profile")
    print("12. View Decision Trace")
    print("13. View Simulation Summary")
    print("14. View Application Statistics")
    print("15. Exit")

    print("=" * 65)


# ==========================================================
# 3. CHECK CUSTOMER DATA
# ==========================================================

def check_customer():

    if user_data is None:

        print("\nPlease enter customer details first.")
        return False

    return True


# ==========================================================
# 4. CHECK CREDIT SCORE
# ==========================================================

def check_score():

    global score_details

    if not check_customer():
        return False

    if score_details is None:

        score_details = calculate_credit_score(user_data)

    return True


# ==========================================================
# 5. ENTER CUSTOMER DETAILS
# ==========================================================

def option_customer_details():

    global user_data
    global score_details
    global credit_report
    global simulation_report

    print("\n--- CUSTOMER REGISTRATION ---")

    new_user_data = collect_user_details()

    if new_user_data:

        user_data = new_user_data

        # Reset old results after updating customer details
        score_details = None
        credit_report = None
        simulation_report = None

        print("\nCustomer information updated successfully!")

    else:

        print("\nCustomer information was not updated.")


# ==========================================================
# 6. CALCULATE CREDIT SCORE
# ==========================================================

def option_calculate_score():

    global score_details

    if not check_customer():
        return

    score_details = calculate_credit_score(user_data)

    score = score_details.get("final_score", 0)

    classification = classify_credit_score(score)

    print("\n")
    print("=" * 65)
    print("                 CREDIT SCORE RESULT")
    print("=" * 65)

    print("\nCustomer Name :", user_data["name"])
    print("Estimated Score:", score)
    print("Classification :", classification)

    print("=" * 65)


# ==========================================================
# 7. VIEW CLASSIFICATION
# ==========================================================

def option_classification():

    if not check_score():
        return

    score = score_details.get("final_score", 0)

    classification = classify_credit_score(score)

    print("\n")
    print("=" * 60)
    print("               CREDIT CLASSIFICATION")
    print("=" * 60)

    print("Customer Name :", user_data["name"])
    print("Credit Score  :", score)
    print("Category      :", classification)

    if classification == "Excellent":

        print("\nExcellent credit profile!")

    elif classification == "Good":

        print("\nYour credit profile is good.")

    elif classification == "Fair":

        print("\nYour credit profile needs improvement.")

    else:

        print("\nYour credit profile requires attention.")

    print("=" * 60)


# ==========================================================
# 8. EXPLAIN CREDIT SCORE
# ==========================================================

def option_explanation():

    if not check_score():
        return

    display_explanation(user_data, score_details)


# ==========================================================
# 9. ANALYZE FINANCIAL RISK
# ==========================================================

def option_risk_analysis():

    if not check_score():
        return

    risk_analysis = analyze_financial_risk(
        user_data,
        score_details
    )

    display_risk_analysis(risk_analysis)


# ==========================================================
# 10. PERSONALIZED RECOMMENDATIONS
# ==========================================================

def option_recommendations():

    if not check_score():
        return

    recommendations = generate_recommendations(
        user_data,
        score_details
    )

    display_recommendations(recommendations)


# ==========================================================
# 11. WHAT-IF SIMULATOR
# ==========================================================

def option_simulator():

    global simulation_report

    if not check_score():
        return

    simulation_report = simulate_credit_score(user_data)


# ==========================================================
# 12. GENERATE COMPLETE CREDIT REPORT
# ==========================================================

def option_complete_report():

    global credit_report

    if not check_score():
        return

    credit_report = generate_credit_report(
        user_data,
        score_details
    )


# ==========================================================
# 13. SAVE CREDIT REPORT
# ==========================================================

def option_save_report():

    if credit_report is None:

        print("\nPlease generate a complete report first.")
        return

    save_credit_report(credit_report)


# ==========================================================
# 14. VIEW SAVED REPORTS
# ==========================================================

def option_view_reports():

    view_saved_reports()


# ==========================================================
# 15. VIEW CUSTOMER PROFILE
# ==========================================================

def option_view_profile():

    if not check_customer():
        return

    display_user_details(user_data)


# ==========================================================
# 16. VIEW DECISION TRACE
# ==========================================================

def option_decision_trace():

    if not check_score():
        return

    display_decision_trace(user_data)


# ==========================================================
# 17. VIEW SIMULATION SUMMARY
# ==========================================================

def option_simulation_summary():

    if simulation_report is None:

        print("\nNo simulation has been performed yet.")
        print("Please use Option 7 first.")

        return

    display_simulation_summary(simulation_report)


# ==========================================================
# 18. APPLICATION STATISTICS
# ==========================================================

def option_statistics():

    total_reports = get_saved_report_count()

    print("\n")
    print("=" * 60)
    print("              CREDITPULSE STATISTICS")
    print("=" * 60)

    print("Saved Credit Reports :", total_reports)

    if user_data is not None:

        print("Current Customer     :", user_data["name"])

    else:

        print("Current Customer     : None")

    if score_details is not None:

        print(
            "Current Estimated Score:",
            score_details.get("final_score", 0)
        )

    else:

        print("Current Estimated Score: Not Calculated")

    print("=" * 60)


# ==========================================================
# 19. EXIT APPLICATION
# ==========================================================

def option_exit():

    print("\n")
    print("=" * 60)
    print("       THANK YOU FOR USING CREDITPULSE!")
    print("=" * 60)

    print("Understand your credit. Make informed decisions.")

    print("\nDisclaimer:")
    print("CreditPulse provides educational credit score estimates.")
    print("It does not generate official credit bureau scores.")

    print("=" * 60)


# ==========================================================
# 20. MAIN APPLICATION LOOP
# ==========================================================

def main():

    display_header()

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-15): ").strip()

        try:

            if choice == "1":

                option_customer_details()

            elif choice == "2":

                option_calculate_score()

            elif choice == "3":

                option_classification()

            elif choice == "4":

                option_explanation()

            elif choice == "5":

                option_risk_analysis()

            elif choice == "6":

                option_recommendations()

            elif choice == "7":

                option_simulator()

            elif choice == "8":

                option_complete_report()

            elif choice == "9":

                option_save_report()

            elif choice == "10":

                option_view_reports()

            elif choice == "11":

                option_view_profile()

            elif choice == "12":

                option_decision_trace()

            elif choice == "13":

                option_simulation_summary()

            elif choice == "14":

                option_statistics()

            elif choice == "15":

                option_exit()
                break

            else:

                print("\nInvalid choice. Please select 1-15.")

        except (ValueError, KeyError, TypeError) as error:

            print("\nAn application error occurred:", error)
            print("Please check the relevant module and try again.")

        except Exception as error:

            print("\nUnexpected error:", error)
            print("Please share this error for debugging.")

        input("\nPress Enter to return to the main menu...")


# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    main()