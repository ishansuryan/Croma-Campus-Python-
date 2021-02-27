class parrot():
    def fly(self):
        print('parrot can fly')
    
    def swim(self):
        print("Parrot can't swim")
        
class penguin():
    
    def fly(self):
        print("panguin can't fly")
    
    def swim(self):
        print("Panguin can swim")


def flying_test(bird):          # polymorhism : ability to use use a common interface for multiple forms.(data types)
    bird.fly()


mitthu = parrot()
jack = penguin()

flying_test(jack)
flying_test(mitthu)
