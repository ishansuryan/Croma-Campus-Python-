# for loops

# syntax: for variable in iterable:
# s = 'Hello world'
# for var in s:
#     print(var)
#  Pattern No 1   
for row in range(5):
    for column in range(row+1):
        print('*',end = '')
    
    print()
    
# Pattern No 3
for r in range(5):
    for s in range(4-r):
        print(end=' ')
    for star in range(r+1):
        print(end = '*')
    
    print()
    
# pattern 4
print('pattern 4')

for r in range(5):
    for space in range(r):
        print(end=' ')
    
    for star in range(5-r):
        print(end = '*')
    
    print()

# pattern 5
print('Pattern 5')
print()
for r in range(5):
    for space in range(5-r):
        print(end =' ')
    
    # for star in range(r+1):
    #     print(end = '*')
    
    # for star2 in range(r):
    #     print(end = '*')
    
    for s in range(2*r+1):
        print(end = '*')
    print()