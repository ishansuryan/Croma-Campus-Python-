# map
l = ['1','2','3','4']
print(l)

z = list(map(int,l))
print(z)

l = [x for x in range(0,11)]
print(l)

# Filter
def even(i):
    if i%2 == 0:
        return True
    
    else:
        return False
    
even_elements = list(filter(even,l))
print(even_elements)

# Zip

l1 = [x for x in range(1,11)]
l2 = [x for x in range(101,150)]

l3 = list(zip(l1,l2))
print(l3)



l = [(1,2),(2,1),(3,5),(4,4)]

l.sort(key = lambda x: x[1])
print(l)


# recursion

def list_sum(l):
    if len(l) == 1:
        return l[0]
    
    return l[0]+list_sum(l[1:])

l = [x for x in range(11)]
print(l)
print(list_sum(l))

def palindrome(s):
    if len(s) == 2 and s[0]== :


