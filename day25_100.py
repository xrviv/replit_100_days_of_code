print("⚔️ Character Stats Generator ⚔️")
print("Made with some help from OPENAI ChatGPT")

import random

def diceRoll(number):
  return random.randint(1, number)
  
def generateHealthStats():
  sixSidedDice = diceRoll(6)
  eightSidedDice = diceRoll(8)
  return sixSidedDice * eightSidedDice

while True:
  charName = input("Name your warrior: ")
  healthStats = generateHealthStats()
  print("Their health is: ", healthStats)
  repeat = input("Would you like to create a new random character?: (y/n)")
  if repeat == "n":
    break
