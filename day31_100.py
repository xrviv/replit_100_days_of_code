def colorChange(color):
	if color=="red":
		return ("\033[31m")
	elif color=="white":
		return ("\033[0m")
	elif color=="blue":
		return ("\033[34m")
	elif color=="yellow":
		return("\033[033m")
	elif color=="green":
		return("\033[032m")
	elif color=="purple":
		return("\033[035m")
		
title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}={colorChange('yellow')} Music App	{colorChange('blue')}={colorChange('white')}={colorChange('red')}="
	
print(f"           {title:^35}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")
print()

prev = "prev"
next = "next"
pause = "pause"
print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")
print()
print()
print(f"\t\t\t{colorChange('white')}   WELCOME TO")
print(f"\t\t{colorChange('blue')}  --    ARMBOOK   --")
print()

text1 = "Definitely not a rip off of"
text2 = "a certain other social"
text3 = "networking site"
print(f"{colorChange('yellow')}{text1:>45}")
print(f"{colorChange('yellow')}{text2:>45}")
print(f"{colorChange('yellow')}{text3:>45}")
print()
print(f"\t\t\t\t{colorChange('red')}Honest.")
print()
print(f"\t\t\t\t{colorChange('white')}Username:")
print(f"\t\t\t\t{colorChange('white')}Password:")
