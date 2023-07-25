from classes.molde import Personaje

class Ninja(Personaje):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, pirate):
        super().attack(pirate)
        return self