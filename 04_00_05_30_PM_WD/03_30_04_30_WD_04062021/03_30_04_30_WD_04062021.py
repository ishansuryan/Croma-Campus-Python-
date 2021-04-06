import re
some_string = '''()()()()({}{}{}[][][]Hello how are you 
(902)-(449)-(7802) is a phone number.first10_@email.gov.in
email id is cromacampus@gmail.com    fgfgfg fgteyhyfggurtui t'''
# print(re.search(r'\w*\s',some_string))
# print(re.findall('\w',some_string))

mobile = re.findall(r'\(\d\d\d\)-\(\d\d\d\)-\(\d\d\d\d\)',some_string)
print(mobile)

email = re.findall(r'[\w]+\@\w*?\.[\w.]+',some_string)
print(email)