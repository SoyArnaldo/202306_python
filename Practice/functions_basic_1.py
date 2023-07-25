#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # Imprime 5


#2
def number_of_military_branches():
    return 5
print(number_of_military_branches()) #Imprime 5


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #Imprime 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #Imprime 5


#5
def number_of_great_lakes():
    print(5) #Imprime 5
x = number_of_great_lakes()
print(x) #Imprime None


#6
def add(b,c):
    print(b+c) #Imprime 3 y 5
print(add(1,2) + add(2,3)) #Imprime None


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #Imprime "25"


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) #Imprime 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #Imprime 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #Imprime 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #Imprime 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + 
    number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #Imprime 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #Imprime 8


#11
b = 500
print(b) #Imprime 500
def foobar():
    b = 300
    print(b) #Imprime 300
print(b) #Imprime 500
foobar() #None
print(b) #Imprime 500


#12
b = 500
print(b) #Imprime 500
def foobar():
    b = 300
    print(b) #Imprime 300
    return b
print(b) #Imprime 500
foobar() #Devuelve 300
print(b) #Imprime 500


#13
b = 500
print(b) #Imprime 500
def foobar():
    b = 300
    print(b) #Imprime 300
    return b
print(b) #Imprime 500
b=foobar() 
print(b) #Imprime 300


#14
def foo():
    print(1) #Imprime 1
    bar() #None
    print(2) #Imprime 2
def bar():
    print(3) #Imprime 3
foo() #None


#15
def foo():
    print(1) #Imprime 1
    x = bar()
    print(x) #Imprime 5
    return 10
def bar():
    print(3) #Imprime 3
    return 5
y = foo()
print(y) #Imprime 10