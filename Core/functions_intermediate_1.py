x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'}, 
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]["last_name"] = 'Bryant'
print(estudiantes)


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)


estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(listt) :
    for  index in range(len(listt)):
        key = list(listt[index].items())
        print(key[0][0] + " - " + key[0][1] + ", " + key[1][0] + " - " + key[1][1])
iterateDictionary(estudiantes)


def iterateDictionary2(listt2):
    count = 0
    count2 = 0
    for num in range(8):
        if count <= 3:
            key = list(listt2[count].keys())
            print(listt2[count][key[0]])
            count += 1
        else:
            key = list(listt2[count2].keys())
            print(listt2[count2][key[1]])
            count2 += 1
iterateDictionary2(estudiantes)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(listt):
    key = list(listt.keys())
    lenn = int(len(listt[key[0]]))
    lennn = int(len(listt[key[1]]))
    print(lenn, f"{key[0].upper()}")
    for i in range(len(listt[key[0]])):
        print(listt[key[0]][i])
    print("""""")
    print(lennn, f"{key[1].upper()}")
    for i in range(len(listt[key[1]])):
        print(listt[key[1]][i])
printInfo(dojo)