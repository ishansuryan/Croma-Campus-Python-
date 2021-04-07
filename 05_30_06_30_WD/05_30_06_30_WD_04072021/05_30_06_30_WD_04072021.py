# Error Handling

a = 10
b = 0
# try:
#     print(a[30])
# except NameError:
#     print('Variable not defined')

# except KeyError:
#     print("Key is not in dictionary")    
    
try:
    print(a/b)

except ValueError:
    print('Devision by zero is not defined\n')

except TypeError:
    print("Please enter a valid value")
    
except ZeroDivisionError:
    print("Devision by zero not defined")

# finally :
#     print('finally executed')


else:
    print('Else executed')


print('The programme is running smoothly')

b = 0

# if b == 0 :
#     raise TypeError ('Value must not be 0')
'''Below, we have provided buggy code. Add a try/except clause 
so the code runs without errors. If a blog post didn’t get any
likes, a ‘Likes’ key should be added to that dictionary with 
a value of 0.'''

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]
# print(blog_posts)
# total_likes = 0

# for post in blog_posts:
#     try:
#         total_likes = total_likes + post['Likes']
    
#     except KeyError:
#         post['Likes'] = 0
        
# print(blog_posts)


import numpy as np
print(np.__version__)
assert np.__version__ > '1.2', "Numpy version below required minimum is 2.0"

print('You have met minimum requirements for numpy')