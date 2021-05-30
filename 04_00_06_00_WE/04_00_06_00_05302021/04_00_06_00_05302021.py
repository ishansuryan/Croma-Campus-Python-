# Class 
# Multilevel inheritance
# class grandfather():
#     def __init__(self, nme):
#         self.name = nme
#     def get_name(self):
#         print('grand father class name is:', self.name)

# class father(grandfather):
#     def __init__(self, name,ag):
#         super().__init__(name)
#         self.age = ag
#     var_ = 20

#     def get_age(self):
#         print('The age is:', self.age)
#         print(self.var_+30)

# class child(father):
#     def __init__(self,nme,age,sport):
#         super().__init__(nme,age)
#         self.sport = sport
#     def get_sport(self):
#         print('Favourate sport is', self.sport)
# g1 = grandfather('Sun')      # creating an instance of class
# g2 = grandfather('Monday')
# g1.get_name()
# g2.get_name()
# f1 = father('SUN',30)

# f1.get_age()
# f1.get_name()

# f2 = father('Monday',58)
# f2.get_name()
# f2.get_age()

# c1 = child('Sun', 30, 'Football')
# c1.get_name()
# c1.get_age()
# c1.get_sport()

# Multiple inheritance

# class grandfather():
#     def __init__(self, nme):
#         self.name = nme
#     def get_name(self):
#         print('grand father class name is:', self.name)

#     def any_func(self):
#         print('inside grandfather class')

# class father():
#     def __init__(self, ag):

#         self.age = ag
#     var_ = 20

#     def get_age(self):
#         print('The age is:', self.age)
#         print(self.var_+30)

#     def any_func(self):
#         print('inside father class')

# class child(grandfather,father):
#     def __init__(self,nme,age,sport):
#         grandfather.__init__(self,nme)
#         father.__init__(self,age)
#         self.sport = sport
#     def get_sport(self):
#         print('Favourate sport is', self.sport)

# c1 = child('Sohan', 32, 'Cricket')

# c1.get_name()
# c1.get_age()
# c1.any_func()
# father.any_func(c1)
# father.get_age(c1)

# Polymorphism

# class dog():
#     def __init__(self,name,):
#         self.name = name

#     def get_name(self):
#         print(f'the name of dog is {self.name}')
    
#     def make_sound(self):
#         print('Dog barks')

# class cat():
#     def __init__(self,name,):
#         self.name = name

#     def get_name(self):
#         print(f'the name of cat is {self.name}')
    
#     def make_sound(self):
#         print('cat makes sound meow')

# d = dog('Jimmy')
# c = cat('Garfield')

# def properties(instance):
#     instance.get_name()
#     instance.make_sound()

# properties(d)
# properties(c)

from datetime import datetime

class cl_method():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self, age):
        print(f'age of {self.name} is {self.age}')

    @classmethod
    def birthyear(cls,name,birth_year):
        print(f'age of {name} is {datetime.now().year - birth_year}')

    @staticmethod
    def method(a,b):
        print('sum is', a+b)


cl_method.birthyear('Ram', 1985)
cl_method.method(3,3)

class tester():
    foo = 3
    _bar = 5
    __baz = 9

print(tester.foo)
print(tester._bar)
# print(tester.__baz__)
print(dir(tester))
print(tester._tester__baz)
