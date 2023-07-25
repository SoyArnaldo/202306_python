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

cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria()
cuenta1.deposito(100_000).deposito(250_000).deposito(150_000).retiro(50_000)
cuenta1.genera_interes().mostrar_info_cuenta()
cuenta2.deposito(250_000).deposito(200_000).retiro(100_000).retiro(100_000)
cuenta2.retiro(100_000).retiro(50_000).genera_interes().mostrar_info_cuenta()