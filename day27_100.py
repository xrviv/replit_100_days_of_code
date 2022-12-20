print("⚔️ Character Generator ⚔️")

import random, os, time


def diceRoll(number):
  return random.randint(1, number)
  
def generateHealthStats():
  sixSidedDice = diceRoll(6)
  twelveSidedDice = diceRoll(12)
  return (sixSidedDice * twelveSidedDice)/2 + 10

def generateStrengthStats():
  sixSidedDice = diceRoll(6)
  twelveSidedDice = diceRoll(12)
  return (sixSidedDice * twelveSidedDice)/2 + 12

while True:
  charName = input("Give the first name for the character: ")
  healthStats = generateHealthStats()
  strengthStats = generateStrengthStats()
  charType = input("Choose the Character Type: (Human, Elf, Wizard, Orc): ")
  print()
  os.system('clear')
  time.sleep(1)
  print("Welcome,", charName, "the", charType)
  print("Your initial health is: ", healthStats)
  print("Your initial strength is: ", strengthStats)
  time.sleep(3)
  repeat = input("Would you like to create a new random character?: (y/n)")
  if repeat == "n":
    break
  else:
    os.system('clear')
    continue
