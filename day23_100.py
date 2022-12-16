print("Replit Login System")
print()
def inputLogin():
  while True:
    print()
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username == "david" and password == "baldies4life":
      print("------------------")
      print("Welcome to Replit!")
      print("------------------")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      print()
    
inputLogin()
