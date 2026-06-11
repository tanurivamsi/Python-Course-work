#sequence ---> str,list,tuple,set,dictionary
#For loop ---> complete all iteration
#string sequence
'''s= "Vamsi"
for CH in s:
    print(CH)

#list sequence
l= ["Vamsi",1,"w",2.1]
for items in l:
    print(items)

#tuple sequence
t= ("Vamsi",1,"w",2.1)
for items in t:
    print(items)

#set sequence
s= {"Vamsi",1,"w",2.1}
for items in s:
    print(items)

#set sequence
d= {"Name":"Vamsi","roll":1,"branch":'cse-ai'}
for items in d:
    print(items,d[items])
'''

#range Function in for loop
# 1) print 1 to 10 numbers
'''for i in range(1,11):
    print(i)
# 2) print 1 to 10 even numbers
for i in range(2,11,2):
    print(i)
# 3) print 1 to 10 odd numbers
for i in range(1,11,2):
    print(i)
# 4) print 10 to 1 numbers
for i in range(10,0,-1):
    print(i)
# 5) print 10 to 1 even numbers
for i in range(10,0,-2):
    print(i)'''

#indexing each iteration
'''s = "Vamsi"
for i in range(len(s)):
    print(i,s[i])

l = ["Vamsi",1,"w",2.1]
for i in range(len(l)):
    print(i,l[i])

t = ("Vamsi",1,"w",2.1)
for i in range(len(t)):
    print(i,t[i])'''

#enumerate function in loops
'''s = "Vamsi"
for i in enumerate(s):
    print(i[0],i[1])

l = ["Vamsi",1,"w",2.1]
for i in enumerate(l):
    print(i[0],i[1])

t = ("Vamsi",1,"w",2.1)
for i in enumerate(t):
    print(i[0],i[1])

sett = {"Vamsi",1,"w",2.1}
for i in enumerate(sett):
    print(i[0],i[1])
d = {"Name":"Vamsi","roll":1,"branch":'cse-ai'}
for i in enumerate(d):
    print(i[0],i[1])'''

#Jumping statements
'''for i in range(11):
    pass     #--->Empty block of the iteration
for i in range(11):
    if i==8:
        break   #--->termination the iteration
    print(i)
for i in range(11):
    if i==8:
        continue #--->skipping the iteration
    print(i)'''

#problem 2
'''s = 'looping statement'
v = 'aeiouAEIOU'
for i in s:
    if i in v:
        print(i)

#problem 2
l = [1,34,4,32434,24,34,4]
for i in l:
    if i%2 == 0:
        print(i)

#problem 3
d = {'a':1,'b':2,'c':3,'d':0}
for i in d:
    if d[i]:
        print(i)

#problem 4
t = (1,34,4,32434,24,34,4)
for i in range(len(t)):
    print(i*t[i])'''

#problem 5
s = {'vamsi','sai','anandh','mohan'}
for i in s:
    print(i.upper())
    




