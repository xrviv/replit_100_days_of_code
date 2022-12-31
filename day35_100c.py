import os, time
myAgenda = []

def printList():
    for item in myAgenda:
        print(item)
    print()
  
def colorChange(color):
	if color=="red":
		return ("\033[31m")
	elif color=="white":
		return ("\033[0m")
	elif color=="blue":
		return ("\033[34m")
	elif color=="yellow":
		return("\033[033m")
	elif color=="green":
		return("\033[032m")
	elif color=="purple":
		return("\033[035m")

text1 = "     📝 ToDo List Manager 📝"

while True:
    print(f"{colorChange('yellow')}{text1:>5}")
    print(f"{colorChange('white')}")
    print("Do you want to view, add, remove ") 
    menu = input("or edit your to-do list? ")
    print()
    if menu == "add":
        item = input("What's next on the Agenda?: ")
        if item in myAgenda:
            print("-----------------------------------")
            print("That item is already on the agenda.")
            print("Please try again.")
            print()
            print("Restarting...")
            time.sleep(3)
            os.system('clear')
        else:
            myAgenda.append(item)
            os.system('clear')
    elif menu == "view":
        os.system('clear')
    elif menu == "remove":
        print()
        item = input("What do you want to remove?: ")
        print(f"You want to remove: {item} ")
        confirm = input("Are you sure you want to remove this item? (y/n): ")
        if confirm == "y":
            if item in myAgenda:
              myAgenda.remove(item)
              os.system('clear')
              time.sleep(1)        
            else:
              os.system('clear')
              time.sleep(1)
              print()
              print(f"{item} not found")
              print()
        elif confirm == "n":
            print("You selected 'n'")
            print("Restarting")
            time.sleep(2)
            os.system('clear')
        else:
            text2 = "Invalid Option"
            text3 = "Please type in 'y' or 'n' then press ENTER"            
            print()
            print(f"{colorChange('red')}{text2}") 
            print(f"{colorChange('red')}{text3}")
            time.sleep(2)
            os.system('clear')
            print(f"{colorChange('white')}")
    elif menu == "edit":
        print()
        item = input("What do you want to edit?: ")
        print(f"You want to edit: {colorChange('green')}{item} ")
        confirm = input(f"{colorChange('white')}Are you sure you want to edit this item?:{colorChange('green')} (y/n) ")
        if confirm == "y":
            if item in myAgenda:              
              newitem = input(f"{colorChange('white')}What should we replace it with?:{colorChange('green')} ")
              if newitem in myAgenda:
                text4 = "Duplicate entry."
                print()
                print(f"{colorChange('white')}{text4}")
                time.sleep(1)
                os.system('clear')
              else:                
                myAgenda.remove(item)
                item = newitem
                myAgenda.append(newitem)
                os.system('clear')
                time.sleep(1)
                print(f"{colorChange('white')}")
            else:
              os.system('clear')
              time.sleep(1)
              print()
              print(f"{item} not found")
              print()
        elif confirm == "n":
            print("You selected 'n'")
            print("Restarting")
            time.sleep(2)
            os.system('clear')
        else:
            text2 = "Invalid Option"
            text3 = "Please type in 'y' or 'n' then press ENTER"            
            print()
            print(f"{colorChange('red')}{text2}") 
            print(f"{colorChange('red')}{text3}")
            time.sleep(2)
            os.system('clear')
            print(f"{colorChange('white')}")
    else:
      print("Invalid option")
      print("Please try again")
      time.sleep(2)
      os.system('clear')
      continue
    print("           AGENDA")
    print("----------------------------")
    printList()
    print("----------------------------")
