# OpenAI helped me with this. 

def color_text(word, color):
  
  if color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "green":
    print("\033[32m", word, sep="", end="")
  elif color == "cyan":
    print("\033[36m", word, sep="", end="")
  else:
    print("Color is not valid")
  print("\033[0m", end="")

print("Super Subroutine")
print()
print("With my new program I can just call", end=" ")
color_text("and", "red")
print(" and that word will appear in the color I set it to.")
print()
print("With no", end=" ")
color_text("weird gaps.", "cyan")
print()
print("Epic.")
