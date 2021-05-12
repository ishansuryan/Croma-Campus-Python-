s = 'hello world how are you? i am doing fine'
#    012345678910
print('Type of s is:',type(s))
print('Line No.4->', s[0])
print('Line No.5->',s[0:11])
print('Line No.6->',s[-1])

# Rule for slicing: start limit is always smaller than end limit

print('Line No.10->',s[-4:])
print('Line No.11->',s[0:11])
print('Line No.12->',s[:])

print('Line No.14->',s[0:11:3])
v = s.split()
# print('Line NO.->16',v)
print('Line No.17->',s[-1:-5:-1])
print('Line No.18->',s[::-1])