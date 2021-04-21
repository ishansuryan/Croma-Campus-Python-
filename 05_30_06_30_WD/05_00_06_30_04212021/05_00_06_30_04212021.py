class grand_father():
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        print('The name is', self.name)
    
    def same(self):
        print('Grand Father funcrion')
        
class father():
    def __init__(self,age):
        self.age = age
    
    def get_age(self):
        print('The age is ', self.age)
        
    def same(self):
        print('Father funcrion')
        

class child(grand_father,father):
    def __init__(self, name, age, game):
        grand_father.__init__(self,name)
        father.__init__(self,age)
        self.game = game
    
    def get_game(self):
        print(f'The game played by {self.name} is {self.game} at the age of {self.age}')
    
c1 = child('Ronaldo',35,'Football')

c1.get_game()
c1.get_name()
c1.get_age()
grand_father.same(c1)

class dob():
    def __init__(self, birthyear):
        self.byear = birthyear
    
    @classmethod    
    def get_age(cls,year):
        print('the age is', 2021 - year) 
                
    @staticmethod
    def get_year():
        print('the year is 2021')

print()

dob.get_year()     
# s1 = dob(1992)

print()
dob.get_age(2000)
