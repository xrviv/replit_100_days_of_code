import random, os

def colorChange(color):
    if color=="cyan":
        return ("\033[36m")
    elif color=="green":
        return("\033[032m")

cs_words = ["algorithm", "programming", "software", "hardware", "data structure", "database", "computer architecture", "artificial intelligence", "machine learning", "cybersecurity"]
rWords = random.choice(cs_words)
correct_guesses = []
guesses = set()

# Set up a variable to keep track of the unguessed letters
unguessed_letters = set(rWords)

# Set up a counter to keep track of the number of wrong guesses
wrong_guesses = 0

# Define the ASCII art for each part of the hangman
hangman_art = [
  "  ________ \n",
  "  ________ \n  |       | \n",
  "  ________ \n  |       | \n  |       O \n",
  "  ________ \n  |       | \n  |       O  \n  |      /|\\ \n",
  "  ________ \n  |       | \n  |       O  \n  |      /|\\ \n  |       | \n",
  "  ________ \n  |       | \n  |       O  \n  |      /|\\ \n  |       | \n  |      / \\ \n",
  "  ________ \n  |       | \n  |       O  \n  |      /|\\ \n  |       | \n  |      / \\ \n / \\ "
]
ans = ""
os.system('clear')
print("🎮 Welcome to My Simple Hangman Game 🎮")
print(f"{colorChange('cyan')}Code generated in part by 🤖 OpenAI GPT3\033[0m")
print("(Sorry, it's still quite buggy: 'spaces' and 'duplicate' bugs.")
while len(unguessed_letters) > 0: 
  print()
  print(f"{colorChange('green')}There's a hidden list of 🔟 ")
  print("Computer Science words.")
  print("The 🤖 has selected one word")
  print("You must guess it by guessing")
  print("the letters one by one!\033[0m")
  print()
  guess = input("Choose a letter: ")
  guess = guess.replace(" ", "")
  print()
  if guess in rWords:
    os.system('clear')
    print("Correct!")
    # Remove the guessed letter from the set of unguessed letters
    # Add correct guesses to list called correct guesses.
    correct_guesses.append(guess)
    unguessed_letters.remove(guess)
    # Create a new string with underscores in place of unguessed letters
    word_with_underscores = ""
    for letter in rWords:
      if letter in unguessed_letters:
        word_with_underscores += "_"
      else:
        word_with_underscores += letter
    print(word_with_underscores)
    ans = word_with_underscores
  elif guess not in rWords:
    print("Incorrect!")
    # Increment the counter for wrong guesses
    wrong_guesses += 1
    # Draw the next part of the hangman
    
    if wrong_guesses < len(hangman_art):
      os.system('clear')
      print(hangman_art[wrong_guesses])
      print(ans)
    else:
      print("=== GAME OVER ===")
      print()
      print(f"The correct word is {colorChange('cyan')}{rWords}")
      print("Try again!")
      print("   /")
      print(""" /\_/\ 
( o.o ) 
 >^<  """)
      break

# Check if the length of unguessed_letters is 0
if len(unguessed_letters) == 0:
  # Check if the correct guesses match rWords
  if "".join(correct_guesses).replace(" ", "") == rWords.replace(" ", ""):
    # Print the success message
    congrats = "You guessed the whole word! Great job!"
    print(f"{colorChange('cyan')}{congrats}")
    print("   /")
    print(""" /\_/\ 
( o.o ) 
 >^<  """)


