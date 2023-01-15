import time, os, random
while True:
  print("""⭐ Random Idea Storage ⭐
  
  1: Add an idea
  2: Load up a random idea
  3: Exit
  """)
  rand = input("> ")
  print()
  
  if rand == "1":
    f = open("my.ideas", "a+")
    idea = input("Let's have it! > ")
    f.write(idea + '\n')
    print("Writing file.")
    f.close()
    os.system('clear')
    another = input("Would you like to add another? > ").lower()[0]
    if another == "y":
      continue
    else:
      option = input("Would you like to quit? (y/n) > ")
      if option == "y":
        time.sleep(.5)
        print("Exiting")
        break
      else:
        continue
  elif rand == "2":
    loadSub = input("""Loading Ideas
    
    1: Load the entire list
    2. Load a random idea
    
    > """)
    if loadSub == "1":
      f = open("my.ideas", "r")
      content = f.read()
      os.system('clear')
      print(content)
      time.sleep(3)
      continue
    elif loadSub == "2":
      f = open("my.ideas", "r")
      f.seek(0)
      lines = f.readlines()
      if len(lines) > 0:
          random_line = random.choice(lines)
          print("----RANDOM IDEA----")
          print()
          print(f"\t{random_line:^10}")
          print("-------------------")
          print()
  elif rand == "3":
    print("You chose to exit.")
    time.sleep(1)
    print("Exiting")
    break
  else:
    print("Invalid Option")
    option = input("Would you like to quit? (y/n) > ")
    if option == "y":
      exit()
    else:
      continue
