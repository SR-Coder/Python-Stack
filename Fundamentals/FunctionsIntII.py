x = [ [5,2,3], [10,8,9] ]  # LIST OF LISTS
students = [ # LIST OF DICTIONARYS
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = { # DICTIONARY OF LISTS
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ] # LIST OF DICTIONARYS 

# def updList(lst, x, y, val):
#     lst[x][y] = val
#     print(lst)
#     return lst

# updList(x, 1,1,54)
# # x[1][0] = 15

# def updatStud(idx, pos, val):
#     students[idx][pos] = val 
#     print(students)

# updatStud(0,'last_name', 'Bryant')

def updateAnyTwo(obj, idx1, idx2, val):
    obj[idx1][idx2] = val
    print(obj)
    return obj

# updateAnyTwo(x, 1, 0, 15)
# updateAnyTwo(students, 0, "last_name", 'Bryant')
# updateAnyTwo(sports_directory, 'soccer', 0, 'Andres')
# updateAnyTwo(z, 0, 'y', 30)

students1 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for aDict in some_list:
        print(f"first_name - {aDict['first_name']}, last_name - {aDict['last_name']}")

# iterateDictionary(students1)

def iterateDictionary2(keyName, someList):
    for i in range(len(someList)):
        a = someList[i].get(keyName)
        print(a)
    
# iterateDictionary2('first_name', students1)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(someList):
    for key in someList:
        listLength = len(someList[key])
        print(listLength, key)
        for i in range(len(someList[key])):
            print(someList[key][i])

printInfo(dojo)