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
    print("Do you want to view, add, or ") 
    menu = input("edit your to do list? ")
    print()
    if menu == "add":
        item = input("What's next on the Agenda?: ")
        myAgenda.append(item)
        os.system('clear')
    elif menu == "view":
        os.system('clear')        
    elif menu == "edit":
        print()
        item = input("What do you want to edit?: ")
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
