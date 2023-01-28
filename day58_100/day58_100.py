# OpenAI GPT3 Assisted Code

import random, os, time
totalAttempts = 0
os.system('clear')
print(f"Total attempts: {totalAttempts}")
def game():
  attempts = 1
  number = random.randint(1,100)
  print(number)
  while True:
    print(f"attempts: {attempts}")
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      global totalAttempts
      totalAttempts += attempts
      again = input("Play again? (y/n)> ")
      if again == "y":
        game()
      elif again == "n":
        print("Returning to menu")
        menuu()
      break

def menuu():
  while True:
    menu = int(input("1: Guess the random number game\n2: Total Score\n3: Exit\n> "))
    if menu == 1:
      game()
    elif menu == 2:
      print(f"You've had {totalAttempts} attempts")
    elif menu == 3:
      break
    else:
      print("Invalid option. Exiting")
      break

menuu()
