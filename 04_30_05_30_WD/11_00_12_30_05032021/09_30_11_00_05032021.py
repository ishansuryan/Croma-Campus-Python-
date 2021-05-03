# While loop
# gate = ['north', 'east','west', 'south']
# i = 1
# while i !='quit':
#     i = input('Enter gate: ').lower()
#     if i in gate:
#         print('you got the right exit')
#         break
#     # elif i =='quit':
#         # print('are you sure you want to quit? y|n: ', end ='')
#         # z = input()
#         # if z == 'y':
#         #     break
#         # else :
#         #     continue
#     # print(i)
# else :
#     print('loop ended normally')


import time

start = time.time()
for i in range(1500,2701):
    if i % 7 == 0 & i % 5 == 0:
        print(i,end = ',')
stop =time.time()
print()
print(f'time taken is: {stop -start:.10f}')


start = time.time()
for i in range(1500,2701,5):
    if i % 7 == 0:
        print(i,end = ',')
stop =time.time()
print()
print(f'time taken is: {stop -start:.10f}')

num = 1500
start = time.time()
while num <=2700:
    if num % 7 == 0:
        print(num, end =',')
    num+=5

stop = time.time()
print()
print(f'time taken is: {stop -start:.10f}')

num = 1500
start = time.time()
while num <=2700:
    if num % 7 == 0:
        print(num, end =',')
    num=num +5

stop = time.time()
print()
print(f'time taken is: {stop -start:.10f}')