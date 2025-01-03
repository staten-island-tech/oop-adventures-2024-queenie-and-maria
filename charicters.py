class Player:
    def __init__(self, name, job, base):
        self.name = name
        self.job = job
        self.base = base

def make_player():
    x = input("What is the player's name? ")
    y = input("What is the player's job? (Mine Worker, Farmer, Sales Man): ")

    # Validate job
    if y not in ["Mine Worker", "Farmer", "Sales Man"]:
        print("Invalid job. Please choose between 'Mine Worker', 'Farmer', or 'Sales Man'.")
        return None
    
    
    z = input("What is the player's base? ")

    new_player = Player(x, y, z)
    return new_player

# Initialize the data list
data = []

# Create a new player
x = make_player()

# If the player was successfully created, add it to the data list
if x is not None:
    data.append(x.__dict__)

# Print the data to check
print(data)
