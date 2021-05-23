# recursion

# def add(l):
#     if len(l)== 1:
#         return l[0]
    
#     return l[0]+ add(l[1:])

# l = [1,2,3,4,5,6,7,8,9,10]
# result = add(l)
# print(result)

# '''Write a function to check wether a given string is a palindrome or not'''

# scope of a varible

# a = 10 


# def test():
#     global a
#     a = 30
#     print('value of a inside function',a)

# print('Value of a before function',a)

# test()

# print('Value of a after function call',a)


def smart_devide(func):
    def inner(a,b):
        if b == 0:
            # print()
            return 'Devision by Zero is not defined '
        
        return func(a,b)
    return inner

@smart_devide                               # Decorator
def devide(a,b):
    return a/b

# devide = smart_devide(devide)             # Decorator


v = devide(6,0)
print(v)

# iterators and generators

l = iter([1,2,3])#,4,5,6,7,8,9])

# print(next(l))
# print(next(l))
# # print(l[0:8])
# print(next(l))

# generator

def gen(l):
    for i in l:
        yield i

standard_input = gen(l)
t = [100,200,300,400,500,600,700,800,900]

a = int(input())
print('The value of a is ',a)
b =input()
print(b)
c = input()
print(c)
# d = input()

# for i in gen(l):
    # print(i)

# lambda function

# it is a un-maned single line function

q = [(5,6),(3,4),(7,8),(1,2)]

print(q)

# def ret(x):
    # return x[1]

q.sort(key = lambda x:x[1])    #ret)
print(q)