
""" This module is used to manage the data for the application. 
It provides functionalities to add, find, update, remove, and view transactions, as well as to calculate the current balance based on all transactions.
The transactions are stored in a CSV file, allowing for persistent storage and retrieval of financial data."""

import csv
import pandas as pd
from .transaction import Transaction
from financial_tracker import transaction


class Transactions_Manager:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        """Add a new transaction to the list of transactions."""
        if isinstance(transaction, Transaction):
            self.transactions.append(transaction)
        else:
            raise ValueError("Only Transaction objects can be added.")
        return

    def save_transactions(self):
        """Save transactions to the transaction     CSV file."""
        with open("transaction.csv", mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Date", "Type", "Amount",
                            "Category", "Description"])
            for transaction in self.transactions:
                writer.writerow([transaction.ID, transaction.date, transaction.tst_type,
                                 transaction.amount, transaction.category, transaction.description])

    def load_transactions(self):
        """Load transactions from the transaction CSV file."""
        try:
            with open("transaction.csv", mode="r") as file:
                reader = csv.DictReader(file)
                self.transactions = []
                for row in reader:
                    transaction = Transaction(
                        row["Date"], row["Type"], row["Amount"], row["Category"], row["Description"])
                    transaction.ID = int(row["ID"])  # Ensure ID is an integer
                    self.transactions.append(transaction)
        except FileNotFoundError:
            print("No existing transaction file found. Starting with an empty list.")

    def find_transactions(self, **kwargs):
        """Find or filter transactions based on provided keyword arguments."""
        found_transactions = self.transactions
        for key, value in kwargs.items():
            found_transactions = [
                t for t in found_transactions if getattr(t, key) == value]
        return found_transactions

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
                    while True:
                        new_tst_type = input(
                            "Enter the new type (income/expense): ")
                        try:
                            transaction.tst_type = Transaction.valid_type(
                                new_tst_type)
                            print("Type updated successfully.")
                            break
                        except ValueError as e:
                            print(e)
                    
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

                else:
                    print("Invalid choice. No updates made.")
                return
        raise ValueError(f"No transaction found with ID {transaction_id}")

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

    def monthly_summary(self):
        """Show income, expenses, and balance for each month."""
        if not self.transactions:
            print("No transactions found.")
            return

        data = {
            "Date": [t.date for t in self.transactions],
            "Type": [t.tst_type for t in self.transactions],
            "Amount": [t.amount for t in self.transactions]
        }
        df = pd.DataFrame(data)

        # Convert 'Date' to datetime and extract month
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.to_period('M')

        # Group by month and type, then sum amounts
        summary = df.groupby(['Month', 'Type'])[
            'Amount'].sum().unstack(fill_value=0)
        summary['Balance'] = summary.get(
            'income', 0) - summary.get('expense', 0)
        print(summary)
    
    def category_summary(self):
        """Show total income and expenses by category."""
        if not self.transactions:
            print("No transactions found.")
            return

        data = {
            "Category": [t.category for t in self.transactions],
            "Type": [t.tst_type for t in self.transactions],
            "Amount (€)": [t.amount for t in self.transactions]
        }
        df = pd.DataFrame(data)
        summary = df.groupby(["Category", "Type"])["Amount (€)"].sum().reset_index()
        print(summary.to_string(index=False, formatters={"Amount (€)": "{:.2f}".format}))

    def calculate_balance(self):
        """Calculate and return the current balance based on all transactions."""
        balance = 0.0
        for transaction in self.transactions:
            balance += transaction.signed_amount()
        return balance
