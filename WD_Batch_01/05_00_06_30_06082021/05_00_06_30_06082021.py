# Sets

s = {1,2,3,4,5,6,1,2,3,4,5,6}
print(s)

s1 = set()
print(type(s1))

st = 'google'
abc = set(st)           # creating a set from strings
d = {}

for i in abc:
    d[i]= st.count(i)
    
print(d)

s.add(7)                # adding the element ot set at line no.3
print(s)

s2 = {1,2,4,6,8,9,10}

s3 = s.difference(s2)
print(s3)

s3.discard(5)
print(s3)

s4 = s.intersection(s2)
print(s4)

print(s.isdisjoint(abc))

s2.remove(9)
print(s2)

s.update(s2,s3,abc)
print(s)