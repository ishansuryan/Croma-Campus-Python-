# Dictionaries

# item-quantity

a = {}
print(type(a))

b = dict()
b['beeta'] = 0.3
print(type(b))

l = [['one',10],['two',20]]
l_dic = dict(l)
# print(l_dic)
# print(l_dic['one'])
l_dic['three'] = 30
# print(l_dic)
b[1] = 'ONE'
# print(b)

# print(l_dic.keys())
# print(l_dic.values())
# print(l_dic.items())
x = l_dic.get('onee','Not Found')
print(x)

y = l_dic.pop('three')
print(y)

z =l_dic.popitem()
print(z)

l_dic.update(b)
print(l_dic)

if 1 in l_dic.keys():
    print('key found')

else :
    print('key  not found')

