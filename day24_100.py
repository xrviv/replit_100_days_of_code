import random

print("Infinity Dice 🎲")

def dice_roll():
  again = "yes"
  while again == "yes":
    dice_roll = random.randint(1, int(sides))
    print("You rolled", dice_roll)
    again = input("Roll again? (yes/no): ")

sides = input("How many sides?: ")
dice_roll()
