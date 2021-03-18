n = 5

for row in range (n):
    for space in range(n-row):
        print(end=' ')
    
    for star in range(row+1):
        print(star+1, end='')
        
    for num in range(row,0,-1):
        print(num, end='')
        
    print()
    
# Hollow Rectangle

row = 13
col = 13

for r in range(row):
    for c in range(col):
        if r == 0 or r == row -1 or c == 0 or r== row//2:
            print(end = '* ')
        else: print(end = ' ')
    print()