import random
import sys

# Divergent Paths Function (Day 1)
def divergent_paths():
    print("You come to a fork in the trail. Two paths lie ahead:")
    print("1. The Hard Path, a treacherous, narrow trail that could be dangerous but might offer rewards.")
    print("2. The Easy Path, a gentle and wide trail that seems much safer, but it has its own dangers.")
    
    decision = input("Which path will you take? (hard/easy): ").lower()
    
    if decision == "hard":
        print("You bravely take the Hard Path. It's difficult, but you manage to navigate through it.")
        print("You survive the journey and continue on your way. Well done!")
   
    elif decision == "easy":
        print("You take the Easy Path, but as you stroll along, you don't notice the edge of a cliff.")
        print("You accidentally fall off the cliff and perish. Game Over!")
        return False  # Game over scenario due to death

    else:
        print("Invalid input. Please choose 'hard' or 'easy'.")
        return divergent_paths()  # Repeat the decision if invalid

    return True  # Return True if the journey continues

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
        self.currency = 400  # Shared currency for the entire party

    def get_player_name(self):
        """Ask for the player's name and create a Player object"""
        player_name = input("Enter your name: ").strip()
        player = Player(player_name, self.currency)  # Use shared currency for the player
        self.players.append(player)

    def get_companions(self):
        """Ask for companions (up to 3)"""
        print("Now, you can add up to 3 companions.")
        for i in range(1, 4):
            companion_name = input(f"Enter the name of companion {i} (or press Enter to skip): ").strip()
            if companion_name:  
                companion = Player(companion_name, self.currency)  # Use shared currency for companions
                self.players.append(companion)
            else:
                break  

    def skip_to_day_7(self):
        """Skip to day 7"""
        print("\nSkipping to Day 7...")
        self.day = 7
        print(f"\nIt is now Day {self.day}!")

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

        # Shopping phase before trail selection
        print("\nIt's time to prepare for the journey! Let's visit the shop.")
        shop = Shop()

        # Loop for shopping only for the main player
        while True:
            print(f"\nTotal Party Currency: ${self.currency}")
            main_player = self.players[0]  # Only the first player (main player) can buy items
            print(f"\n{main_player.name}'s Shop Menu")

            while True:
                # Show player status
                print(f"\nYour current status: {main_player}")
                
                # Display shop items
                shop.display_items()

                # Let the main player choose an item
                item_choice = shop.get_item_choice()

                if item_choice is None:
                    print("Exiting the shop. Thank you for visiting!")
                    break
                
                quantity, total_cost = shop.get_quantity_choice(item_choice)
                
                # Buy the item
                price_per_unit = shop.items[item_choice.capitalize()]["price"]
                if self.currency >= total_cost:
                    self.currency -= total_cost
                    main_player.buy_item(item_choice.capitalize(), quantity, price_per_unit)
                else:
                    print("Not enough total currency to purchase that item.")

            if input("\nDo you want to continue shopping? (yes/no): ").strip().lower() != "yes":
                break

        # After shopping, proceed with divergent paths
        print("\nIt's now time to choose your path.")
        path_choice = divergent_paths()
        if not path_choice:  # If the player dies, exit the game
            print("Game Over!")
            return

        # Day 1 to Day 7, then Month 1 to Month 6
        while self.month <= 6:
            if self.day == 1:  # Starting a new month
                self.skip_to_next_month()

            if self.month == 1 and self.day == 1:  # If it's the start of the game (Day 1)
                print("\nDay 1: The adventure begins!")
            
            # Loop for shopping on each day of the month (still only for the main player)
            for player in self.players:
                if player == self.players[0]:  # Only the main player can shop
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
                        
                        quantity, total_cost = shop.get_quantity_choice(item_choice)
                        
                        # Buy the item
                        price_per_unit = shop.items[item_choice.capitalize()]["price"]
                        player.buy_item(item_choice.capitalize(), quantity, price_per_unit)

            if self.day == 7 and self.month == 1:  # Skip to Day 7 after the first week
                self.skip_to_day_7()

            if self.day == 7:  # Once Day 7 is complete, skip to the next month
                if self.month < 6:  # Move to the next month if we haven't reached Month 6
                    self.skip_to_next_month()

            # Once the month is over, move to the next month
            self.day = 1  # Reset day to 1 for the next month

            print(f"\nThe day is over. It's the end of Month {self.month}, Day {self.day}. Moving on to the next month...\n")

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




        


