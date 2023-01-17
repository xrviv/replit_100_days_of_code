# OpenAIGPT3 Assisted Code
# Still buggy. Sometimes focuses on the exception rather than running the code.
# Temporary fix is to reload it again.

import os
pizza = []

def prettyPrint():
    print()
    for row in pizza:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()

os.system("clear")
print()

while True:
    try:
        with open("pizza.txt", "r") as f:
            pizza = [line.strip().split(" ") for line in f.readlines()]
        print("🍕 Pizzeria 🍕")
        print()
        print("1: Add Pizza")
        print("2: View Pizza")
        print("3: Exit")
        menu = input("> ")
        if menu == "1":
            name = input("Name: ")
            toppings = input("Toppings: ")
            size = input("Size (s/m/l): ").lower()
            if size == "s":
                size = 10.95
            elif size == "m":
                size = 13.95
            elif size == "l":
                size == 19.95
            while True:
                try:
                    quantity = int(input("Quantity: "))
                    break
                except ValueError:
                    print("Error: Quantity must be an integer")
            total = round(size * quantity, 2)
            row = [name, toppings, size, quantity, total]
            pizza.append(row)
            with open("pizza.txt", "a") as f:
                for item in row:
                    f.write("{:<10}".format(item) + " | ")
                f.write("\n")
        elif menu == "2":
            os.system('clear')
            f = open("pizza.txt", "r")
            pizza = f.read()
            print("NAME: {:<5} TOPPINGS: {:<2} UNIT PRICE: {:<1} QTY: {:<5} TOTAL: {:<10}".format("", "", "", "", ""))
            print(pizza)
        elif menu == "3":
            break
    except:
        print("ERROR: Unable to load. The file may not be created yet.")
        create = input("Create file: pizza.txt? (y/n) > ")
        if create == "y":
            with open("pizza.txt", "w") as file:
                pass
            continue
        else:
            print("Exiting")
            break