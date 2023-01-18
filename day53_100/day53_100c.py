debugMode = True
import os
import time

inventory = []
    
def add():
    os.system("clear")
    print()
    inventory = input("Add an item in inventory > ").title()
    f = open("/day53_100/inventory.txt", "a+")
    f.write(f"{inventory}\n")
    f.close()

def show():
    f = open("/day53_100/inventory.txt", "r")
    inventory = f.read()
    print(inventory)
    f.close()
    time.sleep(2)

def menu():
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    print("1: Add")
    print("2: View")
    print("3: Remove")
    print("4: Exit")
    print()
    
while True:
    try:
        menu()
        choose = input("> ")
        if choose == "1":
            add()
        elif choose == "2":
            show()
        elif choose == "4":
            print("Exiting program.")
            exit()
        else:
            os.system('clear')
            print("Choice not in menu. Please input numbers only.")
            time.sleep(1)                                               
    except:
        print("An error occurred.")
        print()
    
prettyPrint()