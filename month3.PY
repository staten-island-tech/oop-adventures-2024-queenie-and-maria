import random

def lake():
    # Print the situation
    print("You have reached a lake in your third week of the trail. You could either risk your life to cross the lake, or take the safe option and go around the lake, but the trail will be longer.")
    
    # Ask the user for a decision
    decision = input("Do you want to risk crossing the lake? (yes/no): ").lower()
    
    if decision == "yes":
        # If the player decides to cross the lake, generate a survival chance
        def survival_chance():
            # Generate a random float between 0 and 1
            outcome = random.random()
            
            # If the random number is less than 0.5, return "Survival", else "No Survival"
            if outcome < 0.5:
                return "Survival"
            else:
                return "No Survival"
        
        # Running the survival chance function
        result = survival_chance()
        print(f"Result: {result}")
        
    elif decision == "no":
        # If the player decides not to cross, increase time by one month for taking the longer route
        print("You chose the safer route. Your journey will take longer.")
        time_taken = "additional month"
        print(f"The trail is now extended by {time_taken}.")
    else:
        print("Invalid input. Please choose 'yes' or 'no'.")

# Call the function to run the scenario
lake()
