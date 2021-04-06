d = {'two':20,'three':30, }
print(type(d))

d1 = dict()
print(type(d1))

d['one'] = 10
print(d)

d2 = dict([('1',2),('3',4)])
print(d2)

d3 = {(1,2):30}
print(d3)

print(d.get('onee'), )
print(d['one'])
print(d.items())
print()
print(d.keys())
print(d.values())



# Tuples :

# a = (10,)
# a[0] = 30
# print(type(a))

# print(help(tuple))

d.update(d2)

print(d)

# "variable" = 20

test = {'a':'b','b':'c','c':{"d":'e'},'e':'f'}

print(test[test[test[test['a']]]['d']])
#                 c       b