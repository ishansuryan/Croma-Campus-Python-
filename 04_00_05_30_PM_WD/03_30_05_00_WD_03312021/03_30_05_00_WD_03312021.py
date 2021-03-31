# class cat():
#     def __init__(self,nme, ag):
#         self.name = nme
#         self.age = ag
    
#     def make_sound(self):
#         print('Meow')
        
#     def info(self):
#         print(f'HI may name is {self.name} and i an {self.age} years old')


# class dog():
#     def __init__(self,nme, ag):
#         self.name = nme
#         self.age = ag
    
#     def make_sound(self):
#         print('Bark')
        
#     def info(self):
#         print(f'Hi may name is {self.name} and i an {self.age} years old') 


# cat1 = cat('Kitten', 2)
# dog1 = dog('puppy', 5)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2
    
    def __str__(self):
        return 'I am an overloaded function in circle'

a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
print(a)



class base():
    def __init__(self, a,b, nam = 'Non inverted'):
        self.num1 = a
        self.num2 = b
        self.name = nam
        
    def addd(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num1 - self.num2
    
    def __str__(self):
        return self.name


class invert(base):
    def __init__ (self, a,b, ): #n=  'inverted'):
        super().__init__(a,b,'inverted')
        # self.name = n
        self.a = a
        self.b = b
        
    def addd(self):
        return self.a-self.b
    
    def minus(self):
        return self.a+self.b
    
    
    # def __str__(self):
    #     return self.name
    

    
    
org = base(10,20)
print(org.addd())
print(org)

org_ = base(10,20,'new parameters')
print(org_.addd())
print(org_)


inv = invert(10,20)
print(inv.addd())
print(inv)


print()