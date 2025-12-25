import json
from pathlib import Path

main_file = Path("oop/expense-tracker/data/expenses.json")

if main_file.exists():
    with open(main_file, "r") as file:
        expenses = json.load(file)
else:
    with open(main_file, "w") as file:
        expenses = []
        json.dump(expenses, file)


print(expenses)
