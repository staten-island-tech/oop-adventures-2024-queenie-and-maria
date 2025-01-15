
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
        return True  # Continue the journey if the player survives

    elif decision == "easy":
        print("You take the Easy Path, but as you stroll along, you don't notice the edge of a cliff.")
        print("You accidentally fall off the cliff and perish. Fortune favors the bald, and you are not the bald. Game Over!")
        return False  # Game Over scenario due to death

    else:
        print("Invalid input. Please choose 'hard' or 'easy'.")
        return divergent_paths()  # Repeat the decision if invalid

    return True  # Return True if the journey continues

class Player:
    def __init__(self, name, currency=400):
        self.name = name
        self.currency = currency 
        self.inventory = {"Oxen": 2}  # Default oxen set to 2 at the start

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
            print(f"Not enough currency to buy {quantity} {item}(s). oh. ur poor, that sucks, GET A JOB. You need ${total_price - self.currency} more.")

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

    def start_game(self):
        """Start the game and print the player and companions"""
        print("\nWelcome to The Oregon Trail!")
        self.get_player_name()
        self.get_companions()

        print("\nYour party has been formed!")
        for player in self.players:
            print(player)

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
                 # Ask if player wants to buy oxen, skip if invalid
                quantity, total_cost = shop.get_quantity_choice(item_choice)
                
                price_per_unit = shop.items[item_choice.capitalize()]["price"]
                if self.currency >= total_cost:
                    self.currency -= total_cost
                    main_player.buy_item(item_choice.capitalize(), quantity, price_per_unit)
                else:
                    print("Not enough total currency to purchase that item. UR BROKE, get a job.")

            if input("\nDo you want to continue shopping? (yes/no): ").strip().lower() != "yes":
                break

        print("\nIt's now time to choose your path.")
        path_choice = divergent_paths()
        if not path_choice:  # If the player dies, exit the game
            print("Game Over!, How do u die before GTA 6")
            return  # End the game if the player perishes on the path

        # Continue with the game logic if the player survives
        print("You continue your journey. Let's proceed with further events.")
        
        while self.month <= 6:
            if self.day == 1:  
                self.skip_to_next_month()

            if self.month == 1 and self.day == 1:  
                print("\nDay 1: The adventure begins!")

            if self.day == 2:  # Event on Day 2: Oxen Death
                self.oxen_death_event()

            if self.day == 5:  # Event on Day 5: Wild Animal Encounter
                self.wild_animal_event()

            for player in self.players:
                if player == self.players[0]:  
                    print(f"\n{player.name}'s Shop Menu")

                    while True:
                        print(f"\nYour current status: {player}")
                        shop.display_items()

                        item_choice = shop.get_item_choice()

                        if item_choice is None:
                            print("Exiting the shop. Thank you for visiting!")
                            break
                        
                        quantity, total_cost = shop.get_quantity_choice(item_choice)
                        
                        player.buy_item(item_choice.capitalize(), quantity, price_per_unit)

            if self.day == 7 and self.month == 1:
                self.skip_to_day_7()

            if self.day == 7: 
                if self.month < 6:
                    self.skip_to_next_month()

            self.day = 1  

            if self.month == 2:  # Scenario in month 2
                self.buy_oxen()

            if self.month == 3:  # Lake scenario in month 3
                self.lake()

            if self.month == 4:  # Tragedy in month 4
                self.tragedy()

            if self.month == 6:  # End of journey
                print("Congratulations on completing the journey, u survived. I guess.!")
                break

    def oxen_death_event(self):
        """Day 2 Oxen Death Event"""
        print("\nDay 2: Ur oxen ate their own poop, they died to hipotitous. Ur oxen ate somone elses poop, hippotitous!")
        if self.players[0].currency >= 100:  # Check if player has enough money to buy oxen
            decision = input("Do you want to buy 2 new oxen for $100? (yes/no): ").lower()
            if decision == "yes":
                self.players[0].currency -= 100
                self.players[0].inventory["Oxen"] += 2
                print("You have successfully purchased 2 new oxen!")
            elif decision == "no":
                print("You chose not to replace the oxen.")
                print("You now have fewer oxen to continue the journey.")
        else:
            print("You do not have enough currency to replace the oxen!")
            print("You must continue your journey with fewer oxen.")
    
    def wild_animal_event(self):
        """Wild animal encounter on Day 5"""
        print("\nDay 5: You encounter a wild animal! It looks dangerous and could attack you.")
        decision = input("Do you want to fight or avoid the animal? (fight/avoid): ").lower()
        
        if decision == "fight":
            survival_chance = random.random()  # 50% chance of survival
            if survival_chance < 0.5:
                print("You bravely fight the animal and survive the encounter!")
            else:
                print("The animal overpowers you. You have perished. IMagine getting beat up by a bear, that sucks. Game Over!")
                sys.exit()  # End the game if the player dies during the fight
        elif decision == "avoid":
            print("You decide to avoid the animal. You safely continue your journey.")
        else:
            print("Invalid input. Please choose 'fight' or 'avoid'.")
            self.wild_animal_event()  # Recurse if invalid input

