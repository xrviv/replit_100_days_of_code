print("MY HAPPY LOGIN SYSTEM")
print()
userLogin = input("Username > ")
userPass = input("Password > ")
if userLogin == "Mark" and userPass == "1234":
	print("Hello", userLogin, ". It is a very pleasant day, wouldn't you think?	Thank you for logging in. We await your feedback on a variety of matters.")
elif userLogin == "Jane" and userPass == "password123":
	print("Hello Jane. How are you doing? We hope that you are more productive today, so we prepared a bunch of stuff that will make you happy.")
elif userLogin == "Jo" and userPass == "donkeys":
	print("Hello Jo. Hey, hey, hey. This is a personalized message specially written for you. We're glad you're on board.")
else:
	print("Sorry, we don't know who you are or your password doesn't match. Please login again or register.")
