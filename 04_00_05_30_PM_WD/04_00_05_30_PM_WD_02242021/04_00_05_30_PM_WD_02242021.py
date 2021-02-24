# a = list()          # method 1 for creating an empty list
# b = []              # method 2 for creating an empty list
# print('type of b is: ',type(b))

# b = [1,2.2,'string',[121212,'gg'],complex(2,3), True, False]

# # Comcept of Mutability and Immutability
# # Lists are mutable

# a = b
# print(a)
# a[0] = 30

# print("the list a is:", a)
# print('the b is: ',b)

# print("id of b is: ", id(b))
# print("id of a is: ",id(a))

# c = "string"
# d = c
# print("id of c is: ", id(c))
# print("id of d is: ", id(d))

# d = "Stirng"
# print("id of d is: ",id(d))
# print(c)

# b[6] = 100
# print(b, id(b))

# f = b[:]
# print(id(f))

# f[0]= 'Pass'
# print(f[0::2])

# # f.append(['value',"d"])
# # f.extend(['value',"d"])
# # f = f+ ['value',"d"]
# f.extend("string")
# print(f)

print(help(list))

