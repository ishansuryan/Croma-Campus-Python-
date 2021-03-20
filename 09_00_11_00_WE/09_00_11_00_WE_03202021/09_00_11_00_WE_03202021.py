from collections import Counter
l = [[1,10],[2,200],(3,3000)]
l2 = (['hi','how are you'],)
d = dict(l)
print(d)
d2 =dict(l2)
print(d2)
l3 = (['a','apple'],)
print('Type of l3 is',type(l3))

# d1 = {'a':100, 'b':200, 'c':400}
# d2 = {'a':200, 'b':350, 'd':550}
# d3 = Counter(d1)+Counter(d2)
# print(type(d3),d3)

print(list(d.keys())[list(d.values()).index(200)])
find = 100
for i,j in (d.items()):
    if j == find:
        print(i)
        break
else:
    print('not found') 
    
# WAP to find wether a number is armstrong or not

n_ = 153
n= list(str(n_))
s= 0
pow= len(n)
for i in n:
    s+=int(i)**pow
if s == n_:
    print(f'Number {n_} is an armstrong number')
else: print(f'Number {n_} is not an armstrong number')

fib = [0,1]
n = 2
if n == 0:
    print(f'fib {n} is:', 0)
elif n == 1:
    print(f'fib {n} is:', 1)

else:
    for i in range(1,n):
        fib.append(fib[-1]+fib[-2])

print(fib[-1])

def fibb(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return fibb(n-1) + fibb(n-2)

print(fibb(10))