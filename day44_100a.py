# First part of the exercise

listOfShame = []

def prettyPrint():
	print()
	for row in listOfShame:
		for item in row:
			print(f"{item:^10}", end=" | ")
		print()
	print()

while True:
	name = input("What is your name? ")
	age = input("What is your age? ")
	pref = input("What is your Computer platform? ")
	row = [name, age, pref]
	listOfShame.append(row)
	exit = input("Exit? (y/n) ")
	if(exit.strip().lower()[0]=="y"):
		break
prettyPrint()