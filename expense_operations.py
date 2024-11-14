# expense_operations.py

import sqlite3

def add_expense():
    """Add a new expense to the database."""
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent, Utilities): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    
    cursor.execute('''
    INSERT INTO expenses (date, category, description, amount)
    VALUES (?, ?, ?, ?)
    ''', (date, category, description, amount))
    
    conn.commit()
    conn.close()
    print("Expense added successfully!")

def view_expenses():
    """Display all recorded expenses."""
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Description: {row[3]}, Amount: ${row[4]:.2f}")
    else:
        print("No expenses recorded.")
    
    conn.close()

def update_expense():
    """Update an existing expense."""
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    
    expense_id = int(input("Enter the ID of the expense to update: "))
    date = input("Enter new date (YYYY-MM-DD): ")
    category = input("Enter new category: ")
    description = input("Enter new description: ")
    amount = float(input("Enter new amount: "))
    
    cursor.execute('''
    UPDATE expenses
    SET date = ?, category = ?, description = ?, amount = ?
    WHERE id = ?
    ''', (date, category, description, amount, expense_id))
    
    conn.commit()
    conn.close()
    print("Expense updated successfully!")

def delete_expense():
    """Delete an expense by ID."""
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    
    expense_id = int(input("Enter the ID of the expense to delete: "))
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    
    conn.commit()
    conn.close()
    print("Expense deleted successfully!")
