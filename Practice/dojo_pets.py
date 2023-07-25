class Mascota:
	def __init__(self, nombre, golosinas) -> None:
		self.nombre = nombre
		self.golosinas = golosinas
		self.energia = 0
		self.salud = 0
	
	def dormir(self):
		self.energia += 25
	
	def comer(self):
		self.energia += 5
		self.salud += 10
	
	def jugar(self):
		self.salud += 5
	
	def ruido(self):
		print("")

class Ninja(Mascota):
	"""Molde de la clase Ninja"""
	def __init__(self, nombre:str, apellido:str, mascotas:str, premio:str, 
		comida_mascotas:str) -> None:
		"""Constructor para objetos e instancias que se creen de la clase 
			Ninja
		"""
		super().__init__(self, mascotas, comida_mascotas)
		self.nombre = nombre
		self.apellido = apellido
		self.mascotas = mascotas
		self.premio = premio
		self.comida_mascotas = comida_mascotas
	
	def caminar(self):
		super().jugar(self)
	
	def alimentar(self):
		super().comer(self)
	
	def banar(self):
		super().sonido(self)

ninja = Ninja("Ninja", "Chan","Perro", "Mejor amigo del ser humano", "Hueso")