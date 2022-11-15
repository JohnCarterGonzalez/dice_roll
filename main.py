import random
import time

print("Welcome to your (maybe) dice rolling generator.")
print("""
      The game will ask you to define yourself as a player then pit you against
      the computer and roll the dice. 
      """)

def dice():
    player_roll = random.randint(1,6)
    print(f"You rolled an {player_roll}")

    ai = random.randint(1,6)
    print("The computer rolls.....")
    time.sleep(2)
    print(f"The computer rolled a {ai}")

    if player_roll > ai:
        print("You have won!")
    elif player_roll == ai: 
        print("Its a tie.")
    else:
        print("The computer has won!")


while True: # Main game loop, init the game 
    print("Press 'Enter' to roll your dice.")
    roll = input()
    dice()
    choice = input("Would you like to continue? (y/n)")
    if choice == "y":
        dice()
    elif choice == "n":
        print("Thanks for playing.")
        break
    else:
        print("Sorry I didnt understand that, please try again.")

