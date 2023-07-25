def countDown(num) :
    array = []
    for i in range(num, -1, -1):
        array.append(i)
    return array
print(countDown(5))


def func(listt):
    for i in range(len(listt)):
        if i == 0:
            print(listt[i])
        else:
            return listt[i]
print(f"Soy return: {func([2,10])}")


def summ(lisst):
    for i in range(0, len(lisst), +1):
        if i == 0:
            return lisst[i] + len(lisst)
print(summ([2,4,6,8,10,23]))


def new(lisst):
    sum = 0
    new = []
    for i in range(0, len(lisst), +1):
        if lisst[i] > lisst[1]:
            sum += 1
            new.append(lisst[i])
    print(sum)
    return new
print(new([2,4,6,8,10,23]))


def change(size, value):
    new = []
    for i in range(0, size, +1):
        if i <= size:
            new.append(value)
    return new
print(change(4,10))