import os, time
print("🌟Star Wars Name Generator🌟")
print()
print("(As if anybody's going to put in security questions here)")

firstName = input("First name: ")
lastName = input("Last name: ")
maidenMom = input("Mom's maiden surname: ")
cityBorn = input("City of birth: ")

print()
print(f"Your Star Wars name is: {firstName[:3].title()}{lastName[:3].lower()} {maidenMom[:2].title()}{cityBorn[-3:].lower()}") 

print("Please wait for version 2 of this program")
time.sleep(5)
os.system("clear")

print("🌟Star Wars Name Generator v.2🌟")
print()
print("Made with a little help from Chat GPT3")

name = input("""Enter your first and last name, mother's maiden
name and the city where you were born, separated by a space
: """)
w, x, y, z = name.split()  

w1 = w[:3]
x1 = x[:3]
y1 = y[:2]
z1 = z[-3:]

print()
print(f"Your Star Wars name is {w1.title()}{x1.lower()} {y1.title()}{z1.lower()}")
