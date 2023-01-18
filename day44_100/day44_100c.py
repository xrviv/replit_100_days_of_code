# GPT3 Assisted Code

import sys, os
import random

bingo = []
num = []
print("\033c")

def prettyPrint():
    for row in bingo:
        print()
        print("----------------------------")
        print("|{: ^8}|{: ^8}|{: ^8}".format(*row), end="|")
    print()
    print("----------------------------")

def createCard():
    # Initialize the bingo card with random numbers
    numbers = []
    for i in range(8):
        numbers.append(random.randint(1,90))
    numbers.sort()
    global bingo
    bingo = [ [ numbers[0], numbers[1], numbers[2]],
              [ numbers[3], "BINGO", numbers[4]],
              [ numbers[5], numbers[6], numbers[7]]]
    prettyPrint()

# Create and print the bingo card
createCard()

# Start the game
while True:
    exes = 0
    try:
        num = int(input("Next Number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "X"
                os.system('clear')
                prettyPrint()
    for row in bingo:
        for item in row:
            if item=="X":
                exes+=1
    if exes == 8:
        print()
        print(" 🏆BINGO!🏆")
        print()
        break