import random                      #random will generate the random number in every time 
choice= random.randint(0,11)       #randint will generate the random number in int datatype within the range we provided (1,11)
user_guess= int(input("Enter your guess number between 1 to 10: "))
print("The number you guessed is:", user_guess)
print("The computer hardcore number is :", choice)
def guess_game(n):
  
    if n > choice:
        print("Your choice is greater than the choice done by computer")
    elif n== choice:
        print("You Guess is correct")
    else:
        print("Your choice is lesser than the choice done by the computer")
guess_game(user_guess)