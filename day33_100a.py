import os
myAgenda = []

def printList():
    for item in myAgenda:
        print(item)
    print()

while True:
    menu = input("Add or Remove?: ")
    print()
    print("====================")
    if menu == "Add":
        item = input("What's next on the Agenda?: ")
        myAgenda.append(item)
// common error myAgenda first, then append, then item inside parenthesis
// attribute error
        os.system('clear')
    elif menu == "Remove":
        print()
        item = input("What do you want to remove?: ")
        if item in myAgenda:
            myAgenda.remove(item)
        else:
            print()
            print(f"{item} not found")
            print()
    else:
      print("Invalid option")
      print("Please try again")
      print("====================")
      os.system('clear')
      continue
    print("           AGENDA")
    print("----------------------------")
    printList()
    print("----------------------------")
