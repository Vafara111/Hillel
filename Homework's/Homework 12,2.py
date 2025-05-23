class Item:
    def __init__(self, name: str, price: int, description: str, dimensions: str):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user: User):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int):
        self.products[item] = cnt

    def __str__(self):
        result = (f"User: {self.user}\n"
                  f"Items:\n")

        for item in self.products.keys():
            result += item.name + f": {self.products[item]} pcs.\n"
        return result

    def get_total(self) -> int:
        result = 0

        for item in self.products.keys():
            result += item.price * self.products[item]
        return result


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
