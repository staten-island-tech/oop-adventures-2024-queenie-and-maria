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
            print(f"Purchased {quantity} {item}(s).")
        else:
            print(f"Not enough currency to buy {quantity} {item}(s). You need ${total_price - self.currency} more.")

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
                else:
                    quantity = int(input(f"How many pounds of {item} would you like to buy? "))
                
                if quantity > 0:
                    if item == "Oxen":
                        total_cost = price_per_unit * quantity  # Oxen are bought per unit
                    else:
                        total_cost = price_per_unit * (quantity // weight_per_unit)  # Food and Clothes are per pound
                    return quantity, total_cost
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

class Game:
    def __init__(self):
        self.players = []  # List to store player and companions
        self.day = 1
        self.month = 1

    def get_player_name(self):
        """Ask for the player's name and create a Player object"""
        player_name = input("Enter your name: ").strip()
        player = Player(player_name)
        self.players.append(player)

    def get_companions(self):
        """Ask for companions (up to 3)"""
        print("Now, you can add up to 3 companions.")
        for i in range(1, 4):
            companion_name = input(f"Enter the name of companion {i} (or press Enter to skip): ").strip()
            if companion_name:  
                companion = Player(companion_name)
                self.players.append(companion)
            else:
                break  

    def skip_to_next_month(self):
        """Skip to next month"""
        self.month += 1
        self.day = 1  # Start at the first day of the new month
        print(f"\nIt is now Month {self.month}, Day {self.day}!")

    def start_game(self):
        """Start the game and print the player and companions"""
        print("\nWelcome to The Oregon Trail!")
        self.get_player_name()
        self.get_companions()

        print("\nYour party has been formed!")
        for player in self.players:
            print(player)

        # Announce that it's Day 1
        print("\nIt is Day 1! The adventure begins!")

        shop = Shop()

        # Loop for each month (1-6)
        while self.month <= 6:
            print(f"\nMonth {self.month} begins!")

            for player in self.players:
                print(f"\n{player.name}'s Shop Menu")
                print(f"Your current status: {player}")
                
                # Display available items to buy
                shop.display_items()

                while True:
                    item_choice = shop.get_item_choice()

                    if item_choice is None:
                        print("Exiting the shop. Thank you for visiting!")
                        break

                    quantity, total_cost = shop.get_quantity_choice(item_choice)
                    
                    # Buy the item
                    price_per_unit = shop.items[item_choice.capitalize()]["price"]
                    player.buy_item(item_choice.capitalize(), quantity, price_per_unit)

            # After all players have shopped, skip to next month
            if self.month == 6:
                print("\nGame Over! You've reached the final month of your journey.")
                break  # End the game after Month 6
            
            self.skip_to_next_month()

        print("\nThanks for playing The Oregon Trail! Goodbye.")

def start_screen():
    """Start screen to begin the game"""
    print("\n" + "="*40)
    print("    Welcome to The Oregon Trail!")
    print("="*40)
    print("\nPress ENTER to Start the Adventure")
    print("Press ESC to Exit")
    
    # Wait for user input to start the game or quit
    while True:
        user_input = input("\nYour choice: ").strip().lower()
        
        if user_input == "":  # User presses ENTER to start the game
            print("\nStarting the game...\n")
            game = Game()  # Create a Game instance
            game.start_game()  # Start the game logic
            break
        elif user_input == "esc":  # User types "ESC" to quit the game
            print("\nExiting the game. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid input. Please press ENTER to start or ESC to exit.")

# Run the start screen
if __name__ == "__main__":
    start_screen()
