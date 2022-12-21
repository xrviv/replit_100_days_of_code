print("⚔️ Character Generator ⚔️")

import random, os, time

def diceRoll(number):
  rolls = random.randint(1, number)
  diceRoll = rolls
  return diceRoll
  
def generateHealthStats():
  sixSidedDice = diceRoll(6)
  twelveSidedDice = diceRoll(12)
  healthStats = (sixSidedDice * twelveSidedDice)/2 + 10
  return healthStats

def generateStrengthStats():
  sixSidedDice = diceRoll(6)
  twelveSidedDice = diceRoll(12)
  strengthStats = (sixSidedDice * twelveSidedDice)/2 + 12
  return strengthStats

def battleDamage():
  damage = abs(strengthStats1 - strengthStats2) + 1
  return damage

print()
charName1 = input("Give the name for the first character: ")
charType1 = input("Choose the Character Type: (Human🤺, Elf🧝, Wizard 🧙, Orc👹): ")
print()
generateStrengthStats()
generateHealthStats()
healthStats1 = generateHealthStats()
strengthStats1 = generateStrengthStats()
time.sleep(1)
print("Welcome,", charName1, "the", charType1)
print(charName1, "'s initial health is: ", healthStats1)
print(charName1, "'s initial strength is: ", strengthStats1)
time.sleep(2)
print()
print("Who are they battling?")

print()
charName2 = input("Give the name for the second character: ")
charType2 = input("Choose the Character Type: (Human🤺, Elf🧝, Wizard 🧙, Orc👹): ")
print()
generateStrengthStats()
generateHealthStats()
healthStats2 = generateHealthStats()
strengthStats2 = generateStrengthStats()
time.sleep(1)
print("Welcome,", charName2, "the", charType2)
print(charName2, "'s initial health is: ", healthStats2)
print(charName2, "'s initial strength is: ", strengthStats2)
time.sleep(2)
print()
print("⚔️ Prepare for battle!!! ⚔️")
time.sleep(3)
os.system("clear")
while True:
  print("⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️")
  print()
  battleDamage()
  damage = battleDamage()
  print(charName1, " health: ", healthStats1)
  print(charName2, " health: ", healthStats2)
  print()
  print("⚔️⚔️⚔️⚔️ Rolling ⚔️⚔️⚔️⚔️⚔️")
  result1 = diceRoll(6)
  result2 = diceRoll(6)
  time.sleep(3)
  os.system("clear")
  print("Player1 rolls ", result1)
  print("Player2 rolls ", result2)
  if healthStats1 <= 0:
    print()
    print("🏆 Gameover 🏆")
    print("\033[93m", charName2,"the", charType2, "🥇 Wins!\033[0m")
    print()
    break
  elif healthStats2 <= 0:
    print()
    print("🏆 Gameover 🏆")
    print()
    print("\033[93m", charName1,"the", charType1, "🥇 Wins!\033[0m")
    break
  elif result1 > result2:
    print(charName1, "damages", charName2, "by", damage )
    healthStats2 = healthStats2 - damage
    continue
  elif result1 == result2:
    print("It's a draw.")
    continue
  else:
    print(charName2, "damages", charName1, "by", damage )
    healthStats1 = healthStats1 - damage
    continue
