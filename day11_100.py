secMin = 60
minHour = 60
hourDay = 24
dayYear = 365

secYear = secMin * minHour * hourDay * dayYear
print("There are", secYear, "seconds in a normal non-leap year.")
leapDay = secMin * minHour * hourDay
print("If it's a leap year, there would be :", leapDay, "additional seconds")
print("So in total, a leap year would", leapDay + secYear, "seconds")

