"""This is a program that takes products in a store as inputs and neatly outputs it as Data(textfile)
This is a one month project

by Chris Liloba
"""


class Item:
    pay_rate = 0.8 #the payrate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity= 0):
        # this is so that the values will never be negative
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})\n"

user_input = input("Input the number of your product: ")
item1 = Item(user_input, 100, 1)
item2 = Item("Laptop", 1000, 1)
item3 = Item("Cable", 100, 1)
item4 = Item("Mouse", 100, 1)
item5 = Item("Keyboard", 100, 1)

print(Item.all)
"""for instance in Item.all:
    print(instance.name)

This is another way that we can format our items"""

#i want to make this code completely get inputs from the user