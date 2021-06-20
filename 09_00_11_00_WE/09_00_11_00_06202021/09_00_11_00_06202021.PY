# lists Operations

l = [1,2,3,4,5,6]
l.append('Hello')
print('l is:->',l)
l.append(['HI',20,20.2])
print(l)
l2 = [1,2,3,4,5,6]
l2.extend('Hello')
print('l2 is:->',l2)
l2.extend(['HI',20,20.2])
print(l2)

print('l count in l2 is:->',l2.count('l'))
print('index of l in l2 is:->',l2.index('l'))

l2.insert(3,'HI there')
print('line no.18 ',l2)

returned_val = l2.pop(3)
print(returned_val)
print('line no 22 ',l2)
l2.reverse()
print('l2 after reversing',l2)
# l2.sort()
l2.clear()
print('l2 is:->',l2)


'Write a Python program to sum all the items in a list.'
l = [1,2,3,4,5,6]
result = sum(l)
print(result)

' Write a Python program to get the largest number from a list'
l.sort()
print(l[-1])

# Write a Python program to count the number of strings where the 
# string length is 2 or more and the first and last character are 
# same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']

l = ['abc', 'xyz', 'aba', '1221']
counter = 0
for i in l:
    if len(i)>=2 and i[0]==i[-1]:
        counter+=1

print(counter)

# Write a Python program to remove duplicates from a list.

l = [1,2,3,4,5,6,1,23,4,5,6,7,8,9,1,1,32,3,12,3]
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)
        
print(new_l) 

# Write a Python program to check a list is empty or not.

# Write a Python program to find the list of words that 
# are longer than n from a given list of words

l = ['hi','hello','there','hii','bye','quit', 'dot']
new_l =[]
for i in l:
    if len(i)>=3:
        new_l.append(i)

print(new_l)