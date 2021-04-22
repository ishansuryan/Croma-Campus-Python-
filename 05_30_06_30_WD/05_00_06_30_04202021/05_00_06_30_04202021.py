class player():
    def __init__(self, nme,ag):
        self.name  = nme
        self.age = ag
    
    def get_name(self):
        print('The name of player is:',self.name)
    
    def print_age(self):
        print('The age of player is :',self.age)
        
# p1 = player('Ronaldo',35)

# p1.get_name()
# p1.print_age()


class game(player):
    def __init__(self,nme,ag,game):
        super().__init__(nme,ag)
        self.game = game
    
    def get_game(self):
        print(f'The game played by {self.name} is {self.game}')

p2 = game('ronaldo',35,'football')

p2.get_name()


class best_kick(game):
    def __init__(self,name,age,game,kick):
        super().__init__(name,age,game)
        self.kick = kick
        
    def get_stroke(self):
        print(f'The best stroke played by {self.name} is {self.kick} at the age of {self.age}')
        

n1 = best_kick("Christiano",35,'Football','back kick')
n1.get_name()
n1.print_age()
n1.get_game()
n1.get_stroke()