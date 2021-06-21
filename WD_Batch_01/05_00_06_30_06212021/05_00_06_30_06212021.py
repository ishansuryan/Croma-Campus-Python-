# Iterators & Generators

# def itr():
#     for i in range(1,11):
#         yield i
        
# x = itr()
# i = next(x)

l = [1,2,3,4,5,6,7,8,9]
l_ = iter(l)
print(l_)

for i in l_:
    print(i)
    
def sq(e):
    return e**2

l = [1,2,3,4,5,6,7,8,9]
l_sq = tuple(map(sq,l))

print(l_sq)

l_str= list(map(str,l))
print(l_str)

l_1 = [1,2,3,'4','5',6,'7','8','9']

# def seprator(e):
#     if type(e) == str:
#         return True
#     return False   

# l1_str = list(filter(seprator,l_1))
# print(l1_str)

# lmbda function : un-named single line function syntax use lambda word

l1_str = list(filter(lambda e:True if type(e)==str else False, l_1 ))
print(l1_str)

l_2 = [(2,1),(3,5),(6,2),(9,8),(4,3)]

l_2.sort(key = lambda x:x[1])
print(l_2)

# List Comprehension syntax [expression for var in iterable]

l = [x  for x in range(1,10) if x%2 ==0]
print(l)

# dictionary comprehension

d = {x:x**2 for x in range(1,11)}
print(d)