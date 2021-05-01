# class grand_father():
#     def __init__(self,name):
#         self.name = name
        
#     # def get_name(self):
#     #     print('Name is:', self.name)

#     def same(self):class grand_father():
#     def __init__(self,name):
#         self.name = name
        
#     # def get_name(self):
#     #     print('Name is:', self.name)

#     def same(self):
#         print('Inside grandfather class')
    
# class father():
#     def __init__(self, age):
#         self.age = age
    
#     def same(self):
#         print('Inside father class')

# class child(grand_father,father):
#     def __init__(self,name,age,game):
#         grand_father.__init__(self,name)
#         father.__init__(self,age)
#         self.game  = game
    
#     def get_game(self):
#         print(f'The game played by {self.name} is {self.game} at the age {self.age}')

# s = child('Ram',60,'Football')

# # s.get_name()
# s.get_game()   
# father.same(s)
#         print('Inside grandfather class')
    
# class father():
#     def __init__(self, age):
#         self.age = age
    
#     def same(self):
#         print('Inside father class')

# class child(grand_father,father):
#     def __init__(self,name,age,game):
#         grand_father.__init__(self,name)
#         father.__init__(self,age)
#         self.game  = game
    
#     def get_game(self):
#         print(f'The game played by {self.name} is {self.game} at the age {self.age}')

# s = child('Ram',60,'Football')

# # s.get_name()
# s.get_game()   
# father.same(s)
from datetime import date

# print(year)
class age_calculator():
    def __init__(self,age):
        self.age = age
    
    def get_age(self):
        print(f'the age is {self.age}')
    
    @ classmethod
    def age_get(cls, birthyear):
        year = date.today().year
        month =date.today().month
        print(f'The age is {year-birthyear}')
    
    @ staticmethod
    def static(b):
        print(f'2 to the power {b} is',2**b)


# a = age_calculator(0.2)
age_calculator.age_get(1997)
# age_calculator.get_age()
age_calculator.static(2)