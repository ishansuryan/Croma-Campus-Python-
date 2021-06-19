# While Loop : is used when we dont know how many times the loop needs to run.
# Syntax : While condition   # condition which Risults in True or False

# gates = ['north', 'east', 'west','south']

# var = '!'

# while var not in gates:
    
#     var = input('Enter the gate: ').lower()
    
#     if var == 'q' or var == 'quit':
#         print('are you sure you want to quit enter y/n: ',end = '')
#         var = input().lower()
        
#         if var == 'y':
#             break
#         else :
#             continue
    
#     if var in gates:
#         print('you choose correct Exit you Win!!')
    
#     else:
#         print('Wrong exit try again or enter q/quit to exit the game')
        
''''NoRTH,NorTh'''
# Wap to print table of given number upto 10 using while loop

# num = int(input('Enter Number Whose table is needed: '))
# i = 1
# while i <=10:
#     print(f'{num} x {i:2} = {num*i}') 
#     i +=1
    
# WAP to find the factorial of given number using while loop

factorial = 1
i = 1
number = 3
while i<=number:
    factorial *= i
    i+=1
print(factorial)

# Lists: is a collection of multiple elements (can be different types)
# under one name. Lists are mutable
# Defining a list
l = []              # defining a empty list
s = 'Hello'
l1 = list(s)        # creating a list out of other iterables
print('l1 is:->',l1)
print(l1[1])

# proof of lists are mutable 
a = l1
print('id of a is:->', id(a))
a[0] = 'Z'
print('id of l1 is:->',id(l1))
print('a is',a)
print('l1 is',l1)

b = s
print('id of b is :->', id(b))
print('b is:->', b)
# b[0]= 3
b = 2
print('id of b is->',id(b))
print('b is:->',b)
print('s is:->',s)


# iterating or accessiing elements of list

l = [1,2,3,4,5,6]

for i in l:             # i will take all values in list one by one
   print(i)

for i in range(len(l)):             # accessing elements of list using indexing
    print(l[i])

# Wap to find the sum of all elenst of given list
s = 0
for i in l:
    s+=i
print(s)