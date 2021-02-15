print('Hello world!','there is a wall')
print('How are you?')

a = 10
print(type(a))          # type command gives which type of variable it is

a = 1.20
print(type(a))

a = '1.2'
print(type(a))

a = True
print(type(a))

a = complex(1,5)
print('value of a is:', a , '\nType is:', type(a))

# String Formatting

# best and most versatile way for string formatting

# for i in range(1,11):
#     print('The number is {1:<2} the square is {2:^3} the cube is {0:>4}'.format(i**3,i,i**2,))

# Some other ways for string formatting

# for i in range(1,11):
#     print(f'The number is {i:<2} the square is {i**2:^3} the cube is {i**3:>5}')



# pi = 22/7

# print(f"{pi:.60f}")

string = "The quick brown fox jumped over the lazy dog"

# syntax of indexing :---> iterable[index number]

print(string[10])

# syntax of slicing :-----> iterable[start value:endvalue:step value] (end value is not included) by default step is 1

print(string[0:10:2])

print(string[-1])

'''Rules of indexing The start limit ia always smaller than end limit'''

print(string[-15:-10])

print(string[-1:-10:-1])

print(string[20:50])

print(string[-44:])

print(string[:20])

print(string[::-1])