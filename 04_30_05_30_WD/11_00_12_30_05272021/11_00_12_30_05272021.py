import re

s = '''9024494802
(123)-(456)-(7890)
012345679

email@c.com
email@.com
email_id@name.co.in.
he.lp@govt.gov.in'''


mobile_number = re.compile(r'\(?\d{3}\)?-?\(?\d{3}\)?-?\(?\d{4}\)?')

print(mobile_number)

x = re.findall(mobile_number, s)
print(x)

e_mail = r'[\w.]+@[a-zA-Z0-9.]+[\w]+'

y = re.findall(e_mail,s)
print(y)

start = re.match(r'\d{10}',s)
print(start)
print(start.span())
print(start.group())

z = re.search(mobile_number,s)
print(z.span())
print(z.group())
print()
st = re.sub(mobile_number, 'Replaced NUmber', s)
print(st)