# l = (1,2,3,4,5,6)

# l2 = ('1',[2,3],{},(3,),True)

# print(type(l))

# b = (1,)
# print(type(b))
# print(len(b))

# l1 = 'hello'
# v = tuple(l1)
# print(type(v))

# print(help(tuple))

standard_input = [1,10]
# print(l2>l)

# error handling

# a = int(input('Enter number'))
# b = (input('Enter number'))


# try:
#     print('The devision is',a/b)
#     print('zzz')

# except ValueError:
#     print('Please provide a value')

# except TypeError:
#     print('2 different types of data types are privided')
    
# except ZeroDivisionError:
#     print('devision by zero is not defined')

# except:
#     print('Error Handling')

# finally :
#     print('Finally executed')

# import numpy as np

# print(np.__version__)

# assert np.__version__ >='1.20.2', 'Numpy Version is Lower than required please update'
# print('after assertion print command')
# if a<b :
#     raise ValueError( 'A should be smaller than B')


# List Comprehension syntax:-> expression for variable in iterable
# treditoinal way
x = []

for i in range (1,11):
    x.append(i)
print(x)
# List Comprehension Way
#                  expression              for    variable   in     iterable
y = [var if var%2 ==0 else f'odd->{var}'   for    var        in   range(1,11) ]
print(y)

square_dic = {i: i**2 for i in range(1,11)}
print(square_dic)