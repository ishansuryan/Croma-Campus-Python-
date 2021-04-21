# print('Hello world')
# a = int(input('Enter the number: '))
# b = input('Enter the number: ')
# print('The sum is:',a+int(b))

s = "Hello2 how are you"
#    0123456789
print(s[::-1])
print(s[0:7].isalnum())
print(s[0:5].isalnum())
print('class'.isidentifier())


s = r'c:\new folder\table'

print('Line no:16',s.isprintable())


s = '     hi hoW aRe YOU    '
print('line no 20', s.swapcase())
print(s.upper())
print(s.title())
print(s.ljust(20))
print(s.lower())
print(s.lstrip())
print(s.rstrip())
print(s.strip())
s = s.strip()
print('line no 28:',s.split('h'))
print(s.partition('z'))
print(s.replace('o','Z'))
print(s.zfill(20))

# s = ['Hello','how','are','you']
# print(type(s))
# print('-'.join(s))