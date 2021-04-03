l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

index_to_remove = [0,4,5]
index_to_remove.sort(reverse =True)
print(index_to_remove)
for i in index_to_remove:
    l.pop(i)
    
print(l)
l =[]
for i in range(3):
    l1 =[]
    for j in range(4):
        l2 =[]
        for k in range(6):
          l2.append('*')
        
        l1.append(l2)
    l.append(l1)  

print(l)
print()
l = [[[x for x in range (6)] for j in range(4)]for i in range(3)]
print(l)