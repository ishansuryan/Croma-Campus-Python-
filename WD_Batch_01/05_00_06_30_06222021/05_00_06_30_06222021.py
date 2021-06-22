class grand_father():
 
    def __init__(self,name):    #constreuctor
        self.val_rec = name

    def prt_name(self):
        print('Grand Father Class name is ', self.val_rec)

class father(grand_father):
    def __init__(self, name,age):
        super().__init__(name)
        self.ag = age
        
    def prt_age(self):
        print('age is', self.ag)
           
class child(father):
    def __init__(self, name, age, game):
        super().__init__(name,age)
        self.play = game
    
    def prt_game(self):
        print(f'The game played by {self.val_rec} is {self.play} at the age of {self.ag}')
               
# a1 = grand_father('Indian')
# a1.prt_name()

# a2 = grand_father('Bharat')
# a2.prt_name()
f1 = child('Indian',30,'Football')
f1.prt_name()
f1.prt_age()
f1.prt_game()