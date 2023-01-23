# OpenAI GPT3 Assisted Code
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
choose = "y"
while choose == "y":
    print()
    print("🌟Factorial Finder🌟")
    print()
    user_input = int(input("Input a number > "))
    factorial_of_user_input = factorial(user_input)
    print(f"The factorial of", user_input, "is", factorial_of_user_input)
    choose = input("Repeat:? (y/n) > ")
    if choose == "y":
        continue
    else:
        break