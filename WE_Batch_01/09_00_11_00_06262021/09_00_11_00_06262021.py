# Tuples : Immutable list
# Syntax: (Anything inside)
# a = (10,)
# print(type(a),a)

# b =tuple([20])
# print(b)

# # print(help(tuple))

# tup = tuple('Hello')

# for i in tup:
#     print(i)
    
# tup[1] = 'E'

# Dictionaries : does not have order. It has key value pairs.
# Synatx : {key:value, key2:value2...}
# key will always be an immutable element

d = {'a':10,'b':1}

# accessing a dictionary:

print(d['a'])

e ={}       # creating an empty dictionary
# Wap to create a dictionary and print any one of the values

# how to add elements to dictionary

e['c'] = 'value is a string'

print('e is:->',e)

e.clear()
print('e after clear command',e)
# e['g'] = 3.0200205222500

print(e.get('g','Key not found'))
print(e)

dic = {1:10, 2:20,3.2:30,4:40}
print(dic.keys())
print(dic.values())
print(dic.items())

# Wap to print all values on dictionary one by one

# How to get key from value
v = 30
for i in dic.keys():
    if dic[i] == v:
        print('key is', i)

print(list(dic.keys())[list(dic.values()).index(30)])

x = dic.popitem()
print(x)

f = {10:1,200:2}
dic.update(f)
print(dic)

# Write a Python script to sort (ascending and descending) a dictionary by value.
l = list(dic.values())
l.sort()
sort_dic ={}
for i in l:
    index_ = list(dic.values()).index(i)
    sort_dic[list(dic.keys())[index_]] = i
print(sort_dic)

'''Write a Python script to concatenate following dictionaries to create a new one. 

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
# dictionary functions
#%%
# help(dict)
