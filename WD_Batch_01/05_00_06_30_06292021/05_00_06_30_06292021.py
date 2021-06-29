s = '''
+91-123456789
9024494802
+91-(012)-(345)-(6789)

email_10@website.com. Is the line.
email@.com
suppert@help.gov.in.
'''
import re

print(help(re))
# %%

pattern = re.compile('\(?\d{3}\)?-?\(?\d{3}\)?-?\(?\d{4}\)?')
email_pattern = re.compile('[\w]+@[\w]+.[\w]+.?[\w]+')
l = re.findall(email_pattern,s)
print(l)
ss = re.search(email_pattern,s)
print('line no 20:->',type(ss))
print(ss.group())
print(ss.span())
print(ss.groups())

x = re.sub(email_pattern,'email found',s)
print('Line no 26\n',x)