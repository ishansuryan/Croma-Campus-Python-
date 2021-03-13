l = [1,2,3,4,5,6]
x = l.reverse()
print(type(x))
print(l+l)
l.reverse()
print(l)
import random
random.seed(10)
random.shuffle(l)
print('after shuffling the l is:',l)
l.sort()
print('after sorting the l is:',l)

addition = 0

for i in l:
    addition += i

print(addition)

l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l2 = l.copy()
# l1 = []
# for index in range(len(l)):
    
#     for i in range(len(l)-1):
#         if l[i][1]>l[i+1][1]:
#             l[i], l[i+1] = l[i+1],l[i] 

# print(l)
# print(l2)
# l2.sort(key = lambda x:x[1])
# print(l2)

l3=[]
for i in l:
    l3.append(i[1])
print('l3 is:',l3)
l3.sort()
print(l3)
l4 = []
for j in range(len(l)):
    for i in range(len(l)):
        if l3[j] == l[i][1]:
            l4.append(l[i])
            break
    
print(l4)