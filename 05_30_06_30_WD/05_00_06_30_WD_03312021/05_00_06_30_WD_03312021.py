l =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
mini = []
for i in range(len(l),0,-1):
    small = None
    for j in range (i-1):
        if l[j][1] < l[j+1][1]:
            small = l[j]
    mini.append(small)
    l.remove(small)
    
print(mini)
    