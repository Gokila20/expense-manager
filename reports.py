import pandas as pd
from database import get_db_connection
from fpdf import FPDF
import matplotlib.pyplot as plt

# Generate summary by category


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


# Export summary to Excel


def export_to_excel():
    summary = generate_summary()
    if summary is not None:
        summary.to_excel("expense_summary.xlsx", index=False)
        print(" Report exported to Excel: expense_summary.xlsx")


# Export summary to PDF


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
        print(" Report exported to PDF: expense_summary.pdf")


def show_expense_chart():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT category, amount FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No data found to plot chart.")
        return

    # Summarize total amount by category
    summary = df.groupby("category", as_index=False)["amount"].sum()

    # Create the bar chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(summary["category"],
                   summary["amount"],
                   color="#4E79A7",
                   width=0.6)

    # Add chart title and labels
    plt.title("💰 Total Expenses by Category",
              fontsize=14,
              fontweight="bold",
              pad=20)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Amount", fontsize=12)

    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2,
                 yval + 20,
                 f"{yval:.0f}",
                 ha="center",
                 va="bottom",
                 fontsize=10,
                 fontweight="bold")

    # Tight layout to avoid label cut-off
    plt.tight_layout()

    # Save the chart as an image (optional, used for PDF)
    plt.savefig("expense_chart.png")
    print("📊 Chart saved as expense_chart.png")

    # Display the chart
    plt.show()
