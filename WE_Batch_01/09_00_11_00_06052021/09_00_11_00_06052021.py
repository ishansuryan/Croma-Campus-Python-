# strings functions

s = 'Hello How aRe YoU. Hi 1 bb'

print(s.capitalize())

print(f'{s.casefold.__name__} result is:->', s.casefold())

print(f'{s.lower.__name__} result is:->', s.lower())

print(f'{s.center.__name__} result is:-> ',s.center(50) )

print(s.count('o'))

print(s.endswith('. Hi'))

print('line no.17:->',s.find('z'))

# print(s.index('z'))

print(s.isalnum())

print('Line no. 23:-> ','Hello125'.isalnum())

print('h1khhjv'.isidentifier())

print('hello how are you'.islower())

print('c:\ew folder'.isprintable())

print(s.title())

l = ['Hi', 'how', 'are', 'you']

print('-->'.join(l))

print('Prince'.ljust(10))

print('Prince'.rjust(10))

print(s.lower())

print('   hi there   '.lstrip())

print('   hi there   '.rstrip())

print('   hi there   '.strip())

print('The place is delhi and its very costly'.partition('l'))

print('sub-4m car'.removeprefix('sub-'))

print('car is awesome man'.removesuffix(' man'))

print(s.replace('H','z'))

print('The place is delhi and its very costly'.rpartition('l'))

print(s.split('o',2))

print(s.swapcase())

print(s.upper())

print(s.zfill(30))
# print(help(str))