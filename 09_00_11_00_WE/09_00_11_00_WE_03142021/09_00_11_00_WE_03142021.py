#%%
help(dict)
# %%
a = dict()
type(a)
# %%
b= {}
type(b)
# %%
help(tuple)
# %%
a = ()
type(a)
# %%
a = (10,)
type(a)
# %%
# Key of a dictionary is always a immutable element
# %%
a = {'a':'A',1:10, (1,2):[1,2,3,6,5,4,7,89]}
a[(1,2)][-1]
# %%
print(a[1])
a['a']
# %%
b = {(1,2):10}
# %%
b.clear()
b
# %%
a.get('A')
# %%
a['A']
# %%
f = list(a.items())
f[1][1]
# %%
a.keys()
# %%
l = a.pop((1,2))
l
# %%
a
# %%
a.popitem()
# %%
a
# %%
a.popitem()
# %%
a
# %%
b= {1:10,2:30,3:90}
a[20] = 200         # assigning a key and value to dictionary
# %%
a
# %%
a.update(b)
a
# %%
e = [(10,30),('s','String')]
a.update(e)
a
# %%
l = [2,5,6,7,90]
for index,value in enumerate(l):
    print(index, value)
# %%
a1,b1 = (10,30)
print(a1,b1)
# %%
a = {1:10,2:30,3:90,4:50,3:10,3:'three'}
# e = {4:50,3:10}
# a.update(e)
a[3]
# %%
a.keys()
# %%
a
# %%
keys = list(a.keys())
values =list (a.values())
item = 10
item_index = values.index(10)
keys[item_index]
# %%
list(a.keys())[list(a.values()).index('three')]
# %%
s = 'google'
d = {}

for i in s:
    if i not in d.keys():
        d[i] = 1
    else :
        d[i]+=1
print(d)
# %%
x = list(a.keys())[where('three' in list(a.values()).index(10))]
# %%
