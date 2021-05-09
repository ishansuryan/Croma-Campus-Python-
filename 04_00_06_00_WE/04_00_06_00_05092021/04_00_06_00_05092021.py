a = {'one':100,'to':3000}
print(type(a))

a['one'] = 10

print(a)

l = [['two',20],['one',10],['three',30]]
d = dict(l)
print(d)

c = d

c['one'] = 1000
# print(d)

print(d.get('onee','Value Not Present in dictionary'))

# print(d.keys())
# print(d.values())
# print(d.items())
x = d.pop('three')
# print(x,d)
y = d.popitem()
# print(y)
d.setdefault('four',30)
# print(d)
d.update(a)
# print(d)

x = list(d.values())
# print(x)
# x.sort()
# print(x)
# list(d.keys())
# print(list(d.items()))
x = list(d.items())
print('x is', x)
di = {}
for i in range(len(x)):
    for j in range(i,len(x)):
        if x[i][1] > x[j][1]:
            x[i],x[j] = x[j],x[i]
    # if y not in list(di.items()):
    #     di[y[0]] = y[1]

print(dict(x))
    

# a = (10,20)
# print(type(a))
# print(a[0])
# # a[0]=100
# l = [10,20,35]
# a =tuple(l)
# print(a)