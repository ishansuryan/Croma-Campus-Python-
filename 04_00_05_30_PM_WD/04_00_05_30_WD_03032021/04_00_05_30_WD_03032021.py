l = [2,3,3,5,2,5,6,9,8,7,8,2,8]
f = []
for i in l:
    if i not in f:
        f.append(i)
print(f)
# method 1
l1 = l.copy()
l2 = l[:]
print(id(l), id(l1), id(l2))
n = []

# if len(l) == 0:
#     print('List is Empty ')
    
x = 'List is empty' if not n else 'List is full'
print(x) 

n = 4312539425856
print(int(str(n)[::-1]))

n= 122251
sum = 0
for i in str(n):
    sum += int(i)
print(sum)
n = 'Nitin'
print('number is palinderome' if str(n).casefold() == str(n).casefold()[::-1] else 'number is not a plaindrome')

factors = []

n = 11

for i in range(1, n //2 ):
    if n%i == 0:
        factors.append(i)
        factors.append(n//i)

if len(factors)<3:
    print("Number is prime")
else: 
    print('number is not prime')