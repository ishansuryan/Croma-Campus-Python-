l = []
def selection_sort(a):
    if len(a) == 1:
        l.extend(a)
        return 
    else:
        x = a.pop(a.index(min(a)))
        l.append(x)
    return selection_sort(a)

selection_sort([3,2,1,10,20,8,6,0])
print(l)

def number(**kwargs):
    kwargs['a'] = kwargs['a'] + 2
    print(kwargs['a'])

number(a=10)

def gen(l):
    for i in range(len(l)):
        yield l[i]
        
c = gen([10,203,00])

print(next(c))
print(next(c))

print(next(c))

# l = ['1','2','10']
# l1 = ['a','b','c','d']
# l3 = [10,50,60]
# l = list(map(int,l))
# print(l)
# f = list(zip(l,l1,l3))
# print(f)

names =   ['Satyandra', 'Tanu','Chandan','Javed' ]
roll_no = [60,40,30,5]
print(list(zip(roll_no, names)))