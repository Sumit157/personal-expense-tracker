# personal-expense-tracker
<b>The Personal Expense Tracker is a command-line app for managing daily expenses. It allows users to add, view, update, and delete expense records with categories, storing data in an SQLite database. This tool helps users monitor their spending habits and manage their personal finances effectively.<b>

## Features
- **Add Expense**: Log new expenses with date, category, description, and amount.
- **View Expenses**: Display all recorded expenses in a structured format.
- **Update Expense**: Modify existing expense details by ID.
- **Delete Expense**: Remove an expense entry by ID.

## Technologies Used
- **Python**: For core application logic.
- **SQLite**: As a lightweight database to store and retrieve expense data.

## Usage
- **Run the Application**: python expense_tracker.py
- Personal Expense Tracker
- **Add Expense**: Input the date, category, description, and amount.
- **View Expenses**: Lists all expenses by ID, date, category, description, and amount.
- **Update Expense**: Enter the ID of the expense to update, followed by new details.
- **Delete Expense**: Enter the ID of the expense to delete.

## Database Structure
- The SQLite database (expense_tracker.db) contains a single table expenses with the following fields:

- id: Unique identifier (auto-incremented).
- date: Date of the expense in YYYY-MM-DD format.
- category: Category name (e.g., Food, Rent).
- description: Brief description of the expense.
- amount: Amount spent (as a decimal value).
