""" Transaction class for handling financial transactions. 
This class provides methods for validating transaction data, includeing date, time and amount 
as well as calculating signed amounts based on transaction type. """

from datetime import datetime


class Transaction:
    """Represents a normal valid financial transaction ."""
    # tst is the short form of transaction
    next_ID = 1  # Class variable to keep track of the next available ID

    def __init__(self, date, tst_type, amount, category, description):
        self.ID = Transaction.next_ID  # Assign the current next_ID to this transaction
        Transaction.next_ID += 1  # Increment the next_ID for the next transaction
        self.date = Transaction.valid_date(date)  # Expected format: 'YYYY-MM-DD'
        self.tst_type = Transaction.valid_type(tst_type)  # Should be 'income' or 'expense'
        self.amount = Transaction.valid_amount(amount)
        self.category = category.strip() if category else "Uncategorized"
        self.description = description.strip() if description else ""

    @staticmethod
    def valid_date(date_str):
        """Validate the date format. Accepts multiple formats and returns the date in 'YYYY-MM-DD' format."""
        formats = ("%Y-%m-%d", "%d/%m/%Y", "%Y%m%d", "%m/%d/%Y", "%d-%m-%Y", "%Y.%m.%d", "%d.%m.%Y",
                   "%Y%d%m", "%d%m%Y", "%Y/%m/%d", "%d/%m/%y", "%m/%d/%y", "%d-%m-%y", "%Y.%m.%d", "%d.%m.%y")

        for fmt in formats:
            try:
                date=datetime.strptime(date_str, fmt)
                return date.strftime("%Y-%m-%d")  # Return in standard format     
            except (ValueError, TypeError):
                continue
        raise ValueError(
            f"Invalid date '{date_str}'. Expected format YYYY-MM-DD.")

    @staticmethod
    def valid_type(tst_type):
        """Validate the transaction type. Accepts 'I' or 'E' the full forms and returns 'income' or 'expense'."""
        tst_type = tst_type.upper()

        if tst_type == "I" or tst_type == "INCOME":
            return "income"
        elif tst_type == "E" or tst_type == "EXPENSE":
            return "expense"
        else:
            raise ValueError("Invalid type. Please enter I for income or E for expense.")

    @staticmethod
    def valid_amount(amount):
        """Validate the amount. Accepts positive numbers and returns a float."""
        try:
            if isinstance(amount, str):
                amount = amount.replace(',', '.')
            amount = float(amount)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            return amount
        
        except (ValueError, TypeError):
            raise ValueError(
                f"Invalid amount '{amount}'. Must be a non-negative number.")
        
    def __str__(self):
        """Return a string representation of the transaction."""
        return (
            f"ID: {self.ID}, "
            f"Date: {self.date}, "
            f"Type: {self.tst_type}, "
            f"Amount: {self.amount:.2f}, "
            f"Category: {self.category}, "
            f"Description: {self.description}"
        )


    def signed_amount(self):
        """Return the amount as positive for income and negative for expense."""

        if self.tst_type == "income":
            return self.amount
        else:
            return -self.amount
    