s = ''' this is test string for re
Ha Haha

123-456-7890
(902)-(449)-(4802)
6548456549684949kljbhi
additive
add ddd
email@.com
croma_campus.@gmail.com sdsdsdafwfswf
e_mail@site.gov.in
abs.132@gmail.com

'''
import re

print(re.match(r'(\(?\d{3,4}\)?-?){3}',s))


'''
Regex code 
for mobile:  \(?\d{3,4}\)?-?

for email :  [\w\.]*@\w{2,20}[\w*\.]+
'''