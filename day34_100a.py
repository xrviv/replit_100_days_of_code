import os, time
listOfEmail = []

def prettyPrint():
	os.system("clear")
	print("List of email")
	print()
	counter = 1
	for email in listOfEmail:
		print(f"{counter}: {email}")
		counter += 1
	time.sleep(1)

while True:
	print("SPAMMER Inc.")
	menu = input("1. Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
	if menu == "1":
		email = input("Email > ")
		listOfEmail.append(email)
	elif menu == "2":
		email = input("Email > ")
		if email in listOfEmail:
			listOfEmail.remove(email)
	elif menu == "3":
		prettyPrint()
	time.sleep(1)
	os.system("clear")
