# Financial Tracker Application
# This file contains the main logic for the financial tracker application. 
# It provides a command-line interface for users to interact with their financial data, 
# allowing them to add, find, update, remove, and view transactions.

from .transaction import Transaction
from .transactions_manager import Transactions_Manager


def show_menu(tracker):
    """Display the main menu and handle user input for the financial tracker application."""

    print("-----------------------------------------------------")
    print("      Welcome to FINATRACKER")
    print("we help you track your finances easily")
    print("-----------------------------------------------------")
    print(f"Current balance: €{tracker.calculate_balance():.2f}")
    print()
    print("What would you like to do now?")
    print("-----------------------------------------------------")  
    print("💸 TRANSACTIONS")
    print("-----------------------------------------------------")
    print("1. Add income/expense transaction")
    print("2. Find transactions")
    print("3. Update transactions")
    print("4. Remove a transaction")
    print("-----------------------------------------------------")  
    print("📊 SUMMARY AND ANALYSIS ")
    print("-----------------------------------------------------")
    print("5. Monthly summary")
    print("6. Category summary")
    print("7. View all transactions")
    print("-----------------------------------------------------")
    print("8. Exit")



def main():
    tracker = Transactions_Manager()
    tracker.load_transactions()  # Load existing transactions from the file

    while True:
        show_menu(tracker)

        choice = input("Please enter your choice here: ")

        if choice == "1":  # add transaction
            while True:
                date = input("Please enter the date (YYYY-MM-DD): ")
                try:
                    date = Transaction.valid_date(date)
                    break
                except ValueError as e:
                    print(e)

            while True:
                tst_type = input(
                    "What type of transaction is this? (please enter I for Income or E for Expense): ")
                try:
                    tst_type = Transaction.valid_type(tst_type)
                    break
                except ValueError as e:
                    print(e)

            while True:
                amount = input("Please enter the amount: ")
                try:
                    amount = Transaction.valid_amount(amount)
                    break
                except ValueError as e:
                    print(e)

            category = input("Please enter the category (optional): ")
            description = input("Please enter a description (optional): ")
            transaction = Transaction(
                date, tst_type, amount, category, description)
            tracker.add_transaction(transaction)
            tracker.save_transactions()
            print("Thank you! Transaction added successfully!")
            input("\nPress Enter to return to the main menu...")

        elif choice == "2":  # find/filter transactions
            print(
                "\nYou can find transactions by Transaction ID, date, type, or category.")
            print("Please choose one of the following options:")
            print("1. Find by transaction ID")
            print("2. Find by date")
            print("3. Find by type (income/expense)")
            print("4. Find by category")

            filter_choice = input("Please enter your choice here: ")
            if filter_choice == "1":
                transaction_id = int(
                    input("Please enter the transaction ID: "))
                results = tracker.find_transactions(ID=transaction_id)
            
            elif filter_choice == "2":
                date = input("Please enter the date (YYYY-MM-DD): ")
                results = tracker.find_transactions(date=date)

            elif filter_choice == "3":
                tst_type = input(
                    "Please enter I for Income or E for Expense: ").upper()
                try:
                    tst_type = Transaction.valid_type(tst_type)
                except ValueError as e:
                    print(e)
                    continue

                results = tracker.find_transactions(tst_type=tst_type)
            
            elif filter_choice == "4":
                category = input("Please enter the category: ")
                results = tracker.find_transactions(category=category)
            
            else:
                print("Invalid choice. Please try again.")
                continue

            if results:
                for transaction in results:
                 print(transaction)
            else:
                 print("No matching transactions found.")
            input("\nPress Enter to return to the main menu...")


        elif choice == "3":  # update transaction
            tracker.update_transaction()
            tracker.save_transactions()
            input("\nPress Enter to return to the main menu...")


        elif choice == "4":  # remove transaction
            tracker.remove_transaction()
            tracker.save_transactions()
            input("\nPress Enter to return to the main menu...")


        elif choice == "5": # Monthly summary
            tracker.monthly_summary()
            input("\nPress Enter to return to the main menu...")


        elif choice == "6":  # Category summary
            tracker.category_summary()
            input("\nPress Enter to return to the main menu...")


        elif choice == "7":  # View all transactions
            tracker.view_all_transactions()
            input("\nPress Enter to return to the main menu...")


        elif choice == "8":  # exit
            print("Thank you for using FinaTracker!")
            print("Have a great day! Goodbye!")
            break
        else:
            print("Invalid choice.")

        

if __name__ == "__main__":
    main()