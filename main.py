from database import create_table
from crud_operations import add_expense, view_expenses, update_expense, delete_expense
from reports import export_to_excel, export_to_pdf



def main_menu():
  create_table()

  while True:
    print("\n=== Expense Manager ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Generate Reports (Excel)")
    
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      date = input("Enter date (YYYY-MM-DD): ")
      category = input("Enter category: ")
      amount = float(input("Enter amount: "))
      description = input("Enter description: ")
      payment_mode = input("Enter payment mode: ")
      merchant_name = input("Enter merchant name: ")
      location = input("Enter location: ")
      notes = input("Enter notes: ")
      created_by = input("Enter your name: ")

      add_expense(date, category, amount, description, payment_mode,
                  merchant_name, location, notes, created_by)

    elif choice == "2":
      rows = view_expenses()
      if not rows:
        print("No expenses found.")
      else:
        for row in rows:
          print(row)

    elif choice == "3":
      expense_id = int(input("Enter expense ID to update: "))
      new_amount = float(input("Enter new amount: "))
      update_expense(expense_id, new_amount)

    elif choice == "4":
      expense_id = int(input("Enter expense ID to delete: "))
      delete_expense(expense_id)

    elif choice == "5":
      print("Goodbye 👋")
      break
    else:
      print("Invalid choice! Try again.")


if __name__ == "__main__":
  main_menu()
