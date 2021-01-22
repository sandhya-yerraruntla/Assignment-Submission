start = int(input())  
end = int(input())  
print("Prime numbers from",start,"to",end,"are :") 
for num in range(start,end + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
