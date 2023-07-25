num1 = 42 #Variable, Number Int
num2 = 2.3 #Variable, Number Float
boolean = True #Variable, Boolean
string = 'Hello World' #Variable, String

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Variable, List

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Variable, Dict

fruit = ('blueberry', 'strawberry', 'banana') #Variable, Tuple

print(type(fruit)) #Imprime Type Dato

print(pizza_toppings[1]) #Imprime Element de Variable, List

pizza_toppings.append('Mushrooms') #Metodo añade un Element al final a List

print(person['name']) #Imprime valor Dict

person['name'] = 'George' #Cambia valor Dict

person['eye_color'] = 'blue' #Cambia valor Dict

print(fruit[2]) #Imprime ELement de la Variable, Tuple

if num1 > 45: #Condicional if - Condicion #Imprime ,#Condicional else #Imprime
    print("It's greater") 
else: 
    print("It's lower") 

if len(string) < 5: #Condicional if - Condicion #Imprime
    print("It's a short word!")
elif len(string) > 15: #Condicional elif - Condicion #Imprime
    print("It's a long word!")
else: #Condicional else #Imprime
    print("Just right!")

for x in range(5): #Bucle for, de 0 a 5, increment +1
    print(x) #Imprime

for x in range(2,5): #Bucle for, de 2 a 5, increment +1
    print(x) #Imprime

for x in range(2,10,3): #Bucle for, de 2 a 10, increment +3
    print(x) #Imprime

x = 0 #Variable, Number
while(x < 5): #Bucle while, de 0 a menor que 5
    print(x) #Imprime
    x += 1 #Increment +1

pizza_toppings.pop() #Extraer el ultimo element, #Variable, List

pizza_toppings.pop(1) #Extraer el element con indice, #Variable, List

print(person) #Imprime #Variable, Dict

person.pop('eye_color') #Extraer valor #Variable, Dict

print(person)  #Imprime #Variable, Dict

for topping in pizza_toppings: #Bucle For in, recorre  #Variable, List y devuelve element
    if topping == 'Pepperoni': #Condicional if
        continue #Continue - Omite esta iteración si se cumple la condición 
    print('After 1st if statement') #Imprime
    if topping == 'Olives':  #Condicional if
        break #Break - Finalizar de inmediato  si se cumple la condición

def print_hello_ten_times(): #Función
    for num in range(10): #Bucle for in de 0 a 10
        print('Hello') #Imprime

print_hello_ten_times() #Invocando a Función

def print_hello_x_times(x):  #Función
    for num in range(x): #Bucle for in de 0 a 4
        print('Hello') #Imprime

print_hello_x_times(4)  #Invocando a Función

def print_hello_x_or_ten_times(x = 10): #Función
    for num in range(x): #Bucle for in de 0 a 10, y 4
        print('Hello') #Imprime

print_hello_x_or_ten_times() #Invocando a Función
print_hello_x_or_ten_times(4)#Invocando a Función


"""
Bonus section
"""
num3 = 72 #Variable, Number - Int

print(num3) #Imprime

fruit[0] = 'cranberry' #Cambiando valor, #Variable, Tuple

print(person['favorite_team']) #Imprime valor Dict

print(pizza_toppings[7]) #Imprime #Variable, List

print(boolean) #Imprime #Variable, Boolean

fruit.append('raspberry') #Metodo agrega un Element al final a List

fruit.pop(1) #Extraer el element con indice, #Variable, Tuple