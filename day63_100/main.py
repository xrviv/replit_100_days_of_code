import myLibrary as lib

print("Choose from the options")
print()
print("1. Idea Generator")
choice = int(input("Choose a number: "))

if choice == 1:
  lib.show()
else:
  quit()

input("Press Enter to exit...")