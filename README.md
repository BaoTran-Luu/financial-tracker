
# **💰 FinaTracker**

FINATRACKER is a Python application for managing personal finances. It allows users to record and manage income and expenses, track their current balance, and view useful financial summaries through a simple graphical user interface.

## *✨ Features*
- Add transactions — Record income and expenses with date, amount, category, and description.
- Find transactions — Search by ID, date, type, or category.
- Update transactions — Modify existing transaction details.
- Remove transactions — Delete transactions by ID.
- View transactions — Display all recorded transactions.
- Track balance — Automatically calculate the current balance.
- Monthly summaries — Analyse income, expenses, and balance by month.
- Category summaries — Analyse transactions by category and type.
- Data persistence — Transactions are automatically saved to and loaded from a CSV file.
- Input validation — Validate dates, amounts, and transaction types.

## *🛠️ Technologies*
- Python 3.10+
- pandas — Data processing and financial summaries
- uv — Dependency and project management
- Git & GitHub — Version control

## *📁 Project Structure*

```text
financial-tracker/
├── src/
│   └── financial_tracker/
│       ├── __init__.py
│       ├── __main__.py
|       ├── gui.py
│       ├── transaction.py
│       └── transactions_manager.py
├── transaction.csv
├── pyproject.toml
├── uv.lock
└── README.md
```
## *Main Components*

*transaction.py*
Contains the Transaction class, including transaction attributes and input validation.
*transactions_manager.py*
Handles transaction management, searching, updating, removing, persistence, and financial summaries.
*__main__.py*
Provides the command-line interface and handles user interaction.
*gui.py*
Provides the graphical user interface using Tkinter and allows users to manage transactions, view their current balance, and access financial summaries.

## *🚀 Installation*
*Requirements*
Python 3.10 or newer
uv
Clone the repository and navigate to the project directory:
git clone https://github.com/BaoTran-Luu/financial-tracker.git
cd financial-tracker

*Install the project dependencies:*
uv sync
## *▶️ Run the Application*

*Start FinaTracker with:*
uv run -m financial_tracker.gui
The application will open the graphical user interface, where users can add, update, remove, and view transactions, track their current balance, and access financial summaries.

The command-line interface is also available for users who prefer to manage their finances through the terminal as below:
uv run -m financial_tracker

## *💾 Data Storage*
Transactions are stored locally in:
transaction.csv
Existing transactions are loaded when the application starts. Changes are automatically saved when transactions are added, updated, or removed.

## *🎓 About This Project and Notes😭*
Thank you so much for reading and running my first code/app ever!
This was my first programming course ever, and I learned (and struggled) a lot throughout this project. I started with a command-line-only application and then expanded it with a graphical user interface.

At one point, I wasn't sure if I would be able to finish everything on time, so I decided to keep both versions. I plan to continue improving gui.py in the future, as there are still many things I would like to add.

However, one of the most important things I learned from this project is knowing when to stop. So, for this course, this is where I will leave FINATRACKER.

Thank you so much for reading and, hopefully, running my first piece of code and first app ever!