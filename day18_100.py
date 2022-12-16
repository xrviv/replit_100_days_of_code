print("One-Million-To-One")

guessCounter = 1
number = 777777

while True:

  guess = int(input("Please guess a number between 1 to 1000000: "))
  
  if guess == number:
    print()
    print("Holy Cow! You guessed it right!")
    break
  elif guess < 0:
    print()
    print("Guh")
    break
  elif guess < number:
    print()
    print("Guess Number #", guessCounter)
    print("Your guess is \u001b[36mlower\u001b[0m than the number. Guess again!")
    guessCounter += 1
    continue
  elif guess > number:
    print()
    print("Guess Number #", guessCounter)
    print("Your guess is \u001b[36mhigher\u001b[0m than the number. Guess again!")
    guessCounter += 1
    continue
  elif guess < 0:
    print()
    print("Guh")
    break
  else:
    print("Guess Number #", guessCounter)
    print("Please input a number between 1 to 1000000")


