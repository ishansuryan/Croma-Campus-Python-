# error handling

a = 10
b = '-1'
try:
    print(int(a)/int(b))

except ZeroDivisionError:
    print('devision by zero is not defined')

except TypeError:
    print('please check type of variable should be int or float')

except ValueError:
    print('please input int orfloat value type')

except:
    print('Last Except running')

finally:
    print('Runs in Every Sictuation')

    
print('after try and except statement')

# introducing assertion Error

import numpy as np
print(np.__version__)

# assert np.__version__ >='1.20.4','Numpy version is lower than required mini mum required is 1.21.3'
try:
    
    if b<0:
        raise ValueError ('Value of b is smaller than 0')

except:
    pass

if type(b) == str:
    raise TypeError ('Variable type is string requird is int or float')