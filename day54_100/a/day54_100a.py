import csv

total = 0.0

with open("January.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		print(row["Net Total"])
		total += float(row["Net Total"])

print(f"Total: {total}")