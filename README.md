
# **💰 FinaTracker**

FinaTracker is a Python command-line application for managing personal finances. It allows users to record and manage income and expenses, track their current balance, and generate useful financial summaries.

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
uv run -m financial_tracker
The application will display an interactive menu for managing transactions and viewing financial summaries.

## *💾 Data Storage*
Transactions are stored locally in:
transaction.csv
Existing transactions are loaded when the application starts. Changes are automatically saved when transactions are added, updated, or removed.

## *🎓 About This Project and Notes (Please read this part)*
Developed as part of a Python programming project at TU Dortmund University.

This is my first programing course ever and I've learned (and truggled) a lot from this. I actually have an extra gui.py for this project but i am afraid that i can not make it on time as i am keep adding too many thing onit. For now, i will push it on Github without the gui.py and commit it later if i can make it :D

Anyway, thank you so much for reading and running my first code/app ever!