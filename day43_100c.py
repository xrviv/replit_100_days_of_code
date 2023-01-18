# Code fixed by OpenAI GPT3
import os
import random

os.system("clear")
bingo = []

def prettyPrint():
	for row in bingo:
		print(f"{row:^10}", end=" | ")		

numbers = []
for i in range(8):
	numbers.append(random.randint(1,90))
	
numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
		  [ numbers[3], "BINGO", numbers[4]],
		  [ numbers[5], numbers[6], numbers[7]]]
		  
prettyPrint()
