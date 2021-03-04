s = 'the quick brown fox jumped over the lazy dog'

print(s[-1])
print(s[4:9])       # string slicing
print(s[4:9:2])
print('      ',s[:])
print('reverse is: ',s[-1:-10:-1])
print('reversing ideom is:\n',s[::-1])
''' 
Rules for string slicing are:
1) start value must be always smaller than end value
2) start value must be present in string
''' 

print('the slice is ',s[50:60])

s = 'he said that "he is going to come today"'
s = '''he sais that "he's going to come tomorrow"'''
s = 'he sais that "he\'s going to come tomorrow"'
s = 'c:\\folder'
print(s)
s = r'c:\folder'
print('new method for printing backslash :',s)

print(r"C:\Croma-Campus-Python-\05_30_06_30_WD\05_30_06_30_WD_03042021\05_30_06_30_WD_03042021_01.mp4")
