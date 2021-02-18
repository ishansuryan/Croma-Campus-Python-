# for i in range(1,11):
#     print(f'2X{i}={2*i}')
# print('Loop Has ended')

# s = 'hello'
# for i in s:
#     print(i)
    
# for i in range(20,51):
#     if i%2 != 0:
#         print(i,"is odd")

for i in range(5):
    for j in range(i+1):
        print('*',end = '')
    print()
    
for row in range(5):
    for space in range(5-row-1):
        print(' ',end='')
    for star in range(row+1):
        print('*',end='')
    print()
print()
for i in range(5):
    for j in range(i,5):
        print('*',end='')
    print()

print() 
for i in range(5,0,-1):
    for j in range(i):
        print('*',end= '')
    print()       