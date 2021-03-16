def fibonacchi(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    
    return fibonacchi(n-1) + fibonacchi(n-2)

fib = fibonacchi(3)
print(fib) 

# write a function to check wether a string is a palindrome or Not
def pal (s):
    s = str(s)
    if len(s) == 1:
        return True
    
    elif len(s) ==2 and s[0] == s[1]:
        return True
    
    else: 
        if s[0]==s[-1]:
            return pal(s[1:-1])
        else: 
            return False
        
x = pal(101)
print(x)

s='1221'
print('after slicing',s[1:-1]) 

def add(n):
    if n == 1:
        return 1
    else: 
        return n + add(n-1)
    
print(add(10))    