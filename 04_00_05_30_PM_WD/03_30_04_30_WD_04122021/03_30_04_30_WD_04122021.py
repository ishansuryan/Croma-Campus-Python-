import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
# print(x)


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) 

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) 


txt = "The rain in Spain"
x = re.search("in", txt)
print(x)

print("The first white-space character is located in position:", x.start())
print("#The first white-space character is located in position:", x.span())
print("*-***The first white-space character is located in position:", x.string)
print('line no 23:',x.group())

# txt = "The rain in Spain"
# x = re.split("n", txt)
# print(x) 

# txt = "The rain in Spain"
# x = re.sub("\s", "_", txt,2)
# print(x)

# txt = "The rain in Spain"
# x = re.subn("\s", "_", txt)
# print(x)