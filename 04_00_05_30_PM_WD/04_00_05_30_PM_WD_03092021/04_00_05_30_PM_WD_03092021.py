d = {'a':10,2:20,'b':30,4:40,'c':50}

# Wap to print key from value
n = len(d)
value = 30
index = 0
val = list(d.values())
key = list(d.keys())
for i in range(n):
    if val[i] == value :
        index = i
        break

print(key[index])


print(list(d.keys())[list(d.values()).index(40)])
p =[[j for x in range(1,3)] for j in range(3)]
print(p)
l = []
for x in range(10):
    l.append(x)

print(l)

x_ = []
for j in range(3):
    l = []
    for x in range(1,3):
        l.append(j)
    x_.append(l)
print(x_)

m_4_3 = [x for x in range(31) if x%3 ==0 and x%4 ==0]
print(m_4_3)
num = 3
prime_num = True if len([x for x in range(1,num//2) if num%x == 0]) < 2 else False
print(prime_num)
s= 0
add = [s+x for x in range(num) ]
print(add)