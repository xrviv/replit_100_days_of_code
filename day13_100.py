print("Exam Grade Calculator")
print("---------------------")
print()
examName = input("Name of exam: ") 
maxScore = float(input("What is the max. possible score: "))
yourScore = float(input("What is your Score: "))
print()
scorePercent = (yourScore / maxScore)*100
roundedScorePercent = round(scorePercent, 2)
print("Your score in percentage is:", roundedScorePercent, "%")
roundedScorePercent = round(scorePercent, 2)

if roundedScorePercent > 100:
  print("Please input a valid number. (Your score may have been higher than the maximum score, etc)") 
elif (roundedScorePercent >= 90) and (roundedScorePercent <= 100):
   print("The score of\033[0;32m", roundedScorePercent, "\033[32mis equivalent to an A+") 
elif (roundedScorePercent >= 80) and (roundedScorePercent <= 89):
   print("The score of\033[0;32m", roundedScorePercent, "\033[32mis equivalent to an A") 
elif (roundedScorePercent >= 70) and (roundedScorePercent <= 79):
   print("The score of\u001b[33m", roundedScorePercent, "\u001b[33mis equivalent to a B") 
elif (roundedScorePercent >= 60) and (roundedScorePercent <= 69):
   print("The score of\u001b[33m", roundedScorePercent, "\u001b[33mis equivalent to a C") 
elif (roundedScorePercent >= 50) and (roundedScorePercent <= 59):
   print("The score of\u001b[31m", roundedScorePercent, "\u001b[31mis equivalent to a D") 
elif (roundedScorePercent >= 0) and (roundedScorePercent < 50):
   print("The score of\u001b[31m", roundedScorePercent, "\u001b[31mis equivalent to a U") 
else:
   print("Please input a valid number. (Your score may have been higher than the maximum score, negative, etc)") 

