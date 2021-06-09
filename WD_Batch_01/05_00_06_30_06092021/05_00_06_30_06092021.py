# WAP to generate a dictionay upto n elements where number is key and number square is value.

'''Write a Python program to combine two dictionary adding values for common keys. Go to the editor'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

for i in d2.keys():
    if i in d1.keys():
        d1[i] = d1[i]+ d2[i]
    
    else :
        d1[i] = d2[i]
print(d1)

'''
Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
               {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}'''

d = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

d_ = set()

for i in d:
    d_.add(list(i.values())[0])

print(d_)

# Write a Python program to remove None value from a given list. 
# Original list:
l = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

for i in range(l.count(None)):
    l.remove(None)
print(l)