'''
loops : when we need to do same thing multiple times than we use loops

Tpes of Loops 
1) for loop 
2) while Loop

Syantax for for loops: 
for variable_name in iterable: <- this colon indicates the starting of loop
    <- this indent indicates that command is inisde loop and will be executed in every cycle of loop to take a command out of loop
    just remove the indent.
'''
# s = 'Hello World'

# for i in s:
#     print(i)  
    
# for i in range(10):
#     print(i)
    
# # Wap to print a table of 2 using for loop

# for i in range(1,11):
#     # print(f'2 X {i} = {2*i}')
#     print('2 X {:2} = {:2}'.format(i,2*i))

# print()

# for i in range(10,0,-1):
#     # print(f'2 X {i} = {2*i}')
#     print('2 X {:2} = {:2}'.format(i,2*i))
    
# for num in range(2):                            # loop inside loop is called nested loop
#     for i in range(1,11):
#         # print(f'2 X {i} = {2*i}')
#         print('2 X {:2} = {:2}'.format(i,2*i))
# print()
#%% [markdown]
# <img src= "/mnt/New_Volume/Work_From_Home/Croma_Campus/06132021/09_00_11_00_06132021/Star-Pattern-Programs.png"/>


for row in range(5):
    for column in range(row+1):
        print('*', end = '')
    print()
    
print('pattern No:3')
for row in range(5,0,-1):
    for column in range(row):
        print('*', end = '')
    print()

# pattern no 2:
print('pattern No.4\n')
for row in range(5):
    for space in range(5-row-1):
        print(" ", end ='')
    for star in range(row+1):
        print('*', end = '')
    print()