import random
import time

class Dice:
    def roll(self):
        print("Rolling the dice...\\n")
        
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        time.sleep(0.5)
        print(f"You rolled a {die1} and a {die2}. Total sum is: {total}")
        return total

class Game:
    def __init__(self):
        self.dice = Dice()

    def play(self):
        time.sleep(0.8)
        print("""

        !!! WELCOME TO CRAPS!!!

        --- GAME RULES ---

        1. FIRST ROLL:
            * Roll 7 or 11:  YOU WIN immediately!
            * Roll 2, 3, or 12:  CASINO WINS (Craps!)
            * Roll 4, 5, 6, 8, 9, or 10:  Sets your GOAL number.

        2. SUBSEQUENT ROLLS:
            * Keep rolling to hit your GOAL number again to WIN!
            * If you roll a 7 before hitting your goal, YOU LOSE!

        """)
        time.sleep(1)
        input("Press Enter to make your first roll! ")
        
        first_roll = self.dice.roll()

        if first_roll == 7 or first_roll == 11:
            time.sleep(0.5)
            print("Congratulations! You win on the first roll!")
        elif first_roll == 2 or first_roll == 3 or first_roll == 12:
            time.sleep(0.5)
            print("Craps! The casino wins.")
        else:
            goal_number = first_roll
            time.sleep(0.5)
            print(f"\nYour GOAL number is now: {goal_number}")
            time.sleep(0.5)
            print("Keep rolling until you hit your goal to WIN. If you roll a 7, you LOSE.\n")
            
            while True:
                time.sleep(0.5)
                input("Press Enter to roll again... ")
                next_roll = self.dice.roll()
                
                if next_roll == goal_number:
                    print(f"You hit your goal of {goal_number}! YOU WIN!")
                    break
                elif next_roll == 7:
                    print("Oh no, you rolled a 7! YOU LOSE!")
                    break
                else:
                    print(f"You rolled a {next_roll}. Keep trying to hit your goal of {goal_number}.\n")

my_game = Game()
my_game.play()