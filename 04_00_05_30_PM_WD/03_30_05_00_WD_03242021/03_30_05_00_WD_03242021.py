l = ['1','2','3','4']
l = list(map(int,l))
print(type(l[0]))

def sq(n):
    return n**2

l_sq = list(map(sq,l))
print(l_sq)

l3 = ['a','e','k','m','i','o','u','A']

def vowel(n):
    if n.lower() in l3:
        return True
    else:
        return False

final = list(filter(vowel,l3))
print(final)

s = 'the quick brown fox jumps over lazy dog'
lst = [' ']
s = list(s)
def unique(n):
    if n in lst:
        return False
    else :
        lst.append(n)
    return True

z = list(filter(unique,s))
print(z)
print(lst)

s = '1+2'
print(eval(s))