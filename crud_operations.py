from database import get_db_connection


def add_expense(date, category, amount, description, payment_mode,
                merchant_name, location, notes, created_by):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO expenses (date, category, amount, description, payment_mode, merchant_name, location, notes, created_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (date, category, amount, description, payment_mode, merchant_name,
          location, notes, created_by))
    conn.commit()
    conn.close()
    print("✅ Expense added successfully!")


def view_expenses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_expense(expense_id, new_amount):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE expenses SET amount = ? WHERE expense_id = ?",
                   (new_amount, expense_id))
    conn.commit()
    conn.close()
    print("✅ Expense updated successfully!")


def delete_expense(expense_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (expense_id, ))
    conn.commit()
    conn.close()
    print("🗑️ Expense deleted successfully!")
