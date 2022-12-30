import random

greetings = ["Hoy", "Hej", "Hei", "Shalom", "Yassas", "Goedendag"]
name = ["Bob", "John", "Mary", "Peter", "Sally", "Zoe"]
age = ["18", "22", "24", "26", "28", "30"]

a = random.choice(greetings)
b = random.choice(name)
c = random.choice(age)

age = 18

message = f"{a}, my name is {b} and I am {c} years old."
print(message)
