# ==========================================================
# CREDITPULSE - ADVANCED CSV FILE STORAGE SYSTEM
# ==========================================================

import csv
from pathlib import Path


# Always save the CSV inside the project folder
FILE_NAME = "credit_reports.csv"
FILE_PATH = Path(__file__).resolve().parent / FILE_NAME


# Existing CSV structure is preserved for compatibility
FIELDNAMES = [
    "Name",
    "Payment History",
    "Credit Utilization",
    "Credit Age",
    "Loan Enquiries",
    "Credit Types",
    "Estimated Score",
    "Classification",
    "Risk Level",
    "Top Weaknesses",
    "Recommendations"
]


# ==========================================================
# 1. PREPARE CUSTOMER REPORT DATA
# ==========================================================

def prepare_report_record(report):

    user = report.get("user_data", {})
    score = report.get("score_details", {})
    risk = report.get("risk_analysis", {})
    factors = report.get("factors", [])
    recommendations = report.get("recommendations", [])

    # Identify the two biggest weaknesses
    weaknesses = [
        factor for factor in factors
        if factor.get("lost", 0) > 0
    ]

    weaknesses.sort(
        key=lambda factor: factor.get("lost", 0),
        reverse=True
    )

    top_weaknesses = ", ".join(
        factor.get("name", "Unknown Factor")
        for factor in weaknesses[:2]
    )

    if not top_weaknesses:
        top_weaknesses = "No major weaknesses identified"

    # Convert recommendations into CSV-friendly text
    recommendation_text = " | ".join(
        item.get("recommendation", "")
        for item in recommendations
        if item.get("recommendation")
    )

    if not recommendation_text:
        recommendation_text = "No recommendations available"

    record = {
        "Name": user.get("name", "Unknown"),
        "Payment History": user.get("payment_history", 0),
        "Credit Utilization": user.get("credit_utilization", 0),
        "Credit Age": user.get("credit_age", 0),
        "Loan Enquiries": user.get("loan_enquiries", 0),
        "Credit Types": user.get("credit_types", 0),
        "Estimated Score": score.get("final_score", 0),
        "Classification": report.get("classification", "Unknown"),
        "Risk Level": risk.get("risk_level", "Unknown"),
        "Top Weaknesses": top_weaknesses,
        "Recommendations": recommendation_text
    }

    return record


# ==========================================================
# 2. CHECK AND PREPARE CSV FILE
# ==========================================================

def prepare_csv_file():

    try:

        if not FILE_PATH.exists() or FILE_PATH.stat().st_size == 0:

            with open(
                FILE_PATH,
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=FIELDNAMES
                )

                writer.writeheader()

            return True

        # Check whether the existing CSV has the expected columns
        with open(
            FILE_PATH,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)
            existing_fields = reader.fieldnames or []

            if existing_fields == FIELDNAMES:
                return True

            old_records = list(reader)

        # Preserve a backup before changing the CSV structure
        backup_path = FILE_PATH.with_name(
            "credit_reports_backup.csv"
        )

        if not backup_path.exists():

            FILE_PATH.replace(backup_path)

        else:

            # If a backup already exists, retain the current file
            # and create a new backup name.
            backup_path = FILE_PATH.with_name(
                "credit_reports_backup_2.csv"
            )

            FILE_PATH.replace(backup_path)

        # Create a new CSV with the required columns
        with open(
            FILE_PATH,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            writer.writeheader()

            # Preserve values from matching old columns
            for old_record in old_records:

                new_record = {
                    field: old_record.get(field, "")
                    for field in FIELDNAMES
                }

                writer.writerow(new_record)

        print("\nCSV format updated successfully.")
        print("Previous data backup:", backup_path.name)

        return True

    except (OSError, csv.Error) as error:

        print("\nCSV preparation error:", error)
        return False


# ==========================================================
# 3. SAVE CREDIT REPORT
# ==========================================================

def save_credit_report(report):

    if not isinstance(report, dict):

        print("\nInvalid credit report.")
        return False

    # Prevent duplicate saving of the same report object
    if report.get("_saved_to_csv"):

        print("\nThis report has already been saved.")
        return True

    if not prepare_csv_file():

        return False

    try:

        record = prepare_report_record(report)

        with open(
            FILE_PATH,
            "a",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            writer.writerow(record)

        # Mark this report as saved during this session
        report["_saved_to_csv"] = True

        print("\n" + "=" * 55)
        print("       CREDIT REPORT SAVED SUCCESSFULLY!")
        print("=" * 55)

        print("Customer Name :", record["Name"])
        print("Credit Score  :", record["Estimated Score"])
        print("Classification:", record["Classification"])
        print("Risk Level    :", record["Risk Level"])

        print("\nSaved File:", FILE_NAME)
        print("Location:", FILE_PATH)

        print("=" * 55)

        return True

    except (OSError, csv.Error, TypeError) as error:

        print("\nError saving credit report:", error)
        return False


# ==========================================================
# 4. VIEW SAVED CREDIT REPORTS
# ==========================================================

def view_saved_reports():

    print("\n")
    print("=" * 65)
    print("             CREDITPULSE - SAVED REPORTS")
    print("=" * 65)

    if not FILE_PATH.exists():

        print("\nNo saved reports found.")
        return

    try:

        with open(
            FILE_PATH,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            records = list(reader)

        if not records:

            print("\nNo customer records available.")
            return

        for index, record in enumerate(records, start=1):

            print("\n" + "-" * 65)
            print(f" CUSTOMER REPORT #{index}")
            print("-" * 65)

            print(f"Customer Name       : {record.get('Name', '')}")
            print(f"Payment History     : {record.get('Payment History', '')}%")
            print(f"Credit Utilization  : {record.get('Credit Utilization', '')}%")
            print(f"Credit Age          : {record.get('Credit Age', '')} years")
            print(f"Loan Enquiries      : {record.get('Loan Enquiries', '')}")
            print(f"Credit Types        : {record.get('Credit Types', '')}")

            print("\n--- CREDIT SCORE DETAILS ---")

            print(f"Estimated Score     : {record.get('Estimated Score', '')}")
            print(f"Classification      : {record.get('Classification', '')}")
            print(f"Risk Level          : {record.get('Risk Level', '')}")

            print("\n--- SCORE WEAKNESSES ---")

            print(record.get("Top Weaknesses", "None"))

            print("\n--- RECOMMENDATIONS ---")

            recommendations = record.get(
                "Recommendations", ""
            )

            for recommendation in recommendations.split(" | "):

                if recommendation:
                    print(" -", recommendation)

        print("\n" + "=" * 65)
        print("TOTAL SAVED REPORTS:", len(records))
        print("FILE:", FILE_NAME)
        print("=" * 65)

    except (OSError, csv.Error) as error:

        print("\nError reading saved reports:", error)


# ==========================================================
# 5. GET TOTAL NUMBER OF SAVED REPORTS
# ==========================================================

def get_saved_report_count():

    if not FILE_PATH.exists():
        return 0

    try:

        with open(
            FILE_PATH,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            return sum(1 for _ in reader)

    except (OSError, csv.Error):

        return 0