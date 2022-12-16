print("Generation Identifier")
print("@Replit  + @OpenAI GPT3 = 🤯")
print("This code was auto-corrected by GPT3")

year = int(input("Which year were you born? "))

if year <= 1900:
	print("You come from the Lost Generation")
elif year >= 1901 and year <= 1927:
	print("You come from the Greatest Generation")	
elif year >= 1928 and year <= 1945:
	print("You come from the Silent Generation")
elif year >= 1946 and year <= 1964:
	print("You come from the Baby Boomers")
elif year >= 1965 and year <= 1980:
	print("You come from the Generation X")
elif year >= 1981 and year <= 1996:
	print("You come from the Millennials")
elif year >= 1997 and year <= 2012:
	print("You come from the Generation Z")
else:
	print("You come from the Generation Alpha")

