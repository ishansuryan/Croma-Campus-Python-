#File Handling 
# file = open("/mnt/New_Volume/Work_From_Home/Croma_Campus/06242021/05_00_06_30_06242021/testing.txt",'w') 
# file_1 = open('/mnt/New_Volume/Work_From_Home/Croma_Campus/06242021/05_00_06_30_06242021/multipe file.txt','w') 
# file.write("Test content for file handling\n") 
# file_1.write("Test content for file handling in multiple file\n") 
# file.write("Second line in the file\n") 
# file.write('thrid line\n') 
# file_1.write("second line in multiple file\n") 
# file_1.write("third line in multiple file\n") 
# file.write('forth line') 
# file.close() 

# file = open('/mnt/New_Volume/Work_From_Home/Croma_Campus/06242021/05_00_06_30_06242021/testing.txt','r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.seek(0)
# print('The readlines output:->\n',file.readlines())

csv = open('/mnt/New_Volume/Work_From_Home/Croma_Campus/06242021/05_00_06_30_06242021/marks.csv','r',)
# print(csv.readlines())
data = [x.strip('\n').split(',') for x in csv.readlines()]
print('Initial data\n', data)
data = list(map(lambda x: [x[0], int(x[1])],data))
data.sort(key = lambda x:x[1])
print('Modified data\n',data)

sorted_csv = open('/mnt/New_Volume/Work_From_Home/Croma_Campus/06242021/05_00_06_30_06242021/marks_sorted.csv','w')
for i in data:
    sorted_csv.write(str(i[0])+ ','+ str(i[1])+'\n')
sorted_csv.close()
