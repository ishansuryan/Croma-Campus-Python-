# for row in range(5,0,-1):
#     for space in range(5,row,-1):
#         print(' ',end='')
#     for star in range(row):
#         print('*', end='')
#     print()
   
# for row in range(5):
#     for space in range(5-row-1):
#         print(' ',end='')
#     for star in range(2*row +1):
#         print('*', end = '')
#     print()
    

# for row in range(9):
#     for space in range(9-row-1):
#         print(end= ' ')
#     for number in range(row+1):
#         print(number+1, end= '')
#     for reverse_number in range(row,0,-1):
#         print(reverse_number, end ='')
        
#     print()
    
for row in range(5,0,-1):
    for space in range(5-row):
        print(end = ' ')
    for star in range(2*row-1):
        print('*', end = '')
    print()   