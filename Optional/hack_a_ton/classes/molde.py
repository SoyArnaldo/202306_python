class Personaje:
	def __init__(self, name) -> None:
		self.name = name
		self.strength = 0
		self.speed = 0
		self.health = 0

	def attack ( self , personaje ):
		personaje.health -= self.strength
		return self
