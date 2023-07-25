class CuentaBancaria:
	balance = 0
	tasa_interes = 0.01

	def __init__(self, tasa_interes:float = 0.01, balance = 0) -> None:
		self.tasa_interes = tasa_interes
		self.balance = balance
	
	def deposito(self, amount):
		self.balance += amount
		return self

	def retiro(self, amount):
		self.balance -= amount
		if self.balance < 0:
			print( "Fondos insuficientes: cobrando una tarifa de $5")
			self.balance -= 5
		return self

	def mostrar_info_cuenta(self):
		print(f"Balance: ${self.balance}")
		return self

	def genera_interes(self):
		if self.balance > 0:
			self.balance += self.balance * self.tasa_interes                                                            
		return self

class Usuario:

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.cuenta = CuentaBancaria(tasa_interes= 0.02)
	
	def hacer_deposito(self, amount):	
		self.cuenta.balance += amount
		return self

	def hacer_retiro(self, amount):	
		self.cuenta.balance -= amount	
	
	def mostrar_balance_usuario(self):
		print(f"Usuario: {self.name} Balance:{self.cuenta.balance}")
	
	def transfer_dinero(self, other_user, amount):
		self.cuenta.balance  -= amount
		other_user.cuenta.balance += amount
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
usuario3.hacer_deposito(350_000).transfer_dinero(usuario2, 100_000).transfer_dinero(usuario1, 100_000)
usuario3.transfer_dinero(usuario2, 100_000)
usuario3.mostrar_balance_usuario()
