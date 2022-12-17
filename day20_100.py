print("Input the following: ") 
start = int(input("Start at: "))
end = int(input("End at: "))
increment = int(input("Increment between values: "))

for i in range (start, end, increment):
  print(i)
