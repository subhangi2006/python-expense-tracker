"""A simple command-line expense tracker for beginners.

Run with: python expense_tracker.py
"""

expenses = []


def add_expense():
    """Ask for expense details and add them to the list."""
    category = input("Enter expense category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount (INR): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    note = input("Enter a short note (optional): ").strip()
    expenses.append({"category": category, "amount": amount, "note": note})
    print("Expense added successfully!")


def view_expenses():
    """Display all saved expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- Expense History ---")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['category']} - "
            f"₹{expense['amount']:.2f} - {expense['note']}"
        )


def show_total():
    """Calculate and display the total amount spent."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}")


def show_category_summary():
    """Group expenses by category and display category totals."""
    if not expenses:
        print("\nNo expenses to summarize.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\n--- Category Summary ---")
    for category, amount in sorted(totals.items()):
        print(f"{category}: ₹{amount:.2f}")


def main():
    """Display the menu and handle the user's choice."""
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Show total spending")
        print("4. Show category summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_category_summary()
        elif choice == "5":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
