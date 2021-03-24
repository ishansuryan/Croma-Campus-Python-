# n = 5
# for row in range(n):
#     for column in range(n):
#         if row == 0 or row == n-1 or column == n-row-1:
#             print(end = '*')
#         else :print(end = ' ')
#     print()
# print()
# for row in range(n):
#     for column in range(n):
#         if column == 0 or column == n-1 or column == row:
#             print(end = '*')
#         else :print(end = ' ')
#     print()

# While Loop
# x = 0
# while x < 10:
#     print(x)
#     x+=1
standard_input = ['n','a','yes', 'q','North']
l = ['north','east', 'west','south']

# # inpt = '!'
# while True:
#     inpt = input("Enter the exit").lower()
#     if inpt in l:
#         break
i =0
y = '!'
while i<3:
    i+=1
    y = input('Enter')
    if y == 'q':
        print('you win')
        break

else : 
    print('game over')
