""" this module is used to manage the data for the application. 
It provides functions to load, save, and manipulate data in a structured way. 
The data is stored in a JSON format and can be easily accessed and modified using the provided functions."""

from transaction import Transaction


class Transactions_Manager:

    def __init__(self):
        self.transactions = []  # List to store Transaction objects

    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.transactions.append(transaction)
        else:
            raise ValueError("Only Transaction objects can be added.")
        return


    def update_transaction(self):
        """Update a transaction's attributes based on provided keyword arguments."""
        transaction_id = int(input("Enter the transaction ID to update: "))
        
        for transaction in self.transactions:
            if transaction.ID == transaction_id:
                print("What would you like to update?:"
                "\n1. Date  \n2. Type  \n3. Amount  \n4. Category  \n5. Description")
                choice = input("Please enter the corresponding number here:")

                if choice == "1":
                    new_date = input("Enter the new date (YYYY-MM-DD): ")
                    transaction.date = Transaction.valid_date(new_date)
                    print("Date updated successfully.")

                elif choice == "2":
                    new_tst_type = input("Enter the new type (income/expense): ")
                    transaction.tst_type = new_tst_type.lower()
                    print("Type updated successfully.")
                
                elif choice == "3":
                    new_amount = input("Enter the new amount: ")
                    transaction.amount = Transaction.valid_amount(new_amount)    
                    print("Amount updated successfully.")

                elif choice == "4":
                    new_category = input("Enter the new category: ")
                    transaction.category = new_category.strip() if new_category else "Uncategorized"
                    print("Category updated successfully.")

                elif choice == "5":
                    new_description = input("Enter the new description: ")
                    transaction.description = new_description.strip() if new_description else ""
                    print("Description updated successfully.")
                
                else: print("Invalid choice. No updates made.")
                return  # Exit after updating the transaction
            raise ValueError(f"No transaction found with ID {transaction_id}")
        return  # Exit after updating the transaction

    def remove_transaction(self):
        """Remove a transaction by its ID."""
        transaction_id = int(input("Enter the transaction ID to remove: "))
        for transaction in self.transactions:
            if transaction.ID == transaction_id:
                self.transactions.remove(transaction)
                print("Transaction removed.")
                return 
        print(f"No transaction found with ID {transaction_id}.")
    
    def view_all_transactions(self): 
        """view all past transactions"""
        if len(self.transactions) == 0:
            print("No transactions found.")
            return
        for transaction in self.transactions:
            print(f"ID: {transaction.ID}, Date: {transaction.date}, Type: {transaction.tst_type}, "
                  f"Amount: {transaction.amount}, Category: {transaction.category}, "
                  f"Description: {transaction.description}"
                  )


    def calculate_balance(self):
        """Calculate and return the current balance based on all transactions."""
        balance = 0.0
        for transaction in self.transactions:
            balance += transaction.signed_amount()
        return balance

