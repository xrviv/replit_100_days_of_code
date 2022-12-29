print("30 Days Down")
print()

for i in range(1,31):
  print(f"Day {i: <1} of 100")
  feedback = input("How do you feel about this day?: ")
  text = (f"""                   
  
                    \033[0;32mYou thought this day was {feedback: <10}\033[0;0m
                    
                    
                    """)
  print(text)
  
