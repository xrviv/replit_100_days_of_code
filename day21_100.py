print("Math Game!")

multi = int(input("Name your multiples: ")) 

x = 0
for i in range(1, 11):
  print (i, "x", multi, "= ")
  answer = int(input())
  if answer == i * multi:
    print("That's correct. Good job!")
    x += 1
    continue
  else:
    print("That's incorrect.")
    continue
print ("...")
print("You scored", x, "out of", 10)

