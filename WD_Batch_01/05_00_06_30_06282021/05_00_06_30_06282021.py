s = '''
+91-123456789
9024494802
+91-(012)-(345)-(6789)

email_10@website.com. Is the line.
email@.com
suppert@help.gov.in.
'''
import re
#%%
import re
print(help(re))
# %%

pattern = re.compile('\(?\d{3}\)?-?\(?\d{3}\)?-?\(?\d{4}\)?')
email_pattern = re.compile('[\w]+@[\w]+.[\w]+.?[\w]+')
l = re.findall(email_pattern,s)
print(l)