import csv
from pathlib import Path
from models.expense import Expense


def export_to_csv(expenses: list[Expense], path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        if not expenses:
            print("No expenses to export")
            return
        else:
            writer = csv.DictWriter(f, expenses[0].to_dict().keys())
            writer.writeheader()
            for e in expenses:
                writer.writerow(e.to_dict())
