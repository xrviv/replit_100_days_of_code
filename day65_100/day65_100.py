class Char:
  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
   
  def show(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")

class Player(Char):
  def __init__(self, name, health, magicPoints, lives):
    super().__init__(name, health, magicPoints)
    self.lives = lives

  def showAliveStatus(self):
    if self.lives > 0:
      return "Yes"
    else:
      return "No"

class Enemy(Char):
  def __init__(self, name, health, magicPoints, type, strength):
    super().__init__(name, health, magicPoints)
    self.type = type
    self.strength = strength

class Orc(Enemy):
  def __init__(self, name, health, magicPoints, type, strength, speed):
    super().__init__(name, health, magicPoints, type, strength)
    self.speed = speed
    
class Vampire(Enemy):
  def __init__(self, name, health, magicPoints, type, strength, dayOrNight):
    super().__init__(name, health, magicPoints, type, strength)
    self.dayOrNight = dayOrNight

# Instantiate the objects
player = Player("David", 100, 50, 3)
vampire1 = Vampire("Boris", 45, 70, "Vampire", 3, "Night")
vampire2 = Vampire("Rishi", 70, 10, "Vampire", 75, "Night")
orc1 = Orc("Bill", 60, 5, "Orc", 75, 90)
orc2 = Orc("Ted", 75, 40, "Orc", 80, 45)
orc3 = Orc("Station", 35, 40, "Orc", 49, 50)

# Print their values
print("🌟Generic RPG🌟")
print()

player.show()
print(f"Lives: {player.lives}")
print(f"Is alive?: {player.showAliveStatus()}")
print("----------")
vampire1.show()
print(f"Type: {vampire1.type}")
print(f"Strength: {vampire1.strength}")
print(f"Day/Night: {vampire1.dayOrNight}")
print("----------")
vampire2.show()
print(f"Type: {vampire2.type}")
print(f"Strength: {vampire2.strength}")
print(f"Day/Night: {vampire2.dayOrNight}")
print("----------")
orc1.show()
print(f"Type: {orc1.type}")
print(f"Strength: {orc1.strength}")
print(f"Speed: {orc1.speed}")
print("----------")
orc2.show()
print(f"Type: {orc2.type}")
print(f"Strength: {orc2.strength}")
print(f"Speed: {orc2.speed}")
print("----------")
orc3.show()
print(f"Type: {orc3.type}")
print(f"Strength: {orc3.strength}")
print(f"Speed: {orc3.speed}")