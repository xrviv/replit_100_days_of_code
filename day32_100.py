import random

greetings = ["Hoy", "Hej", "Hei", "Shalom", "Yassas", "Goedendag"]

b = random.choice(greetings)

name = "Bob"
age = 18

message = f"{b}, my name is {name} and I am {age} years old."
print(message)
