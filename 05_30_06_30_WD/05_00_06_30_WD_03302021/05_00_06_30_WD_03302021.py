l = [1, 2.3, '30', ['hi','hp',[10,20]]]
print(type(l))
print(l[0])
print(l[3][2][0])

'lists are mutable'

a = [1,2,3,4,5,6,7,8,9]
b = a

print('id of a is:',id(a))
print('id of b is:',id(b))

b[2] = 60
print(a)
print('id of b is:',id(b))

st_a = 'hello'
st_b = st_a
print('id of st_a is:',id(st_a))
print('id of st_b is:',id(st_b))
st_b = 'hheelloo'
print(st_a)
print('id of st_b is:',id(st_b))

l1 = list(range(11))
print(l1)

print(range(11))

l2 = [range(11)]
print(l2)

l1.append(60)
print(l1)

l = list('hello how are you?')
print('line no:38-->',l.count('o'))

l2.extend([20,50,81,20])
print('line no:41-->',l2)

print(l2.index(20))
l2.insert(2,100)
print('line no. 45', l2)

var = l2.pop(3)
print(var, l2)

srt = [10,2,30,5,1,0,2]
srt.sort(reverse=False)
print(srt)