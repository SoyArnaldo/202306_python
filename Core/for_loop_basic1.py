for num in range(0,151, +1):
    if num % 2 == 0:
        print(num)

for num in range(5,1001, +1):
    if num % 5 == 0:
        print(num)

for num in range(1,101, +1):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

sum = 0
for num in range(0,500001, +1):
    if num % 2 != 0:
        sum += num       

print(sum)

year = 2018
while year >= 4:
    print(year)
    year-=4

lowNum=2
highNum=10 
mult=3
for num in range(lowNum,highNum, +1):
    if num % mult == 0:
        print(num)