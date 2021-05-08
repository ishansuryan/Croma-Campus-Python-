# gate = ['north','east','west','south']


# user_ans = ''

# while user_ans != 'quit':
#     user_ans = input('Enter the gate or type "quit" to quit the game: ').lower()

#     if user_ans in gate:
#         print('You got the gate you can now leave')
#         break
    
#     elif user_ans == 'quit':
#         print('Are you sure you want to quit')
#         answer = input('Enter y for yes or n for no:->')
#         if answer == 'y':
#             print('Ok you quit the game')
#             break
#         else : 
#             user_ans = ''

# Lists

l = []
print(type(l))

s = "hello world"

s_l = list(s)
# print(s_l)
# print('Type s_l is :', type(s_l))

# print(s_l[::-1])
# print(s_l)
# s_l.reverse()
# print(s_l)

# s_l.reverse()
# print("line no. 39:", s_l)
even =[]
for i in range(101,201):
    if i%2 == 0:
        even.append(i)

# print(even)

print(s_l.count('h'))

l2 = [1,2,3,4,5,6,'h']
# s_l.append(l2)
# print(s_l)
s_l.extend(l2)
print(s_l)

print(s_l.index('o'))
s_l.insert(2,'hieee')
print(s_l)

re = s_l.pop(2)
print(s_l)
print(re)

s_l.remove('o')
print(s_l)
l2 = [1,3,2,6,7,9,5,4,0]
l2.sort(reverse=True)
print(l2)