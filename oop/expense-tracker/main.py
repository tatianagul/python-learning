from pathlib import Path

from data_io import load_file, save_expenses
from expense_converter import convert_to_dict, convert_to_expense
from expense_actions import add_expense
from expense_input import expense_input

DATA_FILE = Path("oop/expense-tracker/data/expenses.json")

# LOAD DATA
expenses_data = load_file(DATA_FILE)

# CONVERT DATA TO EXPENSE
expenses_list = convert_to_expense(expenses_data)


# ADD EXPENSE
new_expense = expense_input()
add_expense(expenses_list, new_expense)

# CONVERT EXPENSES TO DATA
expenses_data = convert_to_dict(expenses_list)

# SAVE DATA
save_expenses(expenses_data, DATA_FILE)
