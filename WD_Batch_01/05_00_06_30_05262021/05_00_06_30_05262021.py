s = 'Hello world'

# for loops 
# syntax:
# for variable in iterable:
for i in s:
    print(i)
    if i == ' ':
        break  
print(s)

for i in range(10):
    if i%2 !=0:
        continue
    print(i)