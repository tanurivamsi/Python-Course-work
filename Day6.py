# Weekly exam
#1) student report
'''student = input()
rollno = int(input())
s1 = int(input())
s2 = int(input())
s3 = int(input())

total = s1+s2+s3
avg = total/3
print(f"Student Name : {student}")
print(f"Roll No : {rollno}")
print(f"Total Marks : {total}")
print(f"Average : {avg}")'''

#2)string Analyser

'''s = input()
print("Total Characters : ",len(s))
print("First Character  : ",s[0])
print("Last Character : ",s[-1])
print("Uppercase Characters : ",s.upper())
print("Reversed Characters : ",s[::-1])'''


#3)smart number Analyser

'''a,b,c = map(int,input().split())
print("Sum : ",a+b+c)
print("Average  : ",(a+b+c)/3)
print("Product : ",a*b*c)'''

#Methods of String
'''s = "Vamsi Tanuri"
print("Length of characters : ",len(s)) 
print("Sorting the string is :",sorted(s))
print("Maximum value of character is : ",max(s))
print("Minimum value of character is :",min(s))
print("Ascci Value of character 'a' is :",ord('a'))
print("Characters from numbers is : ",chr(2))'''

# case Methods
'''s = "Vamsi Tanuri"
print("uppe characters : ",s.upper())
print("lower is :",s.lower())
print("title character is : ",s.title())
print("casefold character is :",s.casefold())
print("swapcase character is :",s.swapcase())'''
#capitalizer also

#Alignments Methods
'''s = "Vamsi Tanuri"
print("center alignments characters : ",s.center(20,"*"))
print("ljust alignments characters : ",s.ljust(20,"*"))
print("rjust characters : ",s.rjust(20,"*"))
print("zfill characters : ",s.zfill(50))'''

#search and find methods
'''s = "Vamsi Tanuri"
print(s)
print("find the character of 'a' is  : ",s.find("a"))
print("rfind characters of 'V' : ",s.rfind("V"))
print("index characters of 'T' : ",s.index('T'))
print("rindex characters of 'a': ",s.rindex("a"))
print("counting characters of 'a': ",s.count("a"))'''

#Replace and modify
'''s = "Vamsi Tanuri"
print(s)
print("replace character of 'a' to 'A' is  : ",s.replace("a","A"))
print("translate characters of 'Tanuri' to 123456 : ",s.translate('Tanuri',123456))'''


#splitting and joining methods
'''s = "Vamsi Tanuri"
print(s)
print("splitting the characters with ',' is  : ",s.split(","))
print("splitting the characters with ',' in 2 is  : ",s.split(",",2))
print("Right splitting the characters with ',' in 2 is  : ",s.rsplit(",",2))
print("splittingline the characters with ',' in 2 is  : ",s.splitlines())
print("joining characters with '-' is  : ",'-'.join(s))
print("partitioning the characters into three parts is  : ",s.partition('#'))
print("Right partitioning the characters into three parts is  : ",s.rpartition('-'))'''

#Encoding and decoding Methods in strings
s = "Vamsi Tanuri "
print(s)

print("encoding the characters  is  : ",s.encode())














