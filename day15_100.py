exit = ""
while exit != "yes":
  print("Sheep, Cow, Donkey, Horse, Axolotl")
  wantAnimal = input("What animal do you want?: ")
  if wantAnimal == "Cow":
    print("A 🐮 goes Moo.")
  elif wantAnimal == "Horse":
    print("A 🐴 goes 'Neigh!' ")
  elif wantAnimal == "Sheep":
    print("A 🐑 goes 'Baaah!' ")
  elif wantAnimal == "Donkey":
    print("A Donkey goes 'Hee Haw!' ")
  elif wantAnimal == "Axolotl":
    print("An 🦎 goes 'Muhahaha' ")
  else:
    print("Animal not found OR")
    print("Please capitalize the first letter.")
  print("--------------")
  exit = input("Exit? (Yes/No): ")
