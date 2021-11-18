# Author:         Anthony Segura
# ULID/Section:   C00441031 / CMPS150-002
# Lab #5

import random

# set your guess to rock
my_guess = 2
print("My guess: Rock", my_guess)

# get the random guess for the computer using random.randint(1,3)
computer_guess = random.randint(1,3)

# using if, if/else or if/elif/else statements
# play a round of paper/rock/scissors and determine a winner,
# or if it is a tie
if computer_guess == 1:
    print("Computer guess: Paper 1\nPaper covers a rock ... Computer wins!")
elif computer_guess == 3:
    print("Computer guess: Scissors 3\nRock crushes scissors ... I win!")
else:
    print("Computer guess: Rock 2\nIt is a tie!")
