# ==========================================================
# CREDITPULSE - SMART CUSTOMER INPUT MODULE
# ==========================================================

# Required customer information:
# name
# payment_history
# credit_utilization
# credit_age
# loan_enquiries
# credit_types


# ==========================================================
# 1. INPUT CUSTOMER NAME
# ==========================================================

def get_customer_name():

    while True:

        name = input("\nEnter Customer Name: ").strip()

        if not name:

            print("Name cannot be empty.")
            continue

        if not any(character.isalpha() for character in name):

            print("Please enter a valid name.")
            continue

        if len(name) > 60:

            print("Name should not exceed 60 characters.")
            continue

        return name


# ==========================================================
# 2. INPUT PERCENTAGE VALUES
# ==========================================================

def get_percentage(prompt):

    while True:

        try:

            value = float(input(prompt))

            if value < 0 or value > 100:

                print("Enter a percentage between 0 and 100.")
                continue

            return value

        except ValueError:

            print("Invalid input. Please enter a number.")


# ==========================================================
# 3. INPUT CREDIT AGE
# ==========================================================

def get_credit_age():

    while True:

        try:

            age = float(
                input("Enter Age of Oldest Credit Account (years): ")
            )

            if age < 0:

                print("Credit age cannot be negative.")
                continue

            if age > 100:

                print("Please enter a realistic credit age.")
                continue

            return age

        except ValueError:

            print("Invalid input. Please enter a number.")


# ==========================================================
# 4. INPUT NON-NEGATIVE INTEGER
# ==========================================================

def get_non_negative_integer(prompt, maximum=1000):

    while True:

        value = input(prompt).strip()

        try:

            number = int(value)

            if number < 0:

                print("Value cannot be negative.")
                continue

            if number > maximum:

                print(f"Please enter a value not greater than {maximum}.")
                continue

            return number

        except ValueError:

            print("Invalid input. Please enter a whole number.")


# ==========================================================
# 5. COLLECT CUSTOMER FINANCIAL DETAILS
# ==========================================================

def get_user_input():

    print("\n")
    print("=" * 60)
    print("          CREDITPULSE - CUSTOMER REGISTRATION")
    print("=" * 60)

    print("\nPlease enter the customer's financial details.")

    user_data = {}

    user_data["name"] = get_customer_name()

    print("\n--- PAYMENT INFORMATION ---")

    user_data["payment_history"] = get_percentage(
        "Enter On-Time Payment Percentage (0-100): "
    )

    print("\n--- CREDIT UTILIZATION ---")

    user_data["credit_utilization"] = get_percentage(
        "Enter Credit Utilization Percentage (0-100): "
    )

    print("\n--- CREDIT HISTORY ---")

    user_data["credit_age"] = get_credit_age()

    print("\n--- LOAN INFORMATION ---")

    user_data["loan_enquiries"] = get_non_negative_integer(
        "Enter Number of Recent Loan Enquiries: "
    )

    print("\n--- CREDIT MIX ---")

    user_data["credit_types"] = get_non_negative_integer(
        "Enter Number of Different Credit Types: ",
        maximum=20
    )

    print("\nCustomer information collected successfully!")

    display_user_data(user_data)

    return user_data


# ==========================================================
# 6. VALIDATE CUSTOMER DATA
# ==========================================================

def validate_user_data(user_data):

    required_fields = [
        "name",
        "payment_history",
        "credit_utilization",
        "credit_age",
        "loan_enquiries",
        "credit_types"
    ]

    if not isinstance(user_data, dict):

        return False

    for field in required_fields:

        if field not in user_data:

            return False

    if not str(user_data["name"]).strip():

        return False

    try:

        payment = float(user_data["payment_history"])
        utilization = float(user_data["credit_utilization"])
        age = float(user_data["credit_age"])

        enquiries = int(user_data["loan_enquiries"])
        credit_types = int(user_data["credit_types"])

    except (ValueError, TypeError):

        return False

    if not 0 <= payment <= 100:
        return False

    if not 0 <= utilization <= 100:
        return False

    if not 0 <= age <= 100:
        return False

    if enquiries < 0 or credit_types < 0:
        return False

    if enquiries != float(user_data["loan_enquiries"]):
        return False

    if credit_types != float(user_data["credit_types"]):
        return False

    return True


# ==========================================================
# 7. DISPLAY CUSTOMER PROFILE
# ==========================================================

def display_user_data(user_data):

    if not validate_user_data(user_data):

        print("\nCannot display profile: Invalid customer data.")
        return

    print("\n")
    print("=" * 60)
    print("              CUSTOMER FINANCIAL PROFILE")
    print("=" * 60)

    print(f"\nCustomer Name          : {user_data['name']}")

    print(
        f"On-Time Payment        : "
        f"{user_data['payment_history']}%"
    )

    print(
        f"Credit Utilization     : "
        f"{user_data['credit_utilization']}%"
    )

    print(
        f"Oldest Credit Account  : "
        f"{user_data['credit_age']} years"
    )

    print(
        f"Recent Loan Enquiries  : "
        f"{user_data['loan_enquiries']}"
    )

    print(
        f"Different Credit Types: "
        f"{user_data['credit_types']}"
    )

    print("=" * 60)


# ==========================================================
# 8. COMPATIBILITY FUNCTIONS
# ==========================================================
# These aliases help other modules use different function names.

def collect_user_data():
    return get_user_input()


def get_user_data():
    return get_user_input()


def input_user_data():
    return get_user_input()


def get_user_details():
    return get_user_input()
# ==========================================================
# BACKWARD COMPATIBILITY WITH MAIN.PY
# ==========================================================

def collect_user_details():
    return get_user_input()


def display_user_details(user_data):
    return display_user_data(user_data)
