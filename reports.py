import pandas as pd
from database import get_db_connection
from fpdf import FPDF


# ---------------------------------------------
# Generate summary by category
# ---------------------------------------------
def generate_summary():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT category, amount FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No data found.")
        return None

    summary = df.groupby("category", as_index=False)["amount"].sum()
    print("\n=== Expense Summary by Category ===")
    print(summary.to_string(index=False))
    return summary


# ---------------------------------------------
# Export summary to Excel
# ---------------------------------------------
def export_to_excel():
    summary = generate_summary()
    if summary is not None:
        summary.to_excel("expense_summary.xlsx", index=False)
        print("✅ Report exported to Excel: expense_summary.xlsx")


# ---------------------------------------------
# Export summary to PDF
# ---------------------------------------------
def export_to_pdf():
    summary = generate_summary()
    if summary is not None:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Expense Summary Report", ln=True, align="C")
        pdf.set_font("Arial", "", 12)

        pdf.cell(60, 10, "Category", 1, 0, "C")
        pdf.cell(60, 10, "Total Amount", 1, 1, "C")

        for _, row in summary.iterrows():
            pdf.cell(60, 10, str(row["category"]), 1, 0, "C")
            pdf.cell(60, 10, str(row["amount"]), 1, 1, "C")

        pdf.output("expense_summary.pdf")
        print("✅ Report exported to PDF: expense_summary.pdf")
