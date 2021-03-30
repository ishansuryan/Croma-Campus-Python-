# with open(r"E:\Croma-Campus-Python-\04_00_05_30_PM_WD\03_30_05_00_WD_03302021\testing.txt", 'w') as file:
#     file.write('Hello how was you festival')
#     file.write('Mine was good')
#     print('complete')

# with open(r"E:\Croma-Campus-Python-\04_00_05_30_PM_WD\03_30_05_00_WD_03302021\testing.txt", 'r') as file:
#     print(file.readline())

# x = file.readlines()

class student():
    def __init__(self, nme ,cls, sec, rol_no):
        self.name = nme
        self.class_ = cls
        self.section = sec
        self.roll = rol_no
    
    def get_name(self):
        print(self.name)
    

s_03302021_20 = student('Rahul', 8, 'C', 10)

s_03302021_20.get_name()

class old_student(student):
    pass

a_10 = old_student('Chandan',12, 'A',12)

a_10.get_name()