import json
from pathlib import Path
from models.expense import Expense

main_file = Path("oop/expense-tracker/data/expenses.json")

if main_file.exists():
    with open(main_file, "r") as file:
        expenses = json.load(file)
else:
    with open(main_file, "w") as file:
        expenses = []
        json.dump(expenses, file)

expenses_list = []

for item in expenses:
    expense = Expense(**item)
    expenses_list.append(expense)


new_expense = Expense("coffee with Sarah", "food", 100, "13.12.2025", "")

expenses_list.append(new_expense)

expenses_data = []

for exp in expenses_list:
    expenses_data.append(exp.to_dict())


with open(main_file, "w") as file:
    json.dump(expenses_data, file, indent=1)
