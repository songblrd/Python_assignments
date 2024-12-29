# Project: Assignment #2
# Purpose: Menus, Math and Functions
# Revision History: Date created Oct 4th 2024 by Marianne Moyo



import random

def addition_game():
 rand_int1 = random.randint(1,10)
 rand_int2 = random.randint(1, 10)
 answer = rand_int1 + rand_int2
 input_answer = int(input(f"{rand_int1} + {rand_int2} = "))
 while True:
     if  input_answer != answer:
         print("Try again")
     else:
        print("You got it")


def manipulating_values():
 starting_number = int(input("Please enter a number: "))
 for i in range(starting_number + 1, starting_number + 11, 1):
    if i % 2 == 0:
         i = i * 3
    else:
         i = i * 4
    print(i, end=" ")

def repeat_math_game():
    while play_again:
        addition_game()
        play_again = str(input("Would you like to play again? \n Yes/No"))
        if play_again == "Yes":
            play_again = True




