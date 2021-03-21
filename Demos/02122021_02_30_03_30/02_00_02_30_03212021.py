# a = input("Please enter number:")
# b = input('Please enter number:')
# print('The sum is:', int(a)+int(b))

import random as r
print(r.randint(1000,9999))

class player():
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        print('My name is',self.name)
        
player1 = player('Croma')
player1.get_name()