while True:
  print("What sentence do you want rainbow-ising?")
  myString = input(":> ")

  for letter in myString:
    if letter.lower() == "r":
      print('\033[31m', end='') #red
    elif letter.lower() == "b":
      print('\033[34m', end='') #blue
    elif letter.lower() == "g":
      print('\033[32m', end='') #green
    elif letter.lower() == "y":
      print('\033[33m', end='') #yellow
    elif letter.lower() == "p":
      print('\033[35m', end='') #purple
    elif letter.lower() == "c":
      print('\033[36m', end='') #cyan
    elif letter.lower() == "o":
      print('\033[91m', end='') #orange
    elif letter.lower() == " ":
      print('\033[0m', end='')
    print(letter, end="")

  print('\033[0m', end='')
  print("\nDo you want to rainbow-ise another sentence? (y/n)")
  response = input(":> ")
  if response.lower() == "n":
    break
