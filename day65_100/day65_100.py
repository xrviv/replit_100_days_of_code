class Char:
  name = None
  health = None
  magicPoints = None
  
  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
   
  def show(self):
    print("🌟Generic RPG🌟")
    print()
    print(f"Character Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")
    print()

class Player(Char):
  def __init__(self, name, health, magicPoints, lives):
    super().__init__(name, health, magicPoints)
    self.magicPoints = magicPoints
    self.lives = lives

  def print_details(self):
    super().show()
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")

class Enemy(Char):
  def __init__(self, name, health, magicPoints, type, strength, dayNight):
    super().__init__(name, health, magicPoints)
    self.type = type
    self.strength = strength

vampire = Char("Boris", 45, 70, "Vampire", "Night")

vampire = Char("Rishi", 70, 10, "Vampire", 75, "Day")

orc = Char("Bill", 60, 5, "Orc", 75, 90)

vampire.show()
vampire.show()
doctor.show()

'''

class Character:
    def __init__(self, name, health, magic_points):
        self.name = name
        self.health = health
        self.magic_points = magic_points
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Magic Points: {self.magic_points}")


class Player(Character):
    def __init__(self, name, health, magic_points, lives):
        super().__init__(name, health, magic_points)
        self.lives = lives
    
    def is_alive(self):
        if self.lives > 0:
            return "Yes"
        else:
            return "No"


class Enemy(Character):
    def __init__(self, name, health, magic_points, enemy_type, strength):
        super().__init__(name, health, magic_points)
        self.enemy_type = enemy_type
        self.strength = strength


class Orc(Enemy):
    def __init__(self, name, health, magic_points, enemy_type, strength, speed):
        super().__init__(name, health, magic_points, enemy_type, strength)
        self.speed = speed


class Vampire(Enemy):
    def __init__(self, name, health, magic_points, enemy_type, strength, day_night):
        super().__init__(name, health, magic_points, enemy_type, strength)
        self.day_night = day_night


# Instantiate the objects
player = Player("Hero", 100, 50, 3)
vampire1 = Vampire("Dracula", 80, 30, "Vampire", 10, "Night")
vampire2 = Vampire("Vlad", 90, 40, "Vampire", 8, "Night")
orc1 = Orc("Gronk", 120, 20, "Orc", 12, "Fast")
orc2 = Orc("Dorg", 110, 15, "Orc", 10, "Medium")
orc3 = Orc("Morg", 100, 10, "Orc", 8, "Slow")

# Print their values
player.display_info()
print(f"Lives: {player.lives}")
print(f"Is alive? {player.is_alive()}")
print("--------------------")
vampire1.display_info()
print(f"Type: {vampire1.enemy_type}")
print(f"Strength: {vampire1.strength}")
print(f"Day/Night: {vampire1.day_night}")
print("--------------------")
vampire2.display_info()
print(f"Type: {vampire2.enemy_type}")
print(f"Strength: {vampire2.strength}")
print(f"Day/Night: {vampire2.day_night}")
print("--------------------")
orc1.display_info()
print(f"Type: {orc1.enemy_type}")
print(f"Strength: {orc1.strength}")
print(f"Speed: {orc1.speed}")
print("--------------------")
orc2.display_info()
print(f"Type: {orc2.enemy_type}")
print(f"Strength: {orc2.strength}")
print(f"Speed: {orc2.speed}")
print("--------------------")
orc3.display_info()
print(f"Type: {orc3.enemy_type}")
print(f"Strength: {orc3.strength}")
print(f"Speed: {orc3.speed}") '''

