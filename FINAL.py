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
            if item_choice in [item.lower() for item in self.items]:
                return next(item for item in self.items if item.lower() == item_choice)
            elif item_choice == "exit":
                return None
            else:
                print("Invalid item. Please choose a valid item or type 'exit'.")

    def get_quantity_choice(self, item):
        """Let the player choose the quantity to buy"""
        while True:
            try:
                price_per_unit = self.items[item]["price"]
                weight_per_unit = self.items[item]["weight"]
                
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
        self.players = []  
        self.day = 1
        self.month = 1
        self.currency = 400  

    def get_player_name(self):
        """Ask for the player's name and create a Player object"""
        player_name = input("Enter your name: ").strip()
        player = Player(player_name, self.currency)  
        self.players.append(player)

    def get_companions(self):
        """Ask for companions (up to 3)"""
        print("Now, you can add up to 3 companions.")
        for i in range(1, 4):
            companion_name = input(f"Enter the name of companion {i} (or press Enter to skip): ").strip()
            if companion_name:  
                companion = Player(companion_name, self.currency)  
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
        self.day = 1  
        print(f"\nIt is now Month {self.month}, Day {self.day}!")

    def wild_animal_event(self):
        """Wild animal encounter on Day 5"""
        print("\nDay 5: You encounter a wild animal! It looks dangerous and could attack you.")
        decision = input("Do you want to fight or avoid the animal? (fight/avoid): ").lower()
        
        if decision == "fight":
            survival_chance = random.random()  # 50% chance of survival
            if survival_chance < 0.5:
                print("You bravely fight the animal and survive the encounter!")
            else:
                print("The animal overpowers you. You have perished. Imagine getting beat up by a bear, that sucks. Game Over!")
                sys.exit()  # End the game if the player dies during the fight
        elif decision == "avoid":
            print("You decide to avoid the animal. You safely continue your journey.")
        else:
            print("Invalid input. Please choose 'fight' or 'avoid'.")
            self.wild_animal_event()  # Recurse if invalid input

    def start_game(self):
        """Start the game and print the player and companions"""
        print("\nWelcome to The Oregon Trail!")
        self.get_player_name()
        self.get_companions()

        print("\nYour party has been formed!")
        for player in self.players:
            print(player)

        # Only show shop once before the journey begins
        print("\nIt's time to prepare for the journey! Let's visit the shop.")
        shop = Shop()

        while True:
            print(f"\nTotal Party Currency: ${self.currency}")
            main_player = self.players[0]  
            print(f"\n{main_player.name}'s Shop Menu")

            while True:
                print(f"\nYour current status: {main_player}")
                shop.display_items()

                item_choice = shop.get_item_choice()

                if item_choice is None:
                    print("Exiting the shop. Thank you for visiting!")
                    break
                
                quantity, total_cost = shop.get_quantity_choice(item_choice)
                
                price_per_unit = shop.items[item_choice.capitalize()]["price"]
                if self.currency >= total_cost:
                    self.currency -= total_cost
                    main_player.buy_item(item_choice.capitalize(), quantity, price_per_unit)
                else:
                    print("Not enough total currency to purchase that item.")

            if input("\nDo you want to continue shopping? (yes/no): ").strip().lower() != "yes":
                break

        print("\nIt's now time to choose your path.")
        path_choice = divergent_paths()
        if not path_choice: 
            print("Game Over!")
            return

        while self.month <= 6:
            if self.day == 1:  
                self.skip_to_next_month()

            if self.month == 1 and self.day == 1:  
                print("\nDay 1: The adventure begins!")

            # No shop interactions here, the journey continues without additional shopping.

            if self.day == 7 and self.month == 1:
                self.skip_to_day_7()

            if self.day == 7: 
                if self.month < 6:
                    self.skip_to_next_month()

            if self.month == 5:  # Trigger the wild animal event in Month 5
                self.wild_animal_event()

            self.day = 1  

            if self.month == 2:  # Scenario in month 2
                self.buy_oxen()

            if self.month == 3:  # Lake scenario in month 3
                self.lake()

            if self.month == 4:  # Tragedy in month 4
                self.tragedy()

            if self.month == 6:  # End of journey
                print("Congratulations on completing the journey!")
                break

    def buy_oxen(self):
        """Ask if the player wants to buy oxen at the start of the game"""
        oxen_choice = input("Do you want to buy oxen for your journey? (yes/no): ").lower()
        if oxen_choice == "yes":
            return True  # Player buys oxen
        elif oxen_choice == "no":
            return False  # Player does not buy oxen
        else:
            print("Invalid choice. Please choose 'yes' or 'no'.")
            return self.buy_oxen()  # Recurse if invalid input

    def oxen_event(self, oxen_have):
        """Simulate oxen dying during the journey"""
        if oxen_have:
            print("A sudden storm strikes! One of your oxen has died!")
            replacement = input("Do you want to replace the oxen? (yes/no): ").lower()
            if replacement == "yes":
                print("You managed to replace your oxen. You can continue the journey.")
            elif replacement == "no":
                print("Without your oxen, you struggle to move forward. You cannot continue the journey.")
                print("You have perished. Game Over!")
                sys.exit() 
            else:
                print("Invalid choice. Please choose 'yes' or 'no'.")
                self.oxen_event(True) 
        else:
            print("Without oxen, you face a harsh storm and perish. Game Over!")
            sys.exit()  

    def lake(self):
        """Lake crossing decision"""
        print("You have reached a lake in your third week of the trail. You could either risk your life to cross the lake, or take the safe option and go around the lake, but the trail will be longer.")
        
        decision = input("Do you want to risk crossing the lake? (yes/no): ").lower()
        
        if decision == "yes":
            def survival_chance():
                outcome = random.random()
                if outcome < 0.5:
                    return "Survival"
                else:
                    return "No Survival"
            
            result = survival_chance()
            print(f"Result: {result}")
            
        elif decision == "no":
            print("You chose the safer route. Your journey will take longer.")
            print(f"The trail is now extended by an additional month.")
        else:
            print("Invalid input. Please choose 'yes' or 'no'.")

    def tragedy(self):
        """Tragedy event"""
        if len(self.players) >= 2:
            print("Oh no! The third person you brought on the trip has tragically died.")
            print("This marks the end of their journey.")

def start_screen():
    """Start screen to begin the game"""
    print("\n" + "="*40)
    print("    Welcome to The Oregon Trail!")
    print("="*40)
    print("\nPress ENTER to Start the Adventure")
    print("Press ESC to Exit")
    
    while True:
        user_input = input("\nYour choice: ").strip().lower()
        
        if user_input == "":  # Start the game
            print("\nStarting the game...\n")
            game = Game()  
            game.start_game()  
            break
        elif user_input == "esc":  # Exit the game
            print("\nExiting the game. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid input. Please press ENTER to start or ESC to exit.")

if __name__ == "__main__":
    start_screen()
