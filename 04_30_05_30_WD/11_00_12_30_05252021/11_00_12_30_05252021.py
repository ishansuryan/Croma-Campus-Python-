# class today():
#     def __init__(self):
#         self.foo = 'foo'
#         self._bar = 'bar'
#         self._bar_ = 'barr'
#         self.__baz = 'I am Invisible'
    
#     # def print_(self):
#     #     print( self.foo, self._bar,self._bar_, sep = '\n')

#     def gayab(self):
#         print(self.__baz)


# v1 = today()

# print(v1.foo)
# print(v1._bar)
# print(v1._bar_)
# print(v1._today__baz)

# print(dir(v1))
# v1.gayab()


# Polymorphism

class cat():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def sound(self):
        print('cat make sound meow')
    
    def prop(self):
        print(f'The name of cat is {self.name} and age is {self.age}')

class dog():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def sound(self):
        print('Dog make sound bark')
    
    def prop(self):
        print(f'The name of dog is {self.name} and age is {self.age}')

d1 = dog('Diggy',5)      #
c1 = cat('Garfield',1)      # 

def pro(ins):
    ins.sound()
    ins.prop()

pro(d1)
pro(c1)

# Class method

class person():
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    def get_age(self):
        print(f"{self.name}'s age is {self.age}")
    @classmethod
    def birthyear(cls,name, year):
        print(f"{name}'s age is {2021-year}")
        
    @staticmethod
    def addition(a,b):
        print(a+b)

p = person('Prince',20)

p.get_age()

person.birthyear('Rahul',1991)
p.get_age()
p.birthyear('Game',2000)

person.addition(20,30)