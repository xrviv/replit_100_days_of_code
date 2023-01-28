import datetime

print ("🌟Event Countdown Timer🌟")
print()

today = datetime.date.today()
event = input("Input the event > ")
year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))

holiday = datetime.date(year, month, day)

if holiday > today:
  wait = holiday - today
  print(f"🤞 {wait.days} days til the event!")
elif holiday < today:
  passed = today - holiday
  print(f"😔 {passed.days} days have passed since.")
else:
  print(f"🎉🎉 {event} is today! 🎉🎉 ")