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
        return True  # Survived the path

    elif decision == "easy":
        print("You take the Easy Path, but as you stroll along, you don't notice the edge of a cliff.")
        print("You accidentally fall off the cliff and perish. Game Over!")
        return False  # Player dies due to falling off a cliff

    else:
        print("Invalid input. Please choose 'hard' or 'easy'.")
        return divergent_paths()  # Repeat the decision if invalid

class Player:
    def __init__(self, name, currency=400):
        self.name = name
        self.currency = currency
        self.inventory = {}

    def __str__(self):
        return f"Player: {self.name}, Currency: ${self.currency}, Inventory: {self.inventory}"

    def buy_item(self, item, quantity, price_per_unit):
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
            return False  # If the player doesn't have enough money
        return True  # Purchase successful

class Shop:
    def __init__(self):
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
        while True:
            item_choice = input("\nEnter the name of the item you want to buy (or 'exit' to leave the shop): ").strip().lower()
            if item_choice in [item.lower() for item in self.items]:
                return next(item for item in self.items if item.lower() == item_choice)
            elif item_choice == "exit":
                return None
            else:
                print("Invalid item. Please choose a valid item or type 'exit'.")

    def get_quantity_choice(self, item):
        while True:
            try:
                price_per_unit = self.items[item]["price"]
                weight_per_unit = self.items[item]["weight"]
                quantity = int(input(f"How many pounds of {item} would you like to buy? "))
                if quantity > 0:
                    return quantity, price_per_unit * quantity
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

class Game:
    def __init__(self):
        self.players = []  # List to store player and companions
        self.currency = 400  # Shared currency for the entire party

    def get_player_name(self):
        player_name = input("Enter your name: ").strip()
        player = Player(player_name, self.currency)  # Use shared currency for the player
        self.players.append(player)

    def get_companions(self):
        print("Now, you can add up to 3 companions.")
        for i in range(1, 4):
            companion_name = input(f"Enter the name of companion {i} (or press Enter to skip): ").strip()
            if companion_name:
                companion = Player(companion_name, self.currency)  # Use shared currency for companions
                self.players.append(companion)
            else:
                break

    def skip_to_day_7(self):
        print("\nSkipping to Day 7...")
    
    def skip_to_next_month(self):
        self.currency += 50  # For example, you can get more currency each month
        print(f"\nIt is now the next month! New balance: ${self.currency}")

    def start_game(self):
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
                print(f"\nYour current status: {main_player}")
                shop.display_items()

                item_choice = shop.get_item_choice()

                if item_choice is None:
                    print("Exiting the shop. Thank you for visiting!")
                    break
                
                quantity, total_cost = shop.get_quantity_choice(item_choice)
                
                if not main_player.buy_item(item_choice.capitalize(), quantity, total_cost):
                    print("You cannot afford this purchase. Game Over!")
                    return

            if input("\nDo you want to continue shopping? (yes/no): ").strip().lower() != "yes":
                break

        print("\nIt's now time to choose your path.")
        path_choice = divergent_paths()
        if not path_choice:  # If the player dies, exit the game
            print("Game Over!")
            return

        print("You continue your journey. Let's proceed with further events.")

        # Check for survival on specific events
        def survival_event():
            outcome = random.random()
            if outcome < 0.5:
                print("Unfortunately, you didn't survive the event. Game Over!")
                return False
            return True
        
        # Simulate an event
        if not survival_event():  # If the player fails the survival event
            return  # End the game

        # Continue with the game if the player survives
        print("You survive the event and move on!")

# Start screen to begin the game
def start_screen():
    print("\n" + "="*40)
    print("    Welcome to The Oregon Trail!")
    print("="*40)
    print("\nPress ENTER to Start the Adventure")
    print("Press ESC to Exit")
    
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
