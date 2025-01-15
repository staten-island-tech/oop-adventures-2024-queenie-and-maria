import random
import sys


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
