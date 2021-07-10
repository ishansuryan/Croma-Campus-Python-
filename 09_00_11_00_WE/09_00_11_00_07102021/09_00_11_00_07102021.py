standard_input =[1.75]
n = float(input('Enter the number whose table you want'))
for i in range(1,11):
   print(f"{n} X {i} = {n*i}")
   
print()

for i in range(1,11):
       print("{} X {} = {}".format(n,i,n*i))

s = 'the quick brown fox jumps over a lazy dog'
c = {}
for i in s:
    if i not in c.keys():
        c[i] = 1
    
    else :
        c[i] += 1
    
print(c)

# List Comprehension : the
# syntax [expression for variable in iterable]

l = [f"{n} X {i} = {n*i}" for i in range(1,11)]
print(l)

print()
l_d = {f"{n} X {i}": n*i for i in range(1,11)}
print(l_d)
print('\nlist print')
[print(i) for i in l]

print('\ndictionary print')
[print(i, l_d[i],sep =' = ') for i in l_d]

# Wap to enter cumilative sum of numbers up to 10 
# using list comprehension

l_cum_sum = [sum([x for x in range(0,i+1)]) for i in range(1,11)]
print(l_cum_sum)