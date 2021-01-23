string = input("Enter a string : ")
ch = input("Enter a character : ")
for i in range(len(string)):
    if(string[i] == ch):
        i += 1
        print("Character " , ch , "occured at position " , i)

