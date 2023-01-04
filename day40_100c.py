def colorChange(color):
  if color=="blue":
    return ("\033[34m")
  elif color=="white":
    return ("\033[0m")
  elif color=="green":
    return("\033[032m")

name = input(f"{colorChange('blue')}Name: {colorChange('white')}")
dob = input(f"{colorChange('blue')}Date of Birth: {colorChange('white')}")
tel = input(f"{colorChange('blue')}Telephone: {colorChange('white')}")
email = input(f"{colorChange('blue')}Email: {colorChange('white')}")
address = input(f"{colorChange('blue')}Address: {colorChange('white')}")

myUser = {"name" : name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print("Here's your contact card")
print()
print(f"{colorChange('white')}Name: {colorChange('green')}{myUser['name']}")
print(f"{colorChange('white')}Date of Birth: {colorChange('green')}{myUser['dob']}")
print(f"{colorChange('white')}Telephone Number: {colorChange('green')}{myUser['tel']}")
print(f"{colorChange('white')}email: {colorChange('green')}{myUser['email']}")
print(f"{colorChange('white')}Address: {colorChange('green')}{myUser['address']}")



