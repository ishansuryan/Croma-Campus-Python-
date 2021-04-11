# Multilevel Inheritance
# class grand_father():
#     # Constructor 
#     def __init__(self, nme):
#         self.name = nme
        
#     def get_name(self):
#         print('Name is:', self.name)
        
    
# class father(grand_father):
#     # constructor
#     def __init__(self,nme,ag):
#         super().__init__(nme)
#         self.age = ag
    
#     def get_age(self):
#         print('Name is:',self.name,'\tAge is:', self.age)

# class child(father):
#     # constructor
#     def __init__(self, nme,ag, cls):
#         super().__init__(nme,ag)
#         self.clss = cls
        
#     def _get_cls(self):
#         print('Class is:', self.clss)

# c1 = child('Billu','16','10th')

# c1.get_name()
# c1.get_age()
# c1._get_cls()

# Multiple Inheritance

# class grand_father():
#     # Constructor 
#     def __init__(self, nme):
#         self.name = nme
        
#     def get_name(self):
#         print('Name is:', self.name)
        
    
# class father():
#     # constructor
#     def __init__(self,ag):
#         self.age = ag
    
#     def get_name(self):
#         print('Age is:', self.age)

# class child(father, grand_father):
#     # constructor
#     def __init__(self, nme,ag, cls):
#         father.__init__(self,ag)
#         grand_father.__init__(self,nme)
#         super(grand_father, self.get_name)
#         self.clss = cls
        
#     def _get_cls(self):
#         print('Class is:', self.clss)

# c1 = child('Billu','16','10th')

# c1.get_name()
# #c1.get_age()
# c1._get_cls()





# hidden variables in classes 

# class hidden_var():
#     def __init__(self):
#         self.foo = 'Fooo'
#         self._bar = 'bar'
#         self.__baz = 'Baz'
    
# o = hidden_var()
# print(o.foo)
# print(o._bar)
# print(o._hidden_var__baz)
# print(dir(o))


# Polymorphism
# class dog():
#     def __init__(self, nme, breed, snd):
#         self.name = nme
#         self.breed = breed
#         self.sound = snd
    
#     def get_name(self):
#         print('The name of dog is:', self.name)
        
#     def get_breed(self):
#         print('The breed of dog is:', self.breed)
        
#     def make_sound(self):
#         print('The sound of dog is:', self.sound)
        
# class cat():
#     def __init__(self, nme, breed, snd):
#         self.name = nme
#         self.breed = breed
#         self.sound = snd
    
#     def get_name(self):
#         print('The name of cat is:', self.name)
        
#     def get_breed(self):
#         print('The breed of cat is:', self.breed)
        
#     def make_sound(self):
#         print('The sound of cat is:', self.sound)
    
# def get_attributes(object):
#     object.get_name()
#     object.get_breed()
#     object.make_sound()
    
# d1 = dog('blippu','palmerian','bark')
# c1 = cat('Katty','Garfield','meow')

# get_attributes(d1)
# get_attributes(c1)




# decorators
# def smrt_devide(func):
#     def inner(a,b):
#         if b == 0:
#             print('Devision by zero is not defined')
#             return 
        
#         return func(a,b)
    
#     return inner


# @smrt_devide
# def devide(a,b):
#     return a/b

# #devide = smrt_devide(devide)

# devide(10,0)

# Class Methods


# class example():
#     def __init__(self, age):
#         self.age = age
#     @classmethod   
#     def get_age(cls,year):
#         print('age is:', 2021 - year)

#     def get__age(self):
#         print('Age is:', self.age)

# c1 = example(20)
# example.get_age(1992)
# c1.get__age()




class example__():
    def __init__(self, age):
        self.age = age
        # self.day = day
    @staticmethod   
    def get_age(day):
        print('day is:', day)

    def get__age(self):
        print('Age is:', self.age)

c1 = example__(20)
example__.get_age('Sunday')
c1.get__age()