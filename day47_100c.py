# OpenAIGPT3 Assisted Code

import random, os, time
cards = {
"Revel": {"Funding": 15600000, "Employees": 13, "CB Rank": 607, "Investors": 11},
"MSafe": {"Funding": 6300000, "Employees": 10, "CB Rank": 2556, "Investors": 9},
"Plugo": {"Funding": 9000000, "Employees": 50, "CB Rank": 3022, "Investors": 6},
"Xscape Photonics": {"Funding": 10000000, "Employees": 10, "CB Rank": 3127, "Investors": 1},
"Spaceport Technologies": {"Funding": 3600000, "Employees": 10, "CB Rank": 4498, "Investors": 10}
}

print("🌟Top Trumps: 2022 Startup Edition🌟")
print()
print("""Welcome to the Top Trumps 'Startup Battle' Simulator""")
print()
play_again = "y"
while play_again == "y":
  selectCard = input("""Choose your card:
  1 - Revel
  2 - MSafe
  3 - Plugo
  4 - Xscape Photonics
  5 - Spaceport Technologies
  
  > """)
  
  card_name = {
      "1": "Revel",
      "2": "MSafe",
      "3": "Plugo",
      "4": "Xscape Photonics",
      "5": "Spaceport Technologies",
  }.get(selectCard)
  
  print()
  select_startup_attrib = input("""Select a Startup Attribute:
  
  1. Funding
  2. Employees
  3. CB Rank (Lower is Better)
  4. Investors
  
  > """)
  
  startup_attrib = {
      "1": "Funding",
      "2": "Employees",
      "3": "CB Rank",
      "4": "Investors",
  }.get(select_startup_attrib)
  print()
  print(f"""You have chosen: \033[0;36m{card_name}\033[0m and the attribute: \033[0;36m{startup_attrib}\033[0m 
which has a value of : \033[0;36m{cards[card_name][startup_attrib]}\033[0m """)
  
  random_startup = random.choice([startup for startup in cards.keys() if startup != card_name])
  
  
  print(f"""The computer has chosen: \033[0;36m{random_startup}\033[0m and the attribute: \033[0;36m{startup_attrib}\033[0m 
which has a value of : \033[0;36m{cards[random_startup][startup_attrib]}\033[0m """)
  print()
  
  if startup_attrib == 'CB Rank':
      if cards[card_name][startup_attrib] < cards[random_startup][startup_attrib]:
          print(f"""{card_name} wins with a CB Rank of {cards[card_name][startup_attrib]} against 
{random_startup} with CB Rank of {cards[random_startup][startup_attrib]}""")
      elif cards[card_name][startup_attrib] > cards[random_startup][startup_attrib]:
          print(f"""{random_startup} wins with a CB Rank of {cards[random_startup][startup_attrib]} against 
{card_name} with CB Rank of {cards[card_name][startup_attrib]}""")
      else:
          print("It's a tie with the CB Rank of {} for both startups".format(cards[random_startup][startup_attrib]))
  else:
      if cards[card_name][startup_attrib] > cards[random_startup][startup_attrib]:
          print(f"""{card_name} wins with a value of
          {cards[card_name][startup_attrib]} {startup_attrib} against 
          {random_startup} with value of {cards[random_startup][startup_attrib]} {startup_attrib}""")
      elif cards[card_name][startup_attrib] < cards[random_startup][startup_attrib]:
          print(f"""{random_startup} wins with a value of
          {cards[random_startup][startup_attrib]} {startup_attrib} against 
          {card_name} with value of {cards[card_name][startup_attrib]} {startup_attrib} """)
      else:
          print("It's a tie with the value of {} {startup_attrib} for both startups".format(cards[random_startup][startup_attrib]))
  play_again = input("Play again? (y/n) > ")
  if play_again == "n":
    "Thank you for playing, good bye!"
    break
    

