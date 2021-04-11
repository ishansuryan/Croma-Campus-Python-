s = 'hi 12345 '
#    0123456789
print('line no isalnum: 3',s[3:8].isalnum())
print('line no isalpha: 4',s[0:2].isalpha())
print('line no isalpha: 5',s[3:8].isdecimal())
print('line no isidentifier: 6','print'.isidentifier())
print('line no islower: 7', s.islower())
print('line no isprintable: 8', s.isprintable())
print('line no isspace: 9', s[2:3].isspace())

s = 'Hi therE'
print(s.title())
print('lineno 13:',s.swapcase())

l = ['hi','how','are','you']
v ='->'.join(l)
print(v)
print(l)

s = '   hi how are you___'
print(s.lstrip())
print(s.rstrip('_'))
print(s.strip(' _'))
print(s.partition(' '))
print(s.replace('h','b',))
print(s.split('o',3))
s = 'hi \n how \n are you \n there'
print(s.splitlines())
s = 'hi'
print('line no 29',s.zfill(5))