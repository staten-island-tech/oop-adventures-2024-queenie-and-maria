import random
import sys

# Function to ask if the player bought oxen at the start of the game
def buy_oxen():
    oxen_choice = input("Do you want to buy oxen for your journey? (yes/no): ").lower()
    if oxen_choice == "yes":
        return True  # Player buys oxen
    elif oxen_choice == "no":
        return False  # Player does not buy oxen
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        return buy_oxen()  # Recurse if invalid input

# Function to simulate oxen dying during the journey
def oxen_event(oxen_have):
    if oxen_have:
        # If the player has oxen, they may die during the journey
        print("A sudden storm strikes! One of your oxen has died!")
        replacement = input("Do you want to replace the oxen? (yes/no): ").lower()
        if replacement == "yes":
            print("You managed to replace your oxen. You can continue the journey.")
        elif replacement == "no":
            print("Without your oxen, you struggle to move forward. You cannot continue the journey.")
            print("You have perished. Game Over!")
            sys.exit()  # Game over if they don't replace the oxen
        else:
            print("Invalid choice. Please choose 'yes' or 'no'.")
            oxen_event(True)  # Recurse for valid input
    else:
        # If the player has no oxen and they face an event with no oxen, they die
        print("Without oxen, you face a harsh storm and perish. Game Over!")
        sys.exit()  # Game over if they have no oxen and they die

# Function to start the game and interact with the player
def start_game():
    print("Welcome to your journey!")
    
    # Ask if the player wants to buy oxen at the start of the game
    oxen_have = buy_oxen()
    
    # Proceed with the journey
    print("You begin your journey with your supplies.")
    
    # Simulate a scenario where the oxen die
    oxen_event(oxen_have)

# Start the game
start_game()
