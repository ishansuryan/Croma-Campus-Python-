# def pow(a):
#     def inner(b):
#         print(b**a)
#     return inner

# value = pow(2)          # value = inner
# print(value(10))
# value(3)
# value(4)

# cube = pow(3)
# cube(4)

class player():
    def __init__(self,nme, gme, age):
        self.name = nme
        self.game = gme
        self.age = age
        
    def get_name(self):
        print('The player name is', self.name)
        
    def get_game(self):
        print(f'The game played by {self.name} is {self.game}')
        
    def get_age(self):
        print(f'The age of {self.name} is {self.age}')
        

player1 = player('Ronaldo','Cricket',28)
player1.get_name()
player1.get_game()

player2 = player('Sachin','Cricket',48)

player2.get_game()



class cat():
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f'{self.name} makes sound Meow')
        
class dog():
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f'{self.name} makes sound bark')
        
def get_sound(instance):                # polymorphism
    instance.make_sound()
    
c = cat('Orion')
d = dog('Jimmy')

get_sound(d)    
get_sound(c)



# Inheritance Multi Level

class grand_father():
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        print('Name is:', self.name)
    
class father(grand_father):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

class child(father):
    def __init__(self,name,age,game):
        super().__init__(name,age)
        self.game  = game
    
    def get_game(self):
        print(f'The game played by {self.name} is {self.game} at the age {self.age}')

s = child('Ram',60,'Football')

s.get_name()
s.get_game()