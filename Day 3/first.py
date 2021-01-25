data = data1 = ""
with open('file1.txt') as ff :
    data = ff.read()
with open('file2.txt') as fs :
    data1 = fs.read()
data += '\n'
data1 += data
with open('file3.txt' , 'w') as ft :
    ft.write(data1)
