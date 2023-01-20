# OpenAI GPT3 Assisted Code

import os, time

lifeOrg = []
fileExists = False

def prettyPrint():
    print()
    for row in lifeOrg:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()

while True:
    files = os.listdir()
    if "lifeOrg.txt" not in files:
        fileExists == False
        choose = input("lifeOrg.txt not in files. Create lifeOrg.txt? (y/n) > ")
        if choose == "y":
            f = open("lifeOrg.txt", "w")
            fileExists == True
            continue
        else:
            print("Exiting...")
            exit()
    elif "lifeOrg.txt" in files:
        fileExists == True

    with open("lifeOrg.txt", "r") as f:
        lifeOrg = [line.strip().split(" ") for line in f.readlines()]
    os.system("clear")
    print("\t\t🌟Life Organizer🌟")
    print()
    print("\tTODO List Management System")
    print("\tVIEW")
    print()
    time.sleep(0.3)
    print("1: Add")
    time.sleep(0.3)
    print("2: View")
    time.sleep(0.3)
    print("3: Remove")
    time.sleep(0.3)
    print("4: Edit")
    time.sleep(0.3)
    print("5: Save")
    time.sleep(0.3)
    print("6: Quit")
    time.sleep(0.3)
    print()
    menu = input("> ")
    if (menu.strip().lower()[0] == "a" or menu.strip().lower()[0] == "1"):
        print()
        print("ADD A TASK")
        print()
        task = input("What is the task? ")
        due = input("When is it due? ")
        prio = input("What is its priority? (HIGH/MED/LOW) ")
        row = [task, due, prio]
        lifeOrg.append(row)
        with open("lifeOrg.txt", "a") as f:
            f.write(" ".join(row) + "\n")
        if "lifeOrg.txt" not in files:
            fileExists == False
            choose = input("lifeOrg.txt not in files. Create lifeOrg.txt? (y/n) > ")
            if choose == "y":
                f = open("lifeOrg.txt", "w")
                fileExists == True
                continue
            else:
                print("Exiting...")
                exit()
        elif "lifeOrg.txt" in files:
            fileExists == True
            print("Checking for existence of backup folder...")
            if os.path.exists("backup"):
                print("Directory exists")
            else:
                create = input("'backup' directory does not exist. Create? (y/n) > ").lower()
                if create == "y":
                  os.mkdir("backup")
                else:
                  exit()
            print()
            time.sleep(1)
            # Backup Autosave
            with open("lifeOrg.txt", "rb") as src:
                data = src.read()
            with open("backup/backup.txt", "wb") as dst:
                print()
                print("Creating backup file.")
                dst.write(data)
    elif (menu.strip().lower()[0] == "v" or menu.strip().lower()[0] == "2"):
        os.system("clear")
        print("\t\t🌟Life Organizer🌟")
        print()
        print("\tTODO List Management System")
        print()
        time.sleep(0.3)
        print("1: View All")
        time.sleep(0.3)
        print("2: View Priority")
        print()
        viewCho = input("> ")
        if (viewCho.strip().lower()[0] == "a" or viewCho.strip().lower()[0] == "1"):
            os.system("clear")
            print("\t\t🌟Life Organizer🌟")
            print()
            print("\tTODO List Management System")
            print()
            prettyPrint()
            time.sleep(2)
        elif (viewCho.strip().lower()[0] == "p" or viewCho.strip().lower()[0] == "2"):
            print("Enter the priority level you want to view: ")
            print("(HIGH/MEDIUM/LOW)")
            priority_level = input("> ").upper()
            for row in lifeOrg:
                if row[2].upper() == priority_level:
                    print(row)
            time.sleep(2)
    elif (menu.strip().lower()[0] == "r" or menu.strip().lower()[0] == "3"):
        os.system("clear")
        print("\t\t🌟Life Organizer🌟")
        print()
        print("\tTODO List Management System")
        print("\tWhat task do you wish to Remove? ")
        print()
        prettyPrint()
        print()
        task = input("> ")
        items_to_remove = []
        for row in lifeOrg:
            if task in row:
                items_to_remove.append(row)
        for item in items_to_remove:
            lifeOrg.remove(item)
        with open("lifeOrg.txt", "w") as f:
            for row in lifeOrg:
                f.write(" ".join(row) + "\n")
        # Backup Autosave
        with open("lifeOrg.txt", "rb") as src:
            data = src.read()
        with open("backup/backup.txt", "wb") as dst:
            dst.write(data)
    elif (menu.strip().lower()[0] == "e" or menu.strip().lower()[0] == "4"):
        os.system("clear")
        print("\t\t🌟Life Organizer🌟")
        print()
        print("\tTODO List Management System")
        print("\tEdit a task")
        print()
        prettyPrint()
        task = input("Enter the task to edit: ")
        new_task = input("Enter the new task: ")
        new_due = input("Enter the new due date: ")
        new_prio = input("Enter the new priority: ")
        tasks = []
        for i, row in enumerate(lifeOrg):
            if task in row:
                lifeOrg[i] = [new_task,                 new_prio]
        with open("lifeOrg.txt", "w") as f:
            for row in lifeOrg:
                f.write(" ".join(row) + "\n")
# Backup Autosave
        with open("lifeOrg.txt", "rb") as src:
            data = src.read()
        with open("backup/backup.txt", "wb") as dst:
            dst.write(data)
    elif (menu.strip() == "5"):
        with open("lifeOrg.txt", "w") as f:
            for row in lifeOrg:
                f.write(" ".join(row) + "\n")
    elif (menu.strip() == "6"):
        save_choice = input("Do you want to save changes? (yes/no)")
        if save_choice.lower() == 'yes':
            with open("lifeOrg.txt", "w") as f:
                for row in lifeOrg:
                    f.write(" ".join(row) + "\n")
        break

