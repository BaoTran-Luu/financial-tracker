
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from .transaction import Transaction
from .transactions_manager import Transactions_Manager


def create_gui():
    """Create the main FINATRACKER window."""

    root = tk.Tk()

    root.title("FINATRACKER")
    root.geometry("900x700")
    root.configure(bg="lightblue")
    tracker = Transactions_Manager()
    tracker.load_transactions()

    title = ttk.Label(
        root,
        text="FINATRACKER",
        font=("Segoe UI", 24, "bold"),
        background="lightblue",
        foreground="grey30"
    )
    title.pack(pady=(25, 5))

    subtitle = ttk.Label(
        root,
        text="Your personal finance tracker",
        font=("Segoe UI", 14),
        background="lightblue",
        foreground="grey30"
    )
    subtitle.pack()

    # creat dashboard frame
    dashboard_frame = ttk.Frame(root)
    dashboard_frame.pack(pady=40)

    # balance card
    balance_card = ttk.LabelFrame(dashboard_frame, text="Balance", padding=20)
    balance_card.grid(row=0, column=0, padx=20)
    balance_value = ttk.Label(balance_card,
                              text="€0.00",
                              font=("Segoe UI", 16, "bold"), foreground="blue")
    balance_value.grid(row=1, column=0)
    
    def refresh_balance():
        """Refresh the displayed balance."""
        balance = tracker.calculate_balance()
        balance_value.config(text=f"€{balance:.2f}")

    # income card
    income_card = ttk.LabelFrame(dashboard_frame, text="Income", padding=20)
    income_card.grid(row=0, column=1, padx=20)
    income_value = ttk.Label(income_card,
                             text="€0.00",
                             font=("Segoe UI", 16, "bold"), foreground="green")
    income_value.grid(row=1, column=0)
    
    def refresh_income():
        """Update total income in dashboard"""
        income = sum(transaction.amount for transaction in tracker.transactions
                     if transaction.tst_type == "income")
        income_value.config(text=f"€{income:.2f}")

    # expenses card
    expenses_card = ttk.LabelFrame(
        dashboard_frame, text="Expenses", padding=20)
    expenses_card.grid(row=0, column=2, padx=20)
    expenses_value = ttk.Label(expenses_card,
                               text="€0.00",
                               font=("Segoe UI", 16, "bold"), foreground="red")
    expenses_value.grid(row=1, column=0)
    
    def refresh_expenses():
        expenses = sum(transaction.amount for transaction in tracker.transactions
                      if transaction.tst_type == "expense")
        expenses_value.config(text=f"€{expenses:.2f}")


    def create_table(parent, columns):
        """Create a unified styled table."""
        table = ttk.Treeview(
            parent,
            columns=columns,
            show="headings"
        )
        for column in columns:
            table.heading(column, text=column)
            table.column(column, width=100)

        table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        return table

    def refresh_table():
        """Refresh the transaction table."""
        # Remove existing rows
        for item in table.get_children():
            table.delete(item)
            # Add current transactions
        for transaction in tracker.transactions:
            table.insert("", "end",
                         values=(
                             transaction.ID,
                             transaction.date,
                             transaction.tst_type,
                             transaction.amount,
                             transaction.category,
                             transaction.description))
        refresh_balance()
        refresh_income()
        refresh_expenses()

    # add transaction table
    table_frame = ttk.Frame(root)
    table_frame.pack(fill="both", expand=True, padx=30, pady=15)
    table = create_table(table_frame, columns=(
        "ID", "Date", "Type", "Amount", "Category", "Description"))

    def add_transaction():  # Create add function for buttons
        """Open the window for user to add transaction"""

        add_window = tk.Toplevel(root)
        add_window.title("Add Transaction")
        add_window.geometry("300x350")

        ttk.Label(add_window, text="Date").pack(pady=5)
        date_entry = DateEntry(  # add calendar
            add_window,
            date_pattern="yyyy-mm-dd"
        )
        date_entry.pack()

        ttk.Label(add_window, text="Type").pack(pady=5)
        type_entry = ttk.Combobox(  # type entry will be dropbox
            add_window,
            values=["income", "expense"],
            state="readonly"
        )
        type_entry.pack()

        ttk.Label(add_window, text="Amount").pack(pady=5)
        amount_entry = ttk.Entry(add_window)
        amount_entry.pack()

        ttk.Label(add_window, text="Category").pack(pady=5)
        category_entry = ttk.Entry(add_window)
        category_entry.pack()

        ttk.Label(add_window, text="Description").pack(pady=5)
        description_entry = ttk.Entry(add_window)
        description_entry.pack()

        def save_transaction():
            """Save the new transaction."""
            try:  # check valid input
                date = Transaction.valid_date(date_entry.get())
                tst_type = Transaction.valid_type(type_entry.get())
                amount = Transaction.valid_amount(amount_entry.get())
            except ValueError as e:
                messagebox.showerror(
                    "Invalid Information",
                    str(e),
                    parent=add_window
                )
                return

            category = category_entry.get()
            description = description_entry.get()
            if not category:  # check if required field is filled
                messagebox.showwarning(
                    "Missing Information",
                    "Please enter a category.",
                    parent=add_window
                )
                return
            transaction = Transaction(
                date,
                tst_type,
                amount,
                category,
                description
            )
            tracker.add_transaction(transaction)
            tracker.save_transactions()

            refresh_table()
            add_window.destroy()

        ttk.Button(
            add_window,
            text="Save Transaction",
            command=save_transaction
        ).pack(pady=20)

    def find_transaction():  # Create find and search window
        """Open the window for finding transactions."""
        find_window = tk.Toplevel(root)
        find_window.title("Find Transaction")
        find_window.geometry("700x500")

        ttk.Label(
            find_window,
            text="Search Transactions"
        ).pack(pady=10)

        # Search field
        search_entry = ttk.Entry(find_window, width=40)
        search_entry.pack(pady=5)

        def search_transactions():
            """Search for transactions - button."""

            search_text = search_entry.get().lower()

            # Clear previous results
            for item in result_table.get_children():
                result_table.delete(item)

            # Search through transactions
            for transaction in tracker.transactions:
                if (
                    search_text in str(transaction.ID).lower()
                    or search_text in str(transaction.date).lower()
                    or search_text in str(transaction.tst_type).lower()
                    or search_text in str(transaction.amount).lower()
                    or search_text in str(transaction.category).lower()
                    or search_text in str(transaction.description).lower()
                ):
                    result_table.insert(
                        "",
                        "end",
                        values=(
                            transaction.ID,
                            transaction.date,
                            transaction.tst_type,
                            transaction.amount,
                            transaction.category,
                            transaction.description
                        )
                    )

        # Search button
        ttk.Button(
            find_window,
            text="Search",
            command=search_transactions
        ).pack(pady=10)

        result_table = create_table(
            find_window,
            columns=(
                "ID", "Date", "Type", "Amount", "Category", "Description"))

    def update_transaction():  # Create update window, save update
        """Open the window for updating a transaction."""
        selected_item = table.selection()  # select transaction to update

        if not selected_item:
            messagebox.showwarning(
                "No Selection",
                "Please select a transaction first.")
            return

        values = table.item(selected_item[0], "values")
        transaction_id = values[0]
        transaction = next(
            (t for t in tracker.transactions
                if str(t.ID) == str(transaction_id)), None)

        if transaction is None:
            messagebox.showerror(
                "Error",
                "Transaction could not be found.")
            return

        update_window = tk.Toplevel(root)
        update_window.title("Update Transaction")
        update_window.geometry("400x400")

        # Update date
        ttk.Label(update_window, text="Date").pack(pady=5)
        date_entry = DateEntry(
            update_window,
            date_pattern="yyyy-mm-dd")
        date_entry.set_date(transaction.date)
        date_entry.pack()

        # Update type
        ttk.Label(update_window, text="Type").pack(pady=5)
        type_entry = ttk.Combobox(
            update_window,
            values=["income", "expense"],
            state="readonly")
        type_entry.set(transaction.tst_type)
        type_entry.pack()

        # Update amount
        ttk.Label(update_window, text="Amount").pack(pady=5)
        amount_entry = ttk.Entry(update_window)
        amount_entry.insert(0, transaction.amount)
        amount_entry.pack()

        # Update Category
        ttk.Label(update_window, text="Category").pack(pady=5)
        category_entry = ttk.Entry(update_window)
        category_entry.insert(0, transaction.category)
        category_entry.pack()

        # Update Description
        ttk.Label(update_window, text="Description").pack(pady=5)
        description_entry = ttk.Entry(update_window)
        description_entry.insert(0, transaction.description)
        description_entry.pack()

        # Add save change button
        def save_changes():
            """Save the updated transaction."""
            try:
                date = Transaction.valid_date(date_entry.get())
                tst_type = Transaction.valid_type(type_entry.get())
                amount = Transaction.valid_amount(amount_entry.get())

            except ValueError as e:
                messagebox.showerror(
                    "Invalid Information",
                    str(e),
                    parent=update_window)
                return

            category = category_entry.get()
            description = description_entry.get()

            if not category:
                messagebox.showwarning(
                    "Missing Information",
                    "Please enter a category.",
                    parent=update_window)
                return

            # Update the existing transaction
            transaction.date = date
            transaction.tst_type = tst_type
            transaction.amount = amount
            transaction.category = category
            transaction.description = description

            # Save changes to CSV
            tracker.save_transactions()
            refresh_table()
            update_window.destroy()

        # Save button
        ttk.Button(
            update_window,
            text="Save Changes",
            command=save_changes
        ).pack(pady=20)

    def remove_transaction():  # Create confirm and remove transaction
        """Remove transaction - button"""
        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning(
                "No Selection",
                "Please select a transaction first.")
            return

        values = table.item(selected_item[0], "values")
        transaction_id = values[0]
        transaction = next(
            (t for t in tracker.transactions
                if str(t.ID) == str(transaction_id)), None)

        if transaction is None:
            messagebox.showerror(
                "Error",
                "Transaction could not be found.")
            return

        confirm = messagebox.askyesno(
            "Remove Transaction",
            f"Are you sure you want to remove transaction {transaction.ID}?")

        if not confirm:
            return

        tracker.transactions.remove(transaction)
        tracker.save_transactions()

        refresh_table()

    # Buttons for adding, editing, and removing transactions
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    ttk.Button(button_frame, text="Add Transaction",
               command=add_transaction
               ).grid(row=0, column=0, padx=10)

    ttk.Button(button_frame, text="Find Transaction",
               command=find_transaction
               ).grid(row=0, column=1, padx=10)

    ttk.Button(button_frame, text="Update Transaction",
               command=update_transaction
               ).grid(row=0, column=2, padx=10)

    ttk.Button(button_frame, text="Remove Transaction",
               command=remove_transaction).grid(
        row=0, column=3, padx=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
