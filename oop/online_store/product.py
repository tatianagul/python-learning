class Product:
    def __init__(self, id: int, name: str, price: float, amount: int):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def product_is_available(self):
        return self.amount > 0

    def __str__(self):
        return f"{self.name} | id: {self.id} | price: {self.price} | amount: {self.amount}"


class Book(Product):
    def __init__(self, id: int, name: str, author: str, year: int, price: float, amount: int):
        super().__init__(id, name, price, amount)
        self.author = author
        self.year = year


class Electronics(Product):
    def __init__(self, id: int, name: str, brand: str, price: float, amount: int):
        super().__init__(id, name, price, amount)
        self.brand = brand


class Toy(Product):
    def __init__(self, id: int, name: str, age: str, price: float, amount: int):
        super().__init__(id, name, price, amount)
        self.age = age
