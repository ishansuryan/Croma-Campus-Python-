print("hello world",'there ',end = '  ',sep = '->')
print('hi')

a ='10.2'
print(type(a))

a = 10
print(type(a))

s = "Hi there how are you?"
print(s[3:8:3])
print('start value grater than end ',s[8:3])

# actual stntax of slicing is datetime A combination of a date and a time. Attributes: ()
# [Start limit:Endlimit(not included):step size]
# Start value is always smaller than end value

print(s[-20:-10]) # -ve indexing

print(s[-10:-20:-1]) # negative indexing with negative stp

print(s[15:25])

print(s[-21:])
print(s[0:])

print(s[:10])
print(s[::-1])

s = 'hi how'
print(s.capitalize())

s = 'hI hOW aRE YoU? hi hhhhh'
print(s.casefold())
print(s.count('h'))
print(s.endswith(('h')))
print(s.find('hi'))

s = 'Python'
print(s.center(20, '-'))




 