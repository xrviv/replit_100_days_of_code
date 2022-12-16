print("Tip Calculator")
print()
spend = float(input("How much did you spend? "))
print()
tipPercent = float(input("What percentage do you want to tip? "))
print("tipPercent is ", tipPercent, "%")
print ()
people = int(input("How many people in your group? "))
print()
tipPercentDeci = tipPercent / 100 
tipPay = spend * tipPercentDeci
bill = spend + tipPay
print("-------------------------")
print("Your total bill including tip is: ", bill)
print("Your total tip is: ", tipPay)
share = bill / people
print("Each person's share is: ", share)
