from models.expense import Expense


def convert_to_expense(expenses_data: list[dict]) -> list[Expense]:
    expenses_list = []
    for item in expenses_data:
        expense = Expense(**item)
        expenses_list.append(expense)
    return expenses_list


def convert_to_dict(expenses_list: list[Expense]) -> list[dict]:
    expenses_data = []
    for expense in expenses_list:
        expenses_data.append(expense.to_dict())
    return expenses_data
