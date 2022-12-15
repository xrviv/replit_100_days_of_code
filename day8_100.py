print("Wholesome Positivity Machine")
print()
uName = input("Who are you? ")
uName = uName.capitalize()
print()
print("Hi", uName)
uDay = input("What day of the week is today? ")
uDay = uDay.capitalize()
uAchieve = input("What's your favorite thing? ")
print()

if uDay == "Monday":
  print()
  print("Monday is a great day! Start of the week, broom broom!")
elif uDay == "Tuesday":
  print()
  print("Oh look, the grey skies will turn blue!") 
elif uDay == "Wednesday":
  print()
  print("Let's buy another ice cream!")   
elif uDay == "Thursday":
  print()
  print("What's better than an ice cream cone? 2 ice cream cones!") 
elif uDay == "Friday":
  print()
  print("It's one of those moments, when you're just in the middle.") 
elif uDay == "Saturday":
  print()
  print("I'm good! You're good? It's good that you're goodon this", uDay, ",", uName) 
elif uDay == "Sunday":
  print()
  print("This is better! ") 
else:  
  print("Ummm, sorry, you have to enter in a day, ie. Monday.")
    
