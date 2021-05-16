from datetime import date, datetime

curr = datetime.now()

print(curr)

print(curr.strftime("%d/%B/%Y  %H:%M:%S %p"))

# file handling

file = open('file.txt','r+')
print()
# print((file.readline()))
file.read()
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())

file.write('Jawed,1000\n')

file.close()
