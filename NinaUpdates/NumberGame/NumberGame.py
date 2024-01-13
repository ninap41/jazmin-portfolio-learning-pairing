import random 
import re # this is called Regex and it's important to know when mutating strings
import time # for datetime formatting 
from utilities import bcolors #from utilities.py
    
# I extracted out a win function so it's easier to read
def win(random_number):
    print(f'{bcolors.OKGREEN} Yay, congrats! You have guessed the number ({random_number}){bcolors.ENDC}') 
    playAgain = input(f'{bcolors.OKGREEN}Would you like to play again? [ Y / N ]{bcolors.ENDC}')   
    if playAgain.lower() == "y":
        print(f"${bcolors.space}let's make it harder...")
        time.sleep(1)
        print(f"${bcolors.space}...")
        time.sleep(1.5)
        randomNumber(random.randint(1, 999)) # this recursively calls randomNumber so that the game can begin again, but with a bigger number to guess
    elif playAgain.lower() == "n":
        input(f"GoodBye!")    
    else:
        input(f"Lame... later!")    


def randomNumber(max):
    random_number = random.randint(1, max)
    guess = ''
    while guess != random_number:
        guess = input(f"Guess a number between {bcolors.HEADER} 1 {bcolors.ENDC} and {bcolors.HEADER}{max}: {bcolors.ENDC}")
        if any(i.isdigit() for i in guess) is False:  #check for is a digit is in the string
            print(f"{bcolors.FAIL}Sorry, please type a NUMBER{bcolors.ENDC}")
        elif int(re.sub("[^0-9]", "", guess)) > max:
            print(f"{bcolors.FAIL}That number is not between 1-10{bcolors.ENDC}")
        elif int(guess) < random_number: 
            print(f"{bcolors.WARNING}Sorry, guess again. Too low.{bcolors.ENDC} ")
        elif int(guess) > random_number: 
            print(f"{bcolors.WARNING}Sorry, guess again. Too high.{bcolors.ENDC} ")
        else: 
           win(max)  

randomNumber(10)