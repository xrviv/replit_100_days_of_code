print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR")
print()
principal = 1000
loanAmount = 1000
interest = 0.05
interestAmount = loanAmount * interest

for i in range(10):
  loanAmount = loanAmount + loanAmount * interest
  roundedNumber = round(loanAmount, 2)
  print ("Year ", i+1, "is", roundedNumber)
interestTotal = loanAmount - principal
roundedInterestTotal = round(interestTotal, 2)
print("You paid ", roundedInterestTotal, "in interest")
