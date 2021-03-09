# print(help(str))

s = 'hi how are YOU'
print(s.capitalize())
s = 'HeLlO'
print(s.casefold())
print(s.center(7))
print(s.lower().count('l'))
print(s.endswith('HeLlO'))
print(s.lower().find('m'))
print(s.lower().index('l'))
print(s.lower().find('m'))
s = '12'
print(s.isalnum())
print('line no 15:',s.isalpha())
print('line no 16:',s.isdecimal())
print('line no 17:',s.isdigit())
s = 'c:\\new folder'
print('line no 19:',s.isprintable())
s = '  '
print(s.isspace())
s = 'hOW are you'
print('line no 23:',s.title())
s ='How Are You'
print('line no 25:',s.istitle())
l = ['hi','how','are','you']
print('line no 27:',' '.join(l))