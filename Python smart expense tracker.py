import datetime


def display_menu():
    print("\n=================================")
    print("   SMART EXPENSE TRACKER MENU    ")
    print("=================================")
    print("1. Set/Update Monthly Budget")
    print("2. Add an Expense")
    print("3. View All Expenses")
    print("4. View Expense Analysis & Budget Report")
    print("5. Exit")
    print("=================================")


def set_budget():
    """Sets the global monthly budget."""
    global budget
    try:
        amount = float(input("Enter your monthly budget amount ($): "))
        if amount < 0:
            print("Budget cannot be negative!")
            return
        budget = amount
        print(f"Monthly budget successfully set to ${budget:.2f}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def add_expense():
    """Adds a new expense to the list using a dictionary structure."""
    if budget == 0.0:
        print(
            "Warning: Your budget is currently set to $0.00. You might want to set a budget first!"
        )

    try:
        amount = float(input("Enter expense amount ($): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        print("\nChoose a category:")
        for idx, cat in enumerate(categories, 1):
            print(f"  {idx}. {cat}")
        print(f"  {len(categories) + 1}. Other")

        cat_choice = int(input("Select category number: "))

        if 1 <= cat_choice <= len(categories):
            category = categories[cat_choice - 1]
        elif cat_choice == len(categories) + 1:
            category = input("Enter custom category name: ").strip().capitalize()
            if not category:
                category = "Other"
            if category not in categories:
                categories.append(category)
        else:
            print("Invalid category choice. Defaulting to 'Other'.")
            category = "Other"

        description = input("Enter a brief description: ").strip()
        if not description:
            description = "Unspecified"

        # Recording the current date
        date_str = datetime.date.today().strftime("%Y-%m-%d")

        # Creating the expense dictionary record
        expense_item = {
            "date": date_str,
            "amount": amount,
            "category": category,
            "description": description,
        }

        # Appending to the central tracking list
        expenses.append(expense_item)
        print(f"Expense of ${amount:.2f} under '{category}' added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data types.")


def view_expenses():
    """Displays all recorded expenses in a clean, tabular format."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print(
        "\n-----------------------------------------------------------------"
    )
    print(
        f"{'ID':<4} | {'Date':<12} | {'Category':<15} | {'Amount':<12} | {'Description'}"
    )
    print(
        "-----------------------------------------------------------------"
    )
    for idx, exp in enumerate(expenses, 1):
        print(
            f"{idx:<4} | {exp['date']:<12} | {exp['category']:<15} | ${exp['amount']:<11.2f} | {exp['description']}"
        )
    print(
        "-----------------------------------------------------------------"
    )


def view_analysis():
    """Performs budget tracking and personal data breakdown by category."""
    if not expenses:
        print("\n No data available to analyze. Add some expenses first!")
        return

    total_spent = sum(item["amount"] for item in expenses)

    print("\n=================================")
    print("    EXPENSE ANALYSIS REPORT     ")
    print("=================================")
    print(f"Total Budget Specified : ${budget:.2f}")
    print(f"Total Amount Spent     : ${total_spent:.2f}")

    # Budget Status Check
    if budget > 0:
        remaining = budget - total_spent
        if remaining >= 0:
            print(f"Remaining Budget       : ${remaining:.2f} (Safe)")
        else:
            print(
                f"Remaining Budget       : ${remaining:.2f} (OVER BUDGET BY ${abs(remaining):.2f}!)"
            )
    else:
        print("Remaining Budget       : N/A (Budget not configured)")

    print("\n--- Breakdown By Category ---")

    # Grouping logic using a dictionary
    category_totals = {}
    for item in expenses:
        cat = item["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + item["amount"]

    for cat, amt in category_totals.items():
        percentage = (amt / total_spent) * 100 if total_spent > 0 else 0
        print(f"• {cat:<15}: ${amt:<10.2f} ({percentage:.1f}%)")
    print("=================================")


# --- Global Data Structures ---
expenses = []  # List storing dictionaries of expense data
categories = ["Food", "Transport", "Utilities", "Entertainment", "Shopping"]
budget = 0.0  # Initial budget status

# --- Main Program Execution Loop ---
def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            set_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            view_analysis()
        elif choice == "5":
            print("\nThank you for using Smart Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid selection! Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()