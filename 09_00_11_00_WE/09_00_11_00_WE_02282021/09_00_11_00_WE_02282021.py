'''syntax of for loops 

for variable in iterable:
    code to be run number of times/ iterated over'''

# s = 'hello'
# print('pattern 1')
# for i in s:
#     print(i)

# print()
    
# for i in range(1,5):
#     print(i, (s+' ')*(i))

'''
****
****
****
'''
print('pattern 1')
# r = 7
# c = 9 
# for row in range(r):
#     print(row, end = '->')
#     for column in range(c):
#         print(column ,end = '')
#     print()

for row in range(5):
    print('*'*(row+1))
    # for star in range(row +1):
    #     print('*', end = '')
    
    # print()
print('Pattern 2')
for row in range(5):
    print(' '*(5-row-1)+ '*'*(row+1))
    
'''
ss1
s23
456    by default end =
'''
n = 1
for row in range(3):
    for column in range(3-row-1):
        print(end= ' ')
    for num in range(row+1):
        print(n, end = '')
        n+=1
    print()
    

print('Pattern 3')

for row in range(0,5,1):
    for column in range(5-row):
        print('*', end = '')
    print()

for r in range(5):
    print('*'*(5-r))


print('Pattern 4')    

for row in range(5):
    for space in range(row):
        print(end =  " ")
    for star in range(5-row):
        print('*', end = '')
    print()