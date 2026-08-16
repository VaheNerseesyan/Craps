import random
import time

class Dice:
    def roll(self):
        print("Rolling the dice...")
        time.sleep(1) 
        
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        print(f"You rolled a {die1} and a {die2}. Total sum is: {total}")
        return total


my_dice = Dice() 
result = my_dice.roll()