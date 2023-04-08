class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return (self.price * self.quantity)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 10000, 3)

# print(Item.pay_rate) # This is how we acsess class attributes

print(Item.__dict__) # All the attributes for the class  level
print(item1.__dict__) # All the attributes for the instance level

item1.apply_discount()

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7 # To change the default class attribute value
item2.apply_discount()

