import tkinter as tk
import csv

expenses = []

def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    if name and amount:
        expenses.append((name, float(amount)))
        update_display()
        save_to_csv()
        name_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

def update_display():
    text_area.delete(1.0, tk.END)
    total = 0
    for item, cost in expenses:
        text_area.insert(tk.END, f"{item}: ${cost:.2f}\n")
        total += cost
    text_area.insert(tk.END, f"\nTotal: ${total:.2f}")

def save_to_csv():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

app = tk.Tk()
app.title("Expense Tracker")

tk.Label(app, text="Item:").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Amount:").pack()
amount_entry = tk.Entry(app)
amount_entry.pack()

tk.Button(app, text="Add Expense", command=add_expense).pack()

text_area = tk.Text(app, height=10, width=40)
text_area.pack()

app.mainloop()
