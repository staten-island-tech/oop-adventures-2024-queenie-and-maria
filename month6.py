import random
import sys

# Function to simulate the passage of months
def journey_months(lake_choice):
    # Determine when the characters will survive based on their choice
    if lake_choice == "cross":
        print("You crossed the lake, and after facing many challenges, you survive the journey by the 6th month.")
        survival_month = 6
    else:
        print("You took the safer route around the lake, and after a longer journey, you survive the journey by the 7th month.")
        survival_month = 7

    print(f"Survival reached in month {survival_month}.")
    return survival_month
print("Congratulations on completing the journey!")

