print ("Fill in the blank lyrics!")
print ("Type in the blank lyrics and see if you are as cool as me.")
print()

counter = 1
while True:
  print("Never going to ______ you up.")
  answer = input("")
  if answer == "give":
    break
  else:
    print("Nope, try again.")  
    counter += 1
print("Well done! It only took you ", counter, "attempts")
  
