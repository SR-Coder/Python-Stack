# DEFINE A CLASS
class Person:
    # ATTRIBUTES(or characterstics)
    def __init__(self, name='user', hair_color='brown', age =0, limbs =4):
        print(f'a new human is born and their name is {name}')
        self.name = name
        self.age = age
        self.limbs = limbs
        self.hair_color = hair_color
        # print(f'a new human is born and their name is {self.name}')
    # METHODS
    def say_hello(self):
        # print('hello i am awesome')
        print(f"Hello my name is {self.name} and I am {self.age} years old!!")
        return self
    def birthday(self):
        print(self.age)
        self.age += 1  # self.age = self.age + 1
        print(f'oh wow rick look at me im {self.age}')
    def printInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Hair Color: {self.hair_color}, Limbs: {self.limbs}")



# Instantiating a class

person1 = Person('Spyder Bob','red', 43, 8)
person2 = Person('Morty', 'bald', 14, 4)
person3 = Person(limbs=10,name='Mr. MeSeeks',hair_color='blue')
person4 = Person()
print(person1.name)
person1.say_hello()
person2.say_hello()

personLst=[person1, person2, person3, person4]


person2.birthday()
print(person3.limbs)

for person in personLst:
    person.printInfo()

for i in range(len(personLst)-1,0,-1):
    personLst[i].printInfo()


