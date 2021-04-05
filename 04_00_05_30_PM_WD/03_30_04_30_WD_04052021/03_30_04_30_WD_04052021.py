class player():
    def __init__(self, nme, ae):
        self.name = nme
        self.__age = ae
        
    def print_name(self):
        print('name is:', self.name)
        
    # def __print_age(self):
    #     print('Age of player is:', self.__age)

# class child(player):
#     def __init__(self,ne,gme,ag):
#         super().__init__(ne,ag)
#         self.game = gme
        
#     def print_game(self):
#         print(f'The game played by {self.name} is',self.game)
        
#     def print_age(self):
#         print('Age of player is:', self.__age)


# player1 = child('Ronaldo','Football',28)

# player1.print_name()
# player1.print_game()
# player1.print_age()

'''WAP to implement linked lists in python using classes'''
class node():
    def __init__(self,d_val):
        self.dataval = d_val
        self.next_val = None
    
class LinkedList():
    def __inti__(self):
        self.head = None
    
    def print_list(self):
        printval = self.head
        while printval is not None:
            print(printval.dataval)
            printval = printval.next_val
        
list_1 = LinkedList()
e1 = node('Mon')
e2 = node('Tue')
e3 = node('wed')

list_1.head = e1
e1.next_val = e2
e2.next_val = e3

list_1.print_list()