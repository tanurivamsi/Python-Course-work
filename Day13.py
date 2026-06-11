# 1)
'''o = 949494
for i in range(6):
    password = input("Enter your Possword : ")
    
    if password == o:
        print("Unlocked")
        break
    else:
        print("Incorrect Try again ")
else:
    print("Please try again , After 60 seconds")'''

# 2)finding of element in list  

'''l = [1,2,3,4,55,554,22]
a = int(input("Enter a number here : "))
for i in range(len(l)):
    if a == l[i]:
        print(f"The number {a} is found with index {l[i]} ")
        break
else:
    print(f"The number {a} is not found")'''

# 3) checking the password strong or not
'''p = input("Enter your password : ")
if len(p) >= 8:
    s = set()
    for i in p:
        if i.isupper():
            s.add("u")
        elif i.islower():
            s.add("l")
        elif i.isdigit():
            s.add("d")
        else:
            s.add("s")
    if len(s)==4:
        print("Strong password ")
    else:
        print("Weak password ")

else:
    print("Weak password ")'''
#ASSERT --> Debugging
'''
s = 1
assert s != None ,"You need to update the s"
print(s)'''

'''name = "aswd"
age  = 22
batch = 55
assert (name != "" and age != None and batch != None), "You need to add data"
print(name,age,batch)'''


#While loop
'''
1) initialization
2) while condition
3) updation
4) statement

'''
'''i = 1
while i < 11:
    print(i)
    i += 1'''

'''i = 2
while i < 11:
    print(i)
    i += 2'''


# 1)
'''l = [1,3,23,2,45454,5,3,4,3,4]
i = 0
while i<len(l):
    print(l[i])
    i+=1'''

'''l = "Vamsissjk"
i = 0
while i<len(l):
    print(l[i])
    i+=1
l = (1,3,23,2,45454,5,3,4,3,4)
i = 0
while i<len(l):
    print(l[i])
    i+=1

l = [1,3,23,2,45,0,0,454,5,3,4,0,0,0,3,4]
#i = 0
while 0 in l:
    l.remove(0)
    print(l)
'''

i = 0
while i>1:
    status  = input("If you want to continue press [C] to win [W] ").upper()
    if status == 'W':
        print("You won the game ")
        break
    i-=1
    print(f'{i} moves left to play')
    
else:
    print("game Over")
    



