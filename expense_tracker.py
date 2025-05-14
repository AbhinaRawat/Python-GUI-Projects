import tkinter as tk
from tkinter import ttk
import csv

expenses = []

# ------------ Functions -------------
def add_expense():
    item = item_entry.get()
    amount = amount_entry.get()

    if item and amount:
        try:
            cost = float(amount)
            expenses.append((item, cost))
            update_table()
            save_to_csv()
            item_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        except ValueError:
            status_label.config(text="Amount must be a number", fg="red")

def update_table():
    for row in tree.get_children():
        tree.delete(row)

    total = 0
    for i, (item, cost) in enumerate(expenses, start=1):
        tree.insert("", "end", values=(i, item, f"${cost:.2f}"))
        total += cost

    total_label.config(text=f"Total: ${total:.2f}")
    status_label.config(text="Expense added successfully!", fg="green")

def save_to_csv():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Amount"])
        writer.writerows(expenses)

# ------------ UI Setup -------------
app = tk.Tk()
app.title("💸 Expense Tracker")
app.geometry("500x500")
app.config(bg="#f5f5f5")

title_label = tk.Label(app, text="Expense Tracker", font=("Helvetica", 20, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

form_frame = tk.Frame(app, bg="#f5f5f5")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Item:", font=("Helvetica", 12), bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky="e")
item_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=20)
item_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Amount ($):", font=("Helvetica", 12), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=20)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(app, text="Add Expense", command=add_expense, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

status_label = tk.Label(app, text="", font=("Helvetica", 10), bg="#f5f5f5")
status_label.pack()

# Table
table_frame = tk.Frame(app)
table_frame.pack()

cols = ("#", "Item", "Amount")
tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=8)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(side="left")
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Total Label
total_label = tk.Label(app, text="Total: $0.00", font=("Helvetica", 14, "bold"), bg="#f5f5f5")
total_label.pack(pady=10)

app.mainloop()
