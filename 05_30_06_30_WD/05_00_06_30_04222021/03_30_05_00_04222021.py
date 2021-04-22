class node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
class linked_list():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval= printval.next

link = linked_list()  
link.head = node('Mon')
e2 = node('Tue')
e3 = node("wed")

link.head.next = e2
e2.next = e3

link.print_list()


