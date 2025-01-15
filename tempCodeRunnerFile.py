import sys

class Player:
    def __init__(self, name, currency=400):
        self.name = name
        self.currency = currency 
        self.inventory = {}  

    def __str__(self):
        return f"Player: {self.name}, Currency: ${self.currency}, Inventory: {self.inventory}"

    def buy_item(self, item, quantity, price_per_unit):
        """Try to buy an item if the player has enough money"""
        total_price = price_per_unit * quantity
        if self.currency >= total_price:
            self.currency -= total_price
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"{self.name} purchased {quantity} {item}(s). Remaining currency: ${self.currency}")
        else:
            print(f"{self.name} does not have enough currency to buy {quantity} {item}(s). Need ${total_price - self.currency} more.")

class Shop:
    def __init__(self):
        # Adjusted prices and weights for each item
        self.items = {
            "Food": {"price": 10, "weight": 20},  
            "Oxen": {"price": 50, "weight": 1},   
            "Clothes": {"price": 20, "weight": 5}  
        }

    def display_items(self):
        print("\nItems available for purchase:")
        for item, details in self.items.items():
            print(f"{item}: ${details['price']} for {details['weight']} pounds")

    def get_item_choice(self):
        """Let the player choose an item"""
        while True:
            item_choice = input("\nEnter the name of the item you want to buy (or 'exit' to leave the shop): ").strip().lower()
            # Normalize input to match the keys
            if item_choice in [item.lower() for item in self.items]:
                # Return the selected item in its proper format (case-sensitive)
                return next(item for item in self.items if item.lower() == item_choice)
            elif item_choice == "exit":
                return None
            else:
                print("Invalid item. Please choose a valid item or type 'exit'.")

    def get_quantity_choice(self, item):
        """Let the player choose the quantity to buy"""
        while True:
            try:
                # Get price and weight for the selected item
                price_per_unit = self.items[item]["price"]
                weight_per_unit = self.items[item]["weight"]
                
                # For Oxen, it's per item, others are in pounds
                if item == "Oxen":
                    quantity = int(input(f"How many {item} would you like to buy? "))
                el
