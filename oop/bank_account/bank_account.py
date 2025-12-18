from datetime import datetime


class BankAccount:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.transaction = []

    def deposit(self, amount):
        if amount <= 0:
            print("Error. Wrong amount")
        else:
            self.balance += amount
            text = BankAccount.format_transaction(
                "deposit", amount, self.currency)
            self.transaction.append(text)

    def withdraw(self, amount):
        if amount <= 0:
            print("Error. Wrong amount")
        elif amount > self.balance:
            print("Insufficiant funds")
        else:
            self.balance -= amount
            text = BankAccount.format_transaction(
                "withdraw", amount, self.currency)
            self.transaction.append(text)

    def get_balance(self):
        return f"{self.owner}, your balance: {self.balance} {self.currency}"

    def transactions(self):
        return "\n".join(self.transaction)

    @staticmethod
    def format_transaction(operation, amount, currency):
        date = datetime.now().strftime("%d-%m-%Y")

        if operation == "deposit":
            sign = "+"
            name = "Deposit"
        elif operation == "withdraw":
            sign = "-"
            name = "Withdraw"
        else:
            raise ValueError("Unknown operation")

        return f"{date} | {name} | {sign}{amount} {currency}"


account_01 = BankAccount("Svetlana", 500, "USD")
account_02 = BankAccount("Maria", 1000, "EUR")

print(account_01.get_balance())  # Svetlana, your balance: 500 USD

account_01.deposit(50)
account_01.deposit(50)
account_01.withdraw(40)

print(account_02.get_balance())  # Maria, your balance: 1000 EUR
account_02.withdraw(100)
print(account_02.get_balance())  # Maria, your balance: 900 EUR

print(account_01.get_balance())  # Svetlana, your balance: 560 USD
print(account_01.transactions())
# 14-12-2025 | Deposit | +50 USD
# 14-12-2025 | Deposit | +50 USD
# 14-12-2025 | Withdraw | -40 USD
