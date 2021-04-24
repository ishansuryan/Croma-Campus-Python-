class grand_father():
    def same(self):
        print('Grand father function')
        
class father():
    def same(self):
        print('Father function')
        
class child(grand_father, father):
    def out(self):
        print('child function')
        
n1 = child()

grand_father.same(n1)
father.same(n1)

# lambda function

x = [(1,2),(2,1),(5,2),(6,10),(10,6)]
# def second(x):
#     return x[1]
x.sort(key =lambda x: x[1])
print(x)

l = ['1','2',"3",'4','5','6.2','7','8',9]
l = list(map(lambda x: float(x)+10, l))
# filter()
l1 = [x**2 for x in l]
print(l,l1)

l3 = [1,2,3,4,5,6,7,8,9]
# l3 = list(map(lambda x : x**2 , l3))
# print(l3)

# l3 = list(filter(lambda x: x%2 ==0, l3))
# print(l3)

l3 = [x for x in l3 if x%2 ==0 ]
print(l3)

d1 = {1:10,2:20,3:30,4:40,5:50}
d2 = list(filter(lambda x : x if x%2 != 0 else False , d1.keys()))
print(d2)
