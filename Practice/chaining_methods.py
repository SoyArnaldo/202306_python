class Usuario:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.balance_cuenta = 0
		
	def hacer_deposito(self, amount):	
		self.balance_cuenta += amount
		return self

	def hacer_retiro(self, amount):	
		self.balance_cuenta -= amount	
	
	def mostrar_balance_usuario(self):
		print(f"Usuario: {self.name} Balance:{self.balance_cuenta}")
		return self
	
	def transfer_dinero(self, other_user, amount):
		self.balance_cuenta  -= amount
		other_user.balance_cuenta += amount
		return self


usuario1 = Usuario("Daryl", "Daryl@gmail.com")
usuario2 = Usuario("Rick", "Rick@gmail.com")
usuario3 = Usuario("Tom","Tom@gmial.com")
usuario1.hacer_deposito(400_000).hacer_deposito(500_000).hacer_deposito(200_000)
usuario1.transfer_dinero(usuario3, 200_000)
usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()
usuario2.hacer_deposito(250_000).hacer_deposito(150_000)
usuario2.transfer_dinero(usuario1, 100_000).transfer_dinero(usuario3, 100_000)
usuario2.mostrar_balance_usuario()
usuario3.hacer_deposito(350_000)
usuario3.transfer_dinero(usuario2, 100_000).transfer_dinero(usuario1, 100_000)
usuario3.transfer_dinero(usuario2, 100_000)
usuario3.mostrar_balance_usuario()
