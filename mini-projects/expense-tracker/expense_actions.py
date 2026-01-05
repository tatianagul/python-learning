from models.expense import Expense


def add_expense(expenses_list: list[Expense], expense: Expense):
    expenses_list.append(expense)
