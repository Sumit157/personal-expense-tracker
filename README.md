## Personal Expense Tracker

The Personal Expense Tracker is a command-line app for managing daily expenses. It allows users to add, view, update, and delete expense records with categories, storing data in an SQLite database. This tool helps users monitor their spending habits and manage their personal finances effectively.

## Project Directory Structure

```
personal-expense-tracker/          # Root project folder
│
├── expense_tracker.py             # Main program file (entry point)
├── database.py                    # Handles SQLite database setup and initialization
├── expense_operations.py          # Functions for adding, viewing, updating, and deleting expenses
├── expense_tracker.db             # SQLite database file (created when running the program)
├── README.md                      # Project documentation (this file)
└── requirements.txt               # Python dependencies (if any)
```

## Features
- **Add Expense**: Log new expenses with date, category, description, and amount.
- **View Expenses**: Display all recorded expenses in a structured format.
- **Update Expense**: Modify existing expense details by ID.
- **Delete Expense**: Remove an expense entry by ID.

## Technologies Used
- **Python**: For core application logic.
- **SQLite**: As a lightweight database to store and retrieve expense data.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sumit157/personal-expense-tracker.git
   cd personal-expense-tracker
   ```
   
## Usage

1. **Run the Application**:
   ```bash
   python expense_tracker.py
   ```

2. **Follow Menu Options**:
   Upon running, you’ll see a menu with options:
   ```
   Personal Expense Tracker
   1. Add Expense
   2. View Expenses
   3. Update Expense
   4. Delete Expense
   5. Exit
   ```
   - **Add Expense**: Input the date, category, description, and amount.
   - **View Expenses**: Lists all expenses by ID, date, category, description, and amount.
   - **Update Expense**: Enter the ID of the expense to update, followed by new details.
   - **Delete Expense**: Enter the ID of the expense to delete.

## Example

To add a new expense, select `1. Add Expense` from the main menu and enter the details as prompted:
```
Enter date (YYYY-MM-DD): 2024-11-13
Enter category (e.g., Food, Rent, Utilities): Food
Enter description: Lunch
Enter amount: 15.00
```
The expense is saved and confirmed with a success message.

## Database Structure

The SQLite database (`expense_tracker.db`) contains a single table `expenses` with the following fields:
- **id**: Unique identifier (auto-incremented).
- **date**: Date of the expense in `YYYY-MM-DD` format.
- **category**: Category name (e.g., Food, Rent).
- **description**: Brief description of the expense.
- **amount**: Amount spent (as a decimal value).

## Future Improvements
- Add export to CSV.
- Implement a graphical user interface (GUI).
- Provide monthly/weekly spending summaries.
