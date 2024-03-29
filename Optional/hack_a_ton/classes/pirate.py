from classes.molde import Personaje

class Pirate(Personaje):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack (self, ninja):
        super().attack(ninja)
        return self

