from getpass import getpass as input

player1 = input("Player 1 = Choose Rock, Paper, Scissors (Enter R,P,S) then press Enter> ")
player2 = input("Player 2 = Choose Rock, Paper, Scissors (Enter R,P,S) then press Enter> ")
print()

if player1 == "R":
  print("Player 1 has chosen ", player1, "🪨")  
  print("--------------------")
  if player2 == "R":
     print("Player 2 has chosen ", player2, "🪨")
     print("It's a tie 👔")
  elif player2 == "P":
     print("Player 2 has chosen ", player2, "📄")
     print("Player 2 wins! 🎉")
  elif player2 == "S":
     print("Player 2 has chosen ", player2, "✂️")
     print("Player 1 wins! 🥳")  
  else:
     print("Invalid move Player 2")
     print("Please input only R, P or S. (Uppercase)")
elif player1 == "P":
  print("Player 1 has chosen ", player1)
  print("--------------------")
  if player2 == "R":
    print("Player 2 has chosen ", player2, "🪨")
    print("Player 1 wins! 🎉")
  elif player2 == "P":
    print("Player 2 has chosen ", player2, "📄")
    print("It's a tie! 👔")
  elif player2 == "S":
    print("Player 2 has chosen ", player2, "✂️")
    print("Player 2 wins! 🥳")  
  else:
     print("Invalid move Player 2")
     print("Please input only R, P or S. (Uppercase)")
elif player1 == "S":
  print("Player 1 has chosen ", player1)
  print("--------------------")
  if player2 == "R":
    print("Player 2 has chosen ", player2, "🪨")
    print("Player 2 wins! 🎉")
  elif player2 == "P":
    print("Player 2 has chosen ", player2, "📄")
    print("Player 1 wins! 🥳")
  elif player2 == "S":
    print("Player 2 has chosen ", player2, "✂️")
    print("It's a tie! 👔")  
  else:
     print("Invalid move Player 2")
     print("Please input only R, P or S. (Uppercase)")
else:
  print("Please input only R, P or S. (Uppercase)")
