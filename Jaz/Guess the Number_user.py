import random 

#I did a version of this project and the other number game in NINA's UPDATES DIR

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess < random_number: 
            print("Sorry, guess again. Too low. ")
        elif user_guess > random_number: 
            print("Sorry, guess again. Too high. ")
    print(f'Yay, congrats! You have guessed the number {random_number}')

def computer_guess(x):   
    low = 1  
    high = x 
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low 
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1 
        elif feedback == "l":
            low = guess + 1 

    print(f"Yay! The computer had guessed your number, {guess}, correctly!")       

def computer_guess_timed_program


computer_guess(10)

