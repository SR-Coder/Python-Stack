# Data types?
# float, int, double or numbers
x = 1 # int
y = 1.01 # double
pi = 3.14159 # float
# string
my_name = 'Jim is my name' # string
# Bool
test = True # or false / Bool
# Lists are arrays in js
        #  0 1 2 3 4 5
my_list = [9,2,7,4,5,2]
third = my_list[2] # = 7
another_list = ['Yer', 'Jacob', 'Tj'] 
# Dictionarys Objects in js
person1 = {'first_name':'Marc', 'last_name':'Dorsett'}
print(person1)
cars = {
    'car1': 'firebird',
    'car2': 'corvette',
}
person1['age'] = 25
print(person1)
person1['age'] = 35
print(person1)
print(type(person1))
a_first_name = person1['first_name']

fname = 'Jim'
lname = 'Reeder'
my_string = f'Hello, my name is {fname} {lname}'
print(my_string)

# newString = 'Hello, my name is %s %s and I am %d years old' %(fname, lname, age)
# newString = 'Hello, my name is {} {} and I am {} years old'.format(fname, lname, age)

string2 = "hi it's sunny out"

# For Loops
# What is a for loop
# for( i = 0; i < 1000; i++){
#     console.log('Jim Reeder')
# }

for i in range(1000): #range here will give us 0-999
    print(f'thomas {i}')

for i in range(5,500): # 5-499
    print('Jim')

for i in range(10,100,5):
    print("Jake")

i = 0 # initial condition
while(i<100): # while loo[p]
    print('Jim Reeder') # code to run
    i = i+1 #increment

print('Jim Reeder')

persons = ['Jason', 'Joshua','Darrell', 'Jim']
for i in range(0,len(persons), 2):
    print(persons[i])

for name in persons:
    print(name)

# Conditionals
# if, else, elif
# chain conditionals
# and, or
# ==, !=, >, <, >=, <=
for i in range(0,26): # 0-25
    if i<10:
        print('the number is less than 10!!!')
    elif i>=10 and i<20:
        print('Coding is fun')
    else:
        print(i)
print('outside of the for loop')

# Functions
#something that does more than one thing
# code that can be reused
# way to have more control over our code
# Its a Set of Instructions
def sayHello(name):
    print(f'hi my name is {name}')
    
sayHello('slim shady')

def adder(x,y):
    my_sum = x+y
    return my_sum

new_sum = adder(1,2) # --> new_sum = sum --> 3
print(new_sum)

print(adder(2,4))


