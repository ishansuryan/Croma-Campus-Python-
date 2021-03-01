l = [[5,6],[3,4],[1,2]]  
print(l)
n1 = l[0][0]
n2 = l[0][1]
s = []
print(n1,n2)
for i in range(len(l)):
    for i in l:
        if i[0] == n1 and i[1] == n2:
            continue
        elif i[1] < n2:
            n1,n2 = i[0],i[1]
    s.append(l.pop(l.index(i)))
print(s)