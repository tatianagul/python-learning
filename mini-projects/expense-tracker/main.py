from pathlib import Path

from data_io import load_file, save_expenses
from expense_converter import convert_to_dict, convert_to_expense
from expense_actions import add_expense
from expense_input import expense_input
from csv_export import export_to_csv
from zip_backup import backup_to_zip

DATA_DIR = Path("data")
MAIN_FILE = Path("data/expenses.json")
CSV_PATH = Path("exports/expenses.csv")
ZIP_PATH = Path("backups/expenses_backup.zip")


# LOAD DATA
expenses_data = load_file(MAIN_FILE)

# CONVERT DATA TO EXPENSE
expenses_list = convert_to_expense(expenses_data)


while True:
    print("1. Add expense")
    print("2. Export expenses to CSV")
    print("3. Create ZIP backup")
    print("4. Exit")
    print()

    choice = input("Choose option: ")
    print()

# ADD EXPENSE
    if choice == "1":
        new_expense = expense_input()
        add_expense(expenses_list, new_expense)
        expenses_data = convert_to_dict(
            expenses_list)   # CONVERT EXPENSES TO DATA
        save_expenses(expenses_data, MAIN_FILE)   # SAVE DATA
        print()
        print("Expense added")
        print()

# EXPORT TO CSV
    elif choice == "2":
        export_to_csv(expenses_list, CSV_PATH)
        print("CSV exported")
        print()

# CREATE BACKUP
    elif choice == "3":
        backup_to_zip(DATA_DIR, ZIP_PATH)
        print("Backup created")
        print()

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid option, try again")
