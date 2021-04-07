# Sets 

a = {1,2,3,4,5,6,1,2,3,4,5,6}
print(a)
print(type(a))

# l = [1,2,3,4,5,6,2,3,6,5,4,1]
# l = list(set(l))
# print(l)

a.add(10)
print(a)

b = {6,7,8,9,10,11}

c = b.difference(a)
print(c)

c = a.intersection(b)
print(c)

d = {12,13,10}

print(a.isdisjoint(d))

e = {2,3,6,5}
print(e.issubset(a))

e.remove(2)
print(e)


d = {1:10,3:30,2:20}

sort_keys = list(d.keys())
sort_keys.sort()
print(sort_keys)

d[5]=50

print(4 in d)