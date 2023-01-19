#OpenAIGPT3 Assisted code

import os
import time

def add():
    try:
        os.system("clear")
        print()
        inventory = input("Add an item in inventory > ").title()
        f = open("inventory.txt", "a+")
        f.write(inventory + "\n")
        f.close()
    except FileNotFoundError:
        open("inventory.txt", "w")
        add()

def show():
    try:
        f = open("inventory.txt", "r")
        inventory = f.read().splitlines()
        f.close()
        print("Your Inventory Has:")
        for item in set(inventory):
            print(f"{item:<12}  {inventory.count(item)}")
        time.sleep(2)
        print()
    except FileNotFoundError:
        os.system("clear")
        print("File not found, create file? (y/n) ")
        choice = input()
        if choice == "y":
            open("inventory.txt", "w")
        else:
            print("Exiting program.")
            exit()

def remove():
    try:
        f = open("inventory.txt", "r")
        inventory = f.read().splitlines()
        f.close()
        os.system('clear')
        print("Your Inventory Has:")
        for item in inventory:
            print(f"{item:<12}")
        print()
        item_to_remove = input("Enter the item you want to remove > ").title()
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            f = open("inventory.txt", "w")
            for item in inventory:
                f.write(f"{item}\n")
            f.close()
            os.system('clear')
            print(f"{item_to_remove} has been removed from the inventory.")
        else:
            os.system('clear')
            print(f"{item_to_remove} is not in the inventory.")
    except FileNotFoundError:
        os.system('clear')
        print("File not found, would you like to create the inventory file?(y/n)")
        choice = input()
        if choice == "y":
            open('inventory.txt', 'w')
        else:
            os.system('clear')
            print("Exiting program.")
            exit()

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
        elif choose == "3":
            remove()
        elif choose == "4":
            print("Exiting program.")
            exit()
        else:
            os.system('clear')
            print("Choice not in menu. Please input numbers only.")
            time.sleep(1)
    except FileNotFoundError:
        os.system("clear")
        print("File not found, would you like to create the file? (y/n) ")
        choice = input()
        if choice == "y":
            open("inventory.txt", "w")
        else:
            print("Exiting program.")
            exit()
