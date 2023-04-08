from item import Item


class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity=0):
        pay_rate = 0.7
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Validation
        assert broken_phones >= 0, f"Invalid input"

        # Assign to self object
        self.broken_phones = broken_phones