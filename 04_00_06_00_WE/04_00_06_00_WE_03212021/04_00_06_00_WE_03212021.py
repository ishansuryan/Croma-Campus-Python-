print("Hello world",end = '--->')
print('How are you?','I am doing good', sep = '//..//')

s = 'The quick brown fox jumps over the lazy dog'
#    01234
print(s[4])
print(s[-1])
print(s[4:9])
print(s[::2])
print(s[::-1])

a = 10
print('line no 13',type(a))
a = '10'
print('line no 15',type(a))
a = 10.20
print('line no 17',type(a))
a = True
print('line no 19',type(a))
a = complex(2,3)
print('line no 21',type(a))
print(a)
a = None
print('line no 24',type(a))

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 
print(a//b) # quotient
print(a%b)  # remainder
print(a**b) # power

print(a/b*a)
print('-'*30)
print('dd'+'hh')

# devide any two numbers and dsiplay risult as int
#standard_input = [10,20,30]
print(int(a/b))

d = int(input("Enter the number,,,: "))
print(a/d)
c = input("Enter the number: ")
print(c)