from pathlib import Path
from models.expense import Expense

from data_io import load_file, save_expenses
from expense_converter import convert_to_dict, convert_to_expense

main_file = Path("oop/expense-tracker/data/expenses.json")

# LOAD DATA

expenses_data = load_file(main_file)

# CONVERT DATA TO EXPENSE

expenses_list = convert_to_expense(expenses_data)


# add function
new_expense = Expense("coffee with Sarah", "food", 100, "13.12.2025", "")

expenses_list.append(new_expense)

# CONVERT EXPENSES TO DATA
expenses_data = convert_to_dict(expenses_list)

# SAVE DATA

save_expenses(expenses_data, main_file)
