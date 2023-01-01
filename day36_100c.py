// String manipulation challenge
// Create a list with no duplicates and output them on a list.

import os, time
nameList = []

def printList():
	print()
	for i in nameList:
		print(i) 
	print()

while True:
	firstName = input("First Name: ").strip().capitalize()
	surName = input("Sur Name: ").strip().capitalize()
	completeName = firstName + " " + surName
	if completeName not in nameList:
		nameList.append(completeName)
	else:
		print("Name already exists")
		printList()
		time.sleep(2)
		os.system('clear')
	printList()
