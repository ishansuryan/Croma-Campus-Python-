# s = 'the quick brown fox jumps over the lazy dog.'
# print(s.rfind('o'))

# s1 = 'hey. \nhow. wh\nere are y\nou?'
# print(s1.rjust(30,'-'))

# print(s1.rpartition('h'))

# print(s1.rsplit('w'))
# print(s1.split('e'))
# print(s1.splitlines(keepends=True))

# print(s1.startswith('hey. \n'))
# s2 = 'hEy HoW aRE you Doing?'
# print(s2.swapcase())
# print(s2.title())

# s3 = 'Go'
# print(s3.zfill(10))
def standard_input():
    yield 3
a = 10
b = 3.8
c = a+b
print(c)
a = 1.0
print(type(a))
# int(a)
print(int(a))
print(int(b))

print(a*b)
b = 3
print(a/b)
print(10//5)
print(int(a%3))

# Conditional Execution of statements:
a = 5
# Syntax if condition:
if a<2:
    print('Yes')
    print('smaller than 2')
elif a<5:
    print('Smaller than 5')
else:
    print('NO')
    
d = input('Enter the number')
print("you entered the value", d)

d = int(d)

a = 2
b = 'hello'
print('a before:',a )
print('b before:',b)

a,b = b,a

print('a after:',a)
print('b after:',b)

if d%2 == 0:
    print('number id even')

else: 
    print('number is odd')