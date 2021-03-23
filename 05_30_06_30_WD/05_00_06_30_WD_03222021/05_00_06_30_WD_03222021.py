n = 5
for row in range(n):
    for num in range(row+1):
        print(num+1, end ='')
    for space in range(n-row-1):
        print(end = ' ')
    for num in range(n-row-1):
        print(end =' ')
    for space in range(row+1,0,-1):
        print(end = f'{space}')
    print()
    
for row in range(n):
    for num in range(row+1):
        print(num+1, end ='')
    for space in range(2*(n-row)-2):
        print(end = ' ')
    for space in range(row+1,0,-1):
        print(end = f'{space}')
    print()
    
# A
row = 10
for i in range(row):
    for j in range(row-i):
        print(end=' ')
    for k in range(2*i +1):
        if k ==0 or k== 2*i or i == 3*row//4:
            print(end='*')
        else: print(end= ' ')
    
        
    print()