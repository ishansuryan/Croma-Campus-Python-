# file = open('Files1.txt', mode = 'w')
# # print('Hello world!, how are you?', file = file, flush = True)
# file.write('how are you?, Hello world!\n today is your lucky day')
# file.close()

# f = open('Files1.txt', mode = 'r')
# print(f.read())
# print('ok')


from calendar import calendar
x = calendar(2021)

# y = x.replace(' ',',',)
# print(y)

file = open('Files.csv', 'r')
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())
# file.write(x)
# file.close()

# print('the calendar is:\n',x)
# file = open('Files.csv', mode = 'r')
# r = file.read()
# file.seek(0)
# print(file.readlines())
# file.close()
# r = r.split(' ')
# print(r)