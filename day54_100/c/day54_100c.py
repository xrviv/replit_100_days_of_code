# OpenAI GPT3 Assisted Code
import csv 

total = 0.0
subtotal = 0.0

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 
  for row in reader:
    cost = float(row["Cost"])
    quantity = float(row["Quantity"])
    subtotal += cost * quantity

print("🌟Shop $$ Tracker🌟")
print()
print(f"Your shop took £{round(subtotal, 2):,} today.")
