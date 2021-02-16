# string = 'The quick brown fox jumped over the lazy dog'
# print(string[10])

# print(string[0:11])

# print(string[0:11:3])
# print(string[-44:])
# print(string[-10:-14:-1])
# print(string[::-1])

s = 'HoW are YoU?'
# print(s.capitalize())
print(s.casefold())
print(s.center(50))
print(s.casefold().count('o'))
print(s.endswith('YOU?'))
print(s.expandtabs(tabsize = 10))
print(s.find('oj',2,20))
print(s.index('o'))
print(s.isalnum())
print(s.isalpha())

c = '1234.567890'
# print(c.isdecimal())
# print(c.isdigit())
# print()

d='     APPlE      '
# print(d.isidentifier())

# print(d.islower())
# print(c.isnumeric())
# print(d.isprintable())
# space = '     v'
# print(space.isspace())
# print(d.isupper())

l = ['how', 'is', 'the', 'weather']

print(' '.join(l))

print(d.rjust(30))
print(d.lstrip())
print(d.rstrip())
print(d.strip().partition('p'))
print(d.strip().replace('P','o'))