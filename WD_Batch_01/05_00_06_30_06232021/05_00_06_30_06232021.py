class grandfather():
    def __init__(self, name):           # constructor initialises when an instance of class is created
        self.nme = name
        
    def prt_name(self):
        print("Name is", self.nme)
    
    def properties(self):
        print('inside grandfather class')
        
class father():
    def __init__(self, age):
        self.ag = age
    
    def prt_age(self):
        print('Age is', self.ag)
        
    def properties(self):
        print('inside father class')
        

class child(grandfather, father):
    def __init__(self, name,age, game):
        grandfather.__init__(self,name)
        father.__init__(self,age)
        self.gme = game
    
    def prt_prop(self):
        print(f'{self.nme} plays the game {self.gme} at the age of {self.ag}')


c1 = child('Ram',35,'Football')
# c1.prt_prop()
# c1.prt_name()
# c1.prt_age()
# c1.properties()
# father.properties(c1)

# Python name mangling

# class test():
#     foo = 10
#     __bar = 20
#     baz_ = 50

# print(test.foo)
# print(test.baz_)
# print(dir(test))
# print(test._test__bar)
# print('Grandfather directory\n', dir(grandfather))


# Static methods and class Methods

class person():
    def __init__(self, name, age):
        self.n = name
        self.a = age
    
    def prt_prop(self):
        print(f"{self.n}'s age is {self.a}")
    
    @classmethod
    def get_age(cls,name,year):
        from  datetime import datetime 
        year_ = datetime.now().year
        print(f"{name}'s age is {year_ - year}")
    
    @staticmethod
    def func():
        print('About class')
        
person.get_age('Ram', 1984)
person.func()