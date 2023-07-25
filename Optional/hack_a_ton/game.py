import os

from classes.ninja import Ninja
from classes.pirate import Pirate

print("Ingresa tu nombre:\n")
name = input()
user = Pirate(name)
print(f"{name}\nDescripción de tu personaje:")
user.show_stats()
print("Ingresa el nombre de tu rival:\n")
name2 = input()
user2 = Ninja(name2)
print(f"{name2}\nDescripción del personaje:")
user2.show_stats()

while True:
	print("Atacarse ENTER")
	input()
	user.attack(user2)
	print(f"Vida actual de {user2.name}: {user2.health}")
	user2.attack(user)
	print(f"Vida actual de {user.name}: {user.health}")
	if user.health  < 0:
		print(f"Ganador: {user2.name}")
		break
	elif user2.health < 0:
		print(f"Ganador: {user.name}")
		break
	input("Presionar ENTER para continuar...")
	os.system("clear")