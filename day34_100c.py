import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index+1}: {listOfEmail[index]}") 
  time.sleep(1)

def spamming():
  os.system("clear") 
  print("Spamming Begins!") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{listOfEmail[index]}") 
    print("🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔🥔")
    print()
    print("""Dear valued customer,

We are writing to offer you the opportunity to purchase the finest potatoes on the market at unbeatable prices. Our potatoes are grown with the utmost care and attention to detail, ensuring that they are of the highest quality and taste. Order now and receive a special discount on your first purchase. Don't miss out on this amazing offer!

Thank you for considering our offer.

Sincerely,
The Potato Company """)
    time.sleep(5)
    os.system("clear")
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
    time.sleep(1)
  elif menu == "4":
    spamming()
  os.system("clear")
