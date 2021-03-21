# sets
# st = {1,2,3,4,5,6,1,2,3,4,5,6,1,1,1,1,1,1,'1234'}
# st.add(10)
# print(len(st))

# stt =set()   # defining an empty set

# print(type(stt))
# t = ('hello', 'how are you')
# s1 = set('hello, how are you')
# print(s1)

# print(set(t))
# s2 =set('the quick brown fox jumpes over the lazy dog')
# print(s2)

# a = {1,2,3,4,5,6,7}
# b = {4,5,6,7,8,9,10} 

# # c = a.difference(b)
# # print('line no 21:',c)
# # c = a-b
# # print(a-b)
# # c = a.difference_update(b)
# # print(a)

# # a.discard(1)
# # print(a)

# c = a & b           # bitwise and 
# print('line no 31 and:',c)

# d = a|b             # or 
# print('line no 34 or:',d)

# e = a^b
# print('line no 37 xor/ exclusive or :',e)

# f = a.symmetric_difference(b)
# print(a)

# g = a.union(b)
# print(g)

# h = a | b
# print(h)
def standard_input():
    yield 'a'


# Error Handling

l = [1,2,3,4,5,6]
# print(l.pop(20))
try:
    print(l.pop(20))
    
except KeyError:
    print('running with error at line 54')
    
# except IndexError:
#     print("Resolved index error")
    
except :
    print("Error tackled")
    
finally :
    print("runs all the time")
    
a = input("Enter the number")
# a= int(a)
# if a.isalpha():
#     raise Exception ("Please enter a number not alphabets")

import sklearn



    