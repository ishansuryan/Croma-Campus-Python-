s = ''' this is test string for re
Ha Haha

123-456-7890
(902)-(449)-(4802)
6548456 5496849490 kljbhi
additive
add ddd
email@.com
croma_campus.@gmail.com sdsdsdafwfswf
e_mail@site.gov.in
abs.132@gmail.com

'''
import re


def fin_all():
    x = re.finditer(r'\(?\d{3}\)?-?\(?\d{3}\)?-?\(?\d{4}\)?\b',s)
    return x


x = re.findall(r'\(?\d{3}\)?-?\(?\d{3}\)?-?\(?\d{4}\)?\b',s)
#x = [x[:-1] for x in x]
print('line no 25',x)

y = fin_all()
print('line no 28',next(y))
print('line no 28',next(y))


y = re.search(r'\(?\d{3}\)?-?\(?\d{3}\)?-?\(?\d{4}\)?\b',s)
# y = re.fullmatch('[\w]',s)
print('line no 34', y)


def itr():
    x = [1,2,3,4,5]
    # for i in x:
    #     yield i
    x = iter(x)
    return x
z = itr()
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
'''
Regex code 
for mobile:  \(?\d{3,4}\)?-?

for email :  [\w\.]*@\w{2,20}[\w*\.]+
'''