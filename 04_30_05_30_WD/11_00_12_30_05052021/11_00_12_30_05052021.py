l = [1,2,3,4,5,6,7,8,9,13,13,1]
print(len(l))
l2 = [11,12,13,14]

# l.append(l2)
# print(l, len(l))

l.extend(l2)
print('L is:', l)

# l3 = l.copy()
# l3[0]= 1000

# print(l3)
# print('l is: ',l)
# print(l3.index(1000))

l.insert(3, 200,)
print('L ig :',l)

remove = l.pop()
print(l)

print('Pop is', l.pop(3))
print(l)

l.remove(13)
print(l)
l.reverse()
print(l)

l.sort(reverse = True)
print(l)

l[2] = 200