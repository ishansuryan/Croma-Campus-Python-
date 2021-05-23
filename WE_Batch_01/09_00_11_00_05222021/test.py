def smart_devide(func):
    def inner(a,b):
        if b == 0 :
            print("Devision by zero is not defined")
            return
        
        return func(a,b)
    return inner

# @smart_devide
def devide(a,b):
    return a/b
devide = smart_devide(devide)

print('The name of file is',__name__) 
if __name__ == '__main__':
    print(devide(10,0))
    
