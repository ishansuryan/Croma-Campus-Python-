# class test():
#     def __init__(self):
#         self.foo = 200
#         self._bar = 30
#         self.__baz = 1
#     __a = 10

#     def __private(self):
#         print('I am a name mangled function')
    
    
# t = test()
# print(t.foo)
# print(t._bar)
# print(t._test__baz)

# print(dir(t))

# t._test__private()

# class Person:
#     age = 25
    
#     @classmethod
#     def printAge(cls):
#         print('The age is:', cls.age)
        
# # Person.printAge = classmethod(Person.printAge)
# Person.printAge()

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person_ = Person('Adam', 19)
person_.display()
                                #Preson, 'John',  1985
person1 = Person.fromBirthYear('John',  1995)
person1.display()

print(getattr(person1 , 'age'))
# from datetime import date

# # random Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
#         return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

# class Man(Person):
#     sex = 'Male'

# man = Man.fromBirthYear('John', 1985)
# print(isinstance(man, Man))

# man1 = Man.fromFathersAge('John', 1965, 20)
# print(isinstance(man1, Man))

# print(isinstance(man1, Person))

# class tf():
#     @staticmethod
#     def p():
#         print('static method call')

# tf.p()

# instance = tf()

# tf().p()


'''
Difference b/w class and static methods:
Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.
'''

# class Person:
#     age = 23
#     name = "Adam"

# person = Person()
# print('The age is:', getattr(person, "age"))
# print('The age is:', person.age)

# print('The age is:', getattr(person, 'sex','Male'))
# print('The age is:', getattr(person, "sex"))

