# Iterators

l = iter([1,2,3,4,5,6])
print(next(l))
print(next(l))

def gen():
    for i in range(11):
        yield i

for i in gen():
    print(i)

# lambda function & list comprehension
# syntax for list comprehension [expression for variable in iterable]
l = [(1,2,20),(2,1,19),(6,4,23),(5,3,10)]
print(l)
# print('original                 ',l)
# l = [(x[1],x[0],x[2]) for x in l]
# print('after changing places    ',l)

# l.sort()
# print('after sort               ',l)
# l = [(x[1],x[0],x[2]) for x in l]
# print('after sort abd reverse   ',l)

# lambda function
# def f(t):
#     return t[1]
l.sort(key = lambda x:x[1])
print(l)


# wap to print a new list telling me true or false in place of number if
# i am checking for string

test = [1,'2',3,'4','5',6,'7',8,'9',10]

bool_lst = [True if type(y) == str else False for y in test ]
print(bool_lst)

# map function

l_str = ['1','2','3','4']
print(l_str)
l_str = list(map(int,l_str))
print(l_str)

l_ = [1,2,3,4,5,6,7,8,9]
l_ = list(map(str,l_))
print(l_)

# filter

test_int = list(filter(lambda x: True if type(x) == int else False,test))
print(test_int)