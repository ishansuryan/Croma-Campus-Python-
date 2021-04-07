s = ''' this is test string for re
Ha Haha

123-456-7890
(902)-(449)-(4802)
6548456549684949kljbhi
additive
add ddd
email@.com
croma_campus.@gmail.com
e_mail@site.gov.in

'''
import re

print(re.match(r'\wd?',s))