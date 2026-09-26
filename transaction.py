""" Transaction class for handling financial transactions. """

from datetime import datetime


class Transaction:
    """Represents a normal valid financial transaction ."""
    # tst is the short form of transaction
    next_ID = 1  # Class variable to keep track of the next available ID

    def __init__(self, date, tst_type, amount, category, description):
        self.ID = Transaction.next_ID  # Assign the current next_ID to this transaction
        Transaction.next_ID += 1  # Increment the next_ID for the next transaction
        self.date = self.valid_date(date)  # Expected format: 'YYYY-MM-DD'
        self.tst_type = tst_type.lower()  # Should be 'income' or 'expense'
        self.amount = self.valid_ammount(amount)
        self.category = category.strip() if category else "Uncategorized"
        self.description = description.strip() if description else ""

    @staticmethod
    def valid_date(date_str):
        formats = ("%Y-%m-%d", "%d/%m/%Y", "%Y%m%d", "%m/%d/%Y", "%d-%m-%Y", "%Y.%m.%d", "%d.%m.%Y",
                   "%Y%d%m", "%d%m%Y", "%Y/%m/%d", "%d/%m/%y", "%m/%d/%y", "%d-%m-%y", "%Y.%m.%d", "%d.%m.%y")

        for fmt in formats:
            try:
                datetime.strptime(date_str, fmt)
                return date_str
            except (ValueError, TypeError):
                continue
        raise ValueError(
            f"Invalid date '{date_str}'. Expected format YYYY-MM-DD.")

    @staticmethod
    def valid_amount(amount):
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except (ValueError, TypeError):
            raise ValueError(
                f"Invalid amount '{amount}'. Must be a non-negative number.")
        return amount

    def signed_amount(self):
        """Return the amount as positive for income and negative for expense."""

        if self.tst_type == "income":
            return self.amount
        else:
            return -self.amount
