

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

print("Please Input your Products ")
product_1, product_2, product_3, product_4, product_5= input("Product 1: "), input("Product 2: "), input("Product 3: "), input("Product 4: "), input("Product 5: ")

'''
#buildig classes from the attributes we want
class Products:
    def __init__(self):
        self.product1 = int("Item 1: ")
        self.product2 =
        self.product3 =
        self.product4 =
        self.product5 =
#calling the Product Class
my_products = Products()
pass
'''
print ("Item Quantity")
product_1_quantity, product_2_quantity, product_3_quantity, product_4_quantity, product_5_quantity = 
input(f"Product 1 : {product_1}"), input(f"Product 2: {product_2}"), input(f"Product 3:{product_3} "), input(f"Product 4: {product_4}"), input(f"Product 5: {product_5}")



item1 = Item(product_1, product_1_quantity, 1)
item2 = Item(product_2, product_2_quantity, 1)
item3 = Item(product_3, product_3_quantity, 1)
item4 = Item(product_4, product_4_quantity, 1)
item5 = Item(product_5, product_5_quantity, 1)

print(Item.all)
"""for instance in Item.all:
    print(instance.name)

This is another way that we can format our items"""

#i want to make this code completely get inputs from the user
