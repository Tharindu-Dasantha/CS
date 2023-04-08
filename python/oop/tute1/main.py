class Item:
    def calculate_total_price(self, x, y):
        return x + y

item1 = Item ()
item1.name = "Phone"
item1.price = 100
item1.quantity = 10
item1.calculate_total_price(item1.price, item1.quantity)

item2 = Item ()
item2.name = "Laptop"
item2.price = 10000
item2.quantity = 3
item2.calculate_total_price(item2.price, item2.quantity)

item3 = Item ()
item3.name = "pods"
item3.price = 1000
item3.quantity = 15
item3.calculate_total_price(item3.price, item3.quantity)

