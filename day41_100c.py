
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name, value in myDictionary.items():
print(f"{name}: {value}")

if (name == "strength"):
if value > 100: # This nested if wasn't indented properly
  print("Whoa, SO STRONG")
else:
  print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")