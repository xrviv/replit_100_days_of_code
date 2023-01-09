# OpenAI GPT3 Assisted Code

import os, time

lifeOrg = []


def prettyPrint():
    print()
    for row in lifeOrg:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()


while True:
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
                    # print(f"{item:^10}", end=" | ")
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
        # oh, wow, this one actually worked.
        # for row in lifeOrg:
        #  if task in row:
        #    lifeOrg.remove(row)
        #  else:
        #    print("That task is not in the list of tasks.")
        #    time.sleep(2)
        #    break
    elif (menu.strip().lower()[0] == "e" or menu.strip().lower()[0] == "4"):
        os.system("clear")
        print("\t\t🌟Life Organizer🌟")
        print()
        print("\tTODO List Management System")
        print("\tWhat task do you wish to EDIT? ")
        print()
        prettyPrint()
        print()
        task = input("> ")
        for row in lifeOrg:
            if task in row:
                print("Which field do you want to edit?")
                print("1: Task")
                print("2: Due Date")
                print("3: Priority")
                field = input("> ")
                if field == "1":
                    new_task = input("Enter the new task: ")
                    row[0] = new_task
                elif field == "2":
                    new_due_date = input("Enter the new due date: ")
                    row[1] = new_due_date
                elif field == "3":
                    new_priority = input("Enter the new priority: ")
                    row[2] = new_priority
                else:
                    print("Invalid field choice")
        print()
        print("Updated task list:")
        prettyPrint()
        time.sleep(2)

    prettyPrint()