# Wap to find the sumof series 1 + 1/2 + 1/3 + ...... + 1/n
standard_input = [3,100,1,10]

# n = input("Enter the value of n")

# s = 0

# for i in range(1,n+1):
#     s += 1/i

# print(s)


# # wap to find value of e formulae = 1 + 1/1! + 1/2! + .... + 1/n!

# def fact(n):
#     m = 1
#     for i in range(1, n+1):
#         m *= i
    
#     return m    
# n = input("Enter the value of n")
# s = 1
# for i in range (1,n+1):
#     s += 1/fact(i)

# print(s)


# wap to find the pythagorean triplets in a range

# start = int(input('Enter start value'))
# end = int(input('Enter end value'))
# triplets = []
# for n1 in range(start,end-1):
#     for n2 in range(n1+1, end):
#         for n3 in range (n2 + 1, end +1):
#             if (n1**2) + (n2**2) == n3**2:
#                 triplets.append((n1,n2,n3))

# print(triplets)


# Classes

class player():
    def __init__(self, nme):
        self.name = nme
    
    def print_name(self):
        print(self.name)
        
    def rev_name(self):
        print(self.name[::-1])
        
        
# p1 = player('Ronaldo')
# p1.print_name()

# p2 = player('Virat Kohli')
# p2.print_name()

# p2.rev_name()


class student(player):
    def __init__(self, nme, class_, section):
        super().__init__(nme)
        # self.name = nme
        self.cls = class_
        self.section = section
        
    # def get_name(self):
    #     return self.name
    
    def get_c(self):
        return self.cls
    
    def get_section(self):
        return self.section
        

s_0410_2021 = student('Roshan', '10', 'E')

s_0410_2021.print_name()
print(s_0410_2021.get_c())