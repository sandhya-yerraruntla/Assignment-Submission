lst=[]
n = int(input("Enter number of elements "))
for i in range(n):
    ele = (input("Enter values in list "))
    lst.append(ele)
res = [num for num in lst if num != '[]']
print(res)
