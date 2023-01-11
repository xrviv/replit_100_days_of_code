# OpenAI GPT3 Assisted Code
mokedex = {}

def prettyPrint():
  print()
  print("------------------------------------------------------")
  print(f"{'Name':<10} || {'Type':^7} | {'Special Move':^15} | {'HP':^5} | {'MP':^5}")

  for name, info in mokedex.items():
    print(f"{name:<10} || {info['type']:^7} | {info['Special Move']:^15} | {info['HP']:^5} | {info['MP']:^5}")

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

while True:
  print()
  print("-------------------")
  name = input("Beast Name: ")
  type = input("Type: ")
  move = input("Special Move: ")
  hp = input("HP: ")
  mp = input("MP: ")
  print("-------------------")
  mokedex[name] = {"type": type, "Special Move": move, "HP": hp, "MP": mp}
  add = input("Would you like to input another one? (Yes/No) > ")
  if add.lower().startswith('y'):
    continue
  elif add.lower().startswith('n'):
    see = input("Would you like to print the Mokedex you created? (Yes/No) >")
    if see.lower().startswith('y'):
      prettyPrint()
      break
    elif see.lower().startswith('n'):
      print("Okay. Quitting program.")
      break