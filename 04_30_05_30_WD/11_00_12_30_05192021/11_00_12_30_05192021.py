def daa(*a):
    print(type(a))
    print(sum(a))

daa(1,2,3,5,6)
daa(3,30,2)
daa(1,2,2,2,2,2,5,5,5,5,5,)

def kwarg(**a):
    # d = {}
    # d.update(a)
    print(a)

kwarg(c=10,d = 30, e = 50)

def words(a,*args,**kwargs):   
    print(a,args, kwargs)

words(10,'hi','hello', hi = 'HI', hello = 20)
# passing function to a function


# a = devide            # passsing function refference
# print(a(4,2))
# print('Line No 26:',devide)
# x =devide(2,0)

def smart_devide(q):
    def inner(a,b):
        if b == 0:
            print('Devision by zero is not defined')
            return
        
        return q(a,b)
        
    return inner

@smart_devide
def devide(a,b):
    return a/b

# devide = smart_devide(devide)           # decorator

devide(10,0)
z = devide(10,5)
print(z)

# def test():
#     def inner_():
#         print('Inside inner function')
#     return inner_()
# test()
