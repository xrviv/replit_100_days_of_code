# Add or Remove entries

listOfShame = []

def prettyPrint():
	print()
	for row in listOfShame:
		for item in row:
			print(f"{item:^10}", end=" | ")
		print()
	print()

while True:
  menu = input("Add or Remove? ")
  if(menu.strip().lower()[0]=="a"):
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your Computer platform? ")
    row = [name, age, pref]
    listOfShame.append(row)
  else:
    # name = input("What is the name of the record to delete? ")
    # for row in lifeOrg:
    #  if name in row:
    #    lifeOrg.remove(name)
    
    for row in listOfShame:
     if name in row:
       listOfShame.remove(row)
  prettyPrint()