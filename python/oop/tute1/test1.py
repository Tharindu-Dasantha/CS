class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return (self.price * self.quantity)
    
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 10000, 3)

print(item1.calculate_total_price())