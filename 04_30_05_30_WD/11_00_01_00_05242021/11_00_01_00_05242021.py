# classes
# Multilevel Inheritance
class grand_father():
    def __init__(self,nme):
        self.name = nme
        # self.age = ae
        # self.constant = 'CONSTANT VARIABLE'
    # value = 'First'
    # value_1 = 1

    def prt_nme(self):
        print(self.name)
        # print(self.constant)

class father(grand_father):
    def __init__(self,nme,ag):
        super().__init__(nme)
        self.age = ag
    
    def prt_age(self):
        print(self.age)


class child(father):
    def __init__(self, nme, ag, gme):
        super().__init__(nme, ag)
        self.game = gme
    
    def prt_gme(self):
        print(self.game)

c = child('Dhoom Ketu',20,'football')
c.prt_nme()
c.prt_age()
c.prt_gme()

    
# v1 = grand_father('Dhoom Ketu', 21,'c')
# v3 = grand_father('Prince',25,'')

# v1.prt_nme()
# v1.prt_age()

# v3.prt_nme()
# v3.prt_age()


# Multiple Inheritance
class grand_father_1():
    def __init__(self,nme):
        self.name = nme
        # self.age = ae
        # self.constant = 'CONSTANT VARIABLE'
    # value = 'First'
    # value_1 = 1

    def prt_nme(self):
        print(self.name)
        # print(self.constant)
    def PRINT(self):
        print('Inside Grandfather function')

class father_1():
    def __init__(self,ag):
        self.age = ag
    
    def prt_age(self):
        print(self.age)

    def PRINT(self):
        print('Inside father function')


class child_(grand_father_1,father_1):
    def __init__(self, nme, ag, gme):
        grand_father_1.__init__(self,nme)
        father_1.__init__(self,ag)
        # super().__init__(nme, ag)
        self.game = gme
    
    def prt_gme(self):
        print(self.game)

c1 = child_('Shwet Ketu',20,'football')
c1.prt_nme()
c1.prt_age()
c1.prt_gme()   
c1.PRINT()