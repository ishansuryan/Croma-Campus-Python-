l = [(1,2),(2,1),(3,4),(4,-3),(6,0),(5,10)]

# def s(x):
#     return x[1]

l.sort(key=lambda x : x[1])
print(l)


def addition(*s):
    print(type(s))
    
    a = 0
    for i in s:
        a+=i
    
    print('The sum is:', a)
    

addition(1,2,3,5,4,9)
addition(1,10)
addition(10,20,30,60,80,1,2574,24,2876,654)


def minus(*s):
    print(type(s))
    
    a = 0
    for i in s:
        a-=i
    
    print('The sum is:', a)
    
minus(2,3,-4,10,-50)

def kwargs_example(*c,**s):
    print(type(s))
    print(c)
    print(s)
    for key,value in s.items():
        print(key,value, sep = '-->')
    
kwargs_example(1,2,3,4,5,6,7,8,9,d=10,c=30,b = -10,a = 'Apple')

l = ['1','2','3','4']

# l = [int(x) for x in l]
# print(l)

l = list(map(lambda x: int(x)**2,l))
print(l)

odd = list(filter(lambda x : x if x%2 !=0 else 0 ,l))
print(odd)