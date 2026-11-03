
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import date

# Create Database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    expense_date TEXT NOT NULL
)
""")

conn.commit()


# Add Expense
def add_expense():
    name = name_entry.get().strip()
    amount = amount_entry.get().strip()
    category = category_box.get()
    expense_date = date_entry.get().strip()

    if not name or not amount or not category or not expense_date:
        messagebox.showwarning(
            "Warning", "Please fill in all fields!"
        )
        return

    try:
        amount = float(amount)

        if amount <= 0:
            messagebox.showwarning(
                "Warning", "Amount must be greater than zero!"
            )
            return

        date.fromisoformat(expense_date)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid amount and date (YYYY-MM-DD)!"
        )
        return

    cursor.execute("""
    INSERT INTO expenses (name, amount, category, expense_date)
    VALUES (?, ?, ?, ?)
    """, (name, amount, category, expense_date))

    conn.commit()

    clear_fields()
    show_expenses()
    messagebox.showinfo("Success", "Expense added successfully!")


# Display Expenses
def show_expenses():
    for item in expense_table.get_children():
        expense_table.delete(item)

    cursor.execute("""
    SELECT id, name, amount, category, expense_date
    FROM expenses
    ORDER BY id DESC
    """)

    for row in cursor.fetchall():
        expense_table.insert("", tk.END, values=row)

    update_total()


# Delete Selected Expense
def delete_expense():
    selected = expense_table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning", "Please select an expense to delete!"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm", "Do you want to delete this expense?"
    )

    if confirm:
        item = expense_table.item(selected[0])
        expense_id = item["values"][0]

        cursor.execute(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,)
        )

        conn.commit()
        show_expenses()

        messagebox.showinfo(
            "Success", "Expense deleted successfully!"
        )


# Calculate Total Expense
def update_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    total_label.config(text=f"Total Expense: Rs. {total:.2f}")


# Clear Input Fields
def clear_fields():
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_box.set("")
    date_entry.delete(0, tk.END)
    date_entry.insert(0, str(date.today()))


# Main Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("850x600")
root.minsize(750, 500)

title_label = tk.Label(
    root,
    text="EXPENSE TRACKER",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)


# Input Form
form = tk.Frame(root)
form.pack(pady=10)

tk.Label(form, text="Expense Name:").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)

name_entry = tk.Entry(form, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form, text="Amount (Rs.):").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)

amount_entry = tk.Entry(form, width=25)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form, text="Category:").grid(
    row=2, column=0, padx=5, pady=5, sticky="w"
)

category_box = ttk.Combobox(
    form,
    values=["Food", "Travel", "Shopping", "Education", "Other"],
    state="readonly",
    width=22
)
category_box.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form, text="Date (YYYY-MM-DD):").grid(
    row=3, column=0, padx=5, pady=5, sticky="w"
)

date_entry = tk.Entry(form, width=25)
date_entry.grid(row=3, column=1, padx=5, pady=5)
date_entry.insert(0, str(date.today()))


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Expense",
    command=add_expense,
    width=15
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Delete Expense",
    command=delete_expense,
    width=15
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Clear Fields",
    command=clear_fields,
    width=15
).grid(row=0, column=2, padx=5)


# Expense Table
columns = ("ID", "Name", "Amount", "Category", "Date")

expense_table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=12
)

expense_table.heading("ID", text="ID")
expense_table.heading("Name", text="Expense Name")
expense_table.heading("Amount", text="Amount (Rs.)")
expense_table.heading("Category", text="Category")
expense_table.heading("Date", text="Date")

expense_table.column("ID", width=50, anchor="center")
expense_table.column("Name", width=200)
expense_table.column("Amount", width=120, anchor="center")
expense_table.column("Category", width=150, anchor="center")
expense_table.column("Date", width=120, anchor="center")

expense_table.pack(padx=10, pady=10, fill="both", expand=True)


# Total Expense
total_label = tk.Label(
    root,
    text="Total Expense: Rs. 0.00",
    font=("Arial", 14, "bold")
)
total_label.pack(pady=10)


# Load Existing Expenses
show_expenses()

# Run Application
root.mainloop()
