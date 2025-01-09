import random

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
        return 

    else:
        print("Invalid input. Please choose 'hard' or 'easy'.")
     
        divergent_paths()

divergent_paths()
