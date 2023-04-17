import os, time, random

def add():
	os.system("cls" if os.name == "nt" else "clear")
	idea = input("Idea > ")
	f = open("my.ideas", "a+")
	f.write(f"{idea}\n")
	f.close()
	os.system("clear")
	
def show():
	os.system("cls" if os.name == "nt" else "clear")
	f = open("my.ideas", "r")
	ideas = f.read().split("\n")
	f.close()
	ideas.remove("")
	f.close()
	idea = random.choice(ideas)
	print(idea)
	time.sleep(2)
	os.system("cls" if os.name == "nt" else "clear")

while True:
	os.system("cls" if os.name == "nt" else "clear")
	menu = input("1: Add idea\n2: Show a random idea\n>")
	if menu == "1":
		add()
	else:
		show()
