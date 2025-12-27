from models.expense import Expense


def expense_input() -> Expense:
    name = input("Expense name: ")
    category = input("Expense category: ")
    amount = float(input("Expense amount: "))
    date = input("Expense date (format DD.MM.YYYY): ")
    notes = input("Notes: ")
    new_expense = Expense(name, category, amount, date, notes)
    return new_expense
