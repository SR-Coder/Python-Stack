# DEFINE A CLASS
class Person:
    # ATTRIBUTES(or characterstics)
    def __init__(self, name, age, limbs, hair_color):
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
    def birthday(self):
        print(self.age)
        self.age += 1  # self.age = self.age + 1
        print(f'oh wow rick look at me im {self.age}')



# Instantiating a class

person1 = Person('Spyder Bob', 43, 8, 'Red')
person2 = Person('Morty', 14, 4, 'bald')
print(person1.name)
person1.say_hello()
person2.say_hello()

person2.birthday()



