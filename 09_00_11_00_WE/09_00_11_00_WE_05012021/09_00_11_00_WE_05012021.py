import re

s= ''' This is a  string
replaceing
(902)-(449)-(4802)
1234567890

email@.com
valid.email@gmail.com
correct_email@company.co.in.'''

# x = re.compile(r'[\w.]+@[\w]+.[\w]+.?[\w]+')
# print(type(x))
# lst = re.findall(r'[\w.]+@[\w]+.[\w]+.?[\w]+',s)
# print(lst)

# mobile = re.compile(r'\(?[\d]{3}\)?-?\(?[\d]{3}\)?-?\(?[\d]{4}\)?')
# mobile_numbers = re.findall(mobile,s)
# print(mobile_numbers)


x = re.compile(r'[\w.]+@[\w]+.[\w]+.?[\w]+')

# print(type(x))
# lst = re.finditer(r'[\w.]+@[\w]+.[\w]+.?[\w]+',s)
# for i in lst:
#     print('',i.span())
#     # print(i.string)
#     print(i.group())
# print("1",next(lst).group())
# print("2",next(lst).group())

# lst = re.finditer(r'[\w.]+@[\w]+.[\w]+.?[\w]+',s)

# s_ = 'valid.email@gmail.com'
# f_match = re.fullmatch(x,s_)
# print(f_match)

mobile = re.compile(r'\(?[\d]{3}\)?-?\(?[\d]{3}\)?-?\(?[\d]{4}\)?')
mobile_numbers = re.search(mobile,s)
print(mobile_numbers)

x = re.sub(x,'replaced_email',s)
print(x)