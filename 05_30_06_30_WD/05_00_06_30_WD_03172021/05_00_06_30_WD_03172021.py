# pattern no 2
n = 5
# for row in range(n):
#     for space in range(n-row-1):
#         print(end =' ')
#     for start in range(row+1):
#         print(end ='*')
#     print()
    
# for row in range(n):
#     print(' '*(n-row-1)+'*'*(row+1))
    
# # pattern no. 4
# print()
# for row in range(n):
#     for space in range(row):
#         print(end =' ')
#     for start in range(5-row):
#         print(end ='*')
#     print()

# print('pattern no. 5')

# for row in range(n):
#     for space in range(5-row-1):
#         print(end =' ')
#     for start in range(row+1):
#         print(end ='*')
#     for star in range(row):
#         print(end = '*')
#     print()
    
# print()

# for row in range(n):
#     for space in range(5-row-1):
#         print(end =' ')
#     for start in range(2*(row+1)-1):
#         print(end ='*')
#     print()
    
# print('pattern No. 8\n')

# for row in range(n):
#     for star in range(row+1):
#         print(end='*')
#     print()
# for row in range(n-1,0,-1):
#     for star in range(row):
#         print(end='*')
#     print()

print('pattern no.9')
for row in range(n):
    for space in range(n-row-1):
        print(end =' ')
    for start in range(row+1):
        print(end ='*')
    print()

for row in range(n-1):
    for space in range(row+1):
        print(end =' ')
    for start in range(5-row-1):
        print(end ='*')
    print()