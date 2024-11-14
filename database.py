# database.py

import sqlite3

def initialize_db():
    """Initialize the database and create tables if not exist."""
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )
    ''')
    conn.commit()
    conn.close()