import sys

class Player:
    def __init__(self, name, currency=400):
        self.name = name
        self.currency = currency  # Starting currency
        self.inventory = {}  # Inventory stores items and their quantities

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
        # Define items and their prices (price per unit for 20 pounds)
        self.items = {
            "Food": 10,  # $10 per 20 pounds
            "Medicine": 15,  # $15 per 20 pounds
            "Ammunition": 25  # $25 per 20 pounds
        }

    def display_items(self):
            try:
                quantity = int(input("How many 20-pound units would you like to buy? "))
                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")


class Game:
    def __init__(self):
        self.players = []  # List to store player and companions

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
            if companion_name:  # If a name is entered, add a companion
                companion = Player(companion_name)
                self.players.append(companion)
            else:
                break  # Stop if the user presses Enter without entering a name

    def start_game(self):
        """Start the game and print the player and companions"""
        print("\nWelcome to The Oregon Trail!")
        self.get_player_name()
        self.get_companions()

        print("\nYour party has been formed!")
        for player in self.players:
            print(player)

        # Create a shop instance
        shop = Shop()

        # Main shopping loop
        for player in self.players:
            print(f"\n{player.name}'s Shop Menu")

            while True:
                # Show player status
                print(f"\nYour current status: {player}")
                
                # Display shop items
                shop.display_items()

                # Let the player choose an item
                item_choice = shop.get_item_choice()

                if item_choice is None:
                    print("Exiting the shop. Thank you for visiting!")
                    break
                
                # Get the quantity the player wants to buy
                quantity = shop.get_quantity_choice()
                
                # Buy the item
                price_per_unit = shop.items[item_choice.capitalize()]  # Capitalize item to match keys
                player.buy_item(item_choice.capitalize(), quantity, price_per_unit)


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


