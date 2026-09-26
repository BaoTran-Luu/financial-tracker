# Financial Tracker Application

from transaction import Transaction
from transactions_manager import Transactions_Manager

# Initialize the transactions manager
tracker = Transactions_Manager()


def show_menu(tracker):
    """Display the main menu and handle user input for the financial tracker application."""

    print("-----------------------------------------------------")
    print("      Welcome to FINATRACKER")
    print("we help you track your finances easily")
    print("-----------------------------------------------------")
    print(f"Current balance: €{tracker.calculate_balance():.2f}")
    print()
    print("What would you like to do now?")
    print("1. Add income/expense transaction")
    print("2. Update transactions")
    print("3. Remove a transaction")
    print("4. View all transactions")
    print("5. Exit")


def main():
    while True:
        show_menu(tracker)

        choice = input("Please enter your choice here: ")

        if choice == "1":  # add transaction
            date = input("Please enter the date (YYYY-MM-DD): ")
            tst_type = input("Do you want to add an income or expense? ")
            amount = input("Please enter the amount: ")
            category = input("Please enter the category (optional): ")
            description = input("Please enter a description (optional): ")
            transaction = Transaction(
                date, tst_type, amount, category, description)
            tracker.add_transaction(transaction)
            print("Thank you! Transaction added successfully!")

        elif choice == "2":  # update transaction
            tracker.update_transaction()
        elif choice == "3":  # remove transaction
            tracker.remove_transaction()
        elif choice == "4":  # View all transactions
            tracker.view_all_transactions()
        elif choice == "5":  # exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
