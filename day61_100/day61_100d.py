#OpenAI GPT3 Assisted Code

from replit import db
import getpass, os, datetime, time

password = "BananaPie"

def wrongPass():
    print("Incorrect Password. Exiting.")
    exit

def showMenu():
    print()
    print("📖 Welcome to Top Secret Journal")
    print("1: Add diary entry\n2: View Diary entry\n3: Exit")
    print()
    choice = input("> ")
    if choice == "1":
      addEntry()
    if choice == "2":
      viewEntry()
    if choice == "3":
      exit

def addEntry():
    diaryEntry = input("Add an entry > ")
    timestamp = datetime.datetime.now()
    db[timestamp] = diaryEntry
    time.sleep(1)
    os.system("clear")
    showMenu()

def viewEntry():
    keys = list(db.keys())
    keys.sort(reverse=True)
    i = 0
    while i < len(keys):
        print("-------------------------+")
        print(f"{keys[i]}: {db[keys[i]]}")
        print("-------------------------+")
        i += 1
        if i == len(keys):
            break
        view_previous = input("View previous entry? (yes/no) ")
        if view_previous.lower() == "yes":
            continue
        if view_previous.lower() == "no":
            showMenu()
            break

os.system('clear')
passInput = getpass.getpass(prompt='Password: ', stream=None)
if passInput != password:
    wrongPass()
elif passInput == password:
    showMenu()
    