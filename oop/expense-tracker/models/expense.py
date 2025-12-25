class Expense:
    def __init__(self, name="", category="", amount=0.0, date="", notes=""):
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date
        self.notes = notes

    def to_dict(self):
        return {"name": self.name,
                "category": self.category,
                "amount": self.amount,
                "date": self.date,
                "notes": self.notes}

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.name}"
