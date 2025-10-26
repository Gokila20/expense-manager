import sqlite3


def get_db_connection():
    conn = sqlite3.connect("expenses.db")
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT,
            payment_mode TEXT,
            merchant_name TEXT,
            location TEXT,
            notes TEXT,
            created_by TEXT
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("✅ Table created successfully!")
