from getpass import getpass as input
round = 1
p1Score = 0
p2Score = 0
while True:
  
  print("--------------------")
  print("\033[1;31mRound", round, "\u001b[0m")
  print("The scores are:")
  print("Player 1 : ", p1Score)
  print("Player 2 : ", p2Score)
  if p1Score == 3:
    print("Player 1 Wins! 🎉")
  elif p2Score == 3:
    print("Player 2 wins! 🎉")
  else:
    print()
    print("Choose Rock, Paper, Scissors (Enter R,P or S) then press Enter")
    player1 = input("\033[1;35mPlayer 1 >> \u001b[0m")
    player2 = input("\033[1;34mPlayer 2 >> \u001b[0m")
    print()
    if player1 == "R":
      print("Player 1 has chosen ", player1, "🗿")  
      if player2 == "R":
         print("Player 2 has chosen ", player2, "🗿")
         print("It's a tie 👔")
         round += 1
         continue
      elif player2 == "P":
         print("Player 2 has chosen ", player2, "📄")
         print("Player 2 wins this round")
         p2Score += 1
         round += 1
         continue
      elif player2 == "S":
         print("Player 2 has chosen ", player2, "✂️")
         print("Player 1 wins this round")
         p1Score += 1
         round += 1
         continue
      else:
         print("\u001b[31mInvalid move Player 2\u001b[0m")
         print("Please input only R, P or S. (Uppercase)")
         round += 1
         continue
    elif player1 == "P":
      print("Player 1 has chosen ", player1)
      if player2 == "R":
        print("Player 2 has chosen ", player2, "🪨")
        print("Player 1 wins this round")
        p1Score += 1
        round += 1
        continue
      elif player2 == "P":
        print("Player 2 has chosen ", player2, "📄")
        print("It's a tie! 👔")
        round += 1
        continue
      elif player2 == "S":
        print("Player 2 has chosen ", player2, "✂️")
        print("Player 2 wins this round")  
        p2Score += 1
        round += 1
        continue
      else:
        print("\u001b[31mInvalid move Player 2\u001b[0m")
        print("Please input only R, P or S. (Uppercase)")
        round += 1
        continue
    elif player1 == "S":
      print("Player 1 has chosen ", player1)
      if player2 == "R":
        print("Player 2 has chosen ", player2, "🗿")
        print("Player 2 wins! 🎉")
        p2Score += 1
        round += 1
        continue
      elif player2 == "P":
        print("Player 2 has chosen ", player2, "📄")
        print("Player 1 wins! 🥳")
        p1Score += 1
        round += 1
        continue
      elif player2 == "S":
        print("Player 2 has chosen ", player2, "✂️")
        print("It's a tie! 👔")  
        round += 1
        continue
      else:
        round += 1
        print("\u001b[31mInvalid move Player 2\u001b[0m")
        print("Please input only R, P or S. (Uppercase)")
        continue
    else:
      round += 1
      print("\u001b[31mInvalid move Player 1\u001b[0m")
      print("Please input only R, P or S. (Uppercase)")
      continue
  exit()
