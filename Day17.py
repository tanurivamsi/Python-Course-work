#Local Scope --> Accessing the variable
#Local variable
#Globle Variable
'''n = 11
def display():
    global n
    n += 9

    print("Inside : ",n)

display()
print("Outside : ",n)'''

'''n = 11
def outer():
    n = 11
    def inner(n):
        nonlocal n
        n+=10
        print("Inner :",n)

    inner(n)
    print("Outer : ",n)
outer()

#Int
def outer():
    def inner(n):
        n+=10
        print("inner : ",n)
    inner(n)
n = 2
outer()
print("Outer : ",n)

#string
def outer():
    def inner(n):
        n = 'Python '
        print("inner : ",n)
    inner(n)
n = 'Lang'
outer()
print("Outer : ",n)

#complex
def outer():
    def inner(n):
        n+=10
        print("inner : ",n)
    inner(n)
n = 2+4j
outer()
print("Outer : ",n)



#boolean
def outer():
    def inner(n):
        n = True
        print("inner : ",n)
    inner(n)
n = False
outer()
print("Outer : ",n)

#List
def outer():
    def inner(n):
        n = [1,2,3,4,44]
        print("inner : ",n)
    inner(n)
n = [1,3,4]
outer()
print("Outer : ",n)
#Tuple
def outer():
    def inner(n):
        n = (1,2,3,4,44)
        print("inner : ",n)
    inner(n)
n = (1,3,4,4)
outer()
print("Outer : ",n)

#set
def outer():
    def inner(n):
        n = (1,2,3,4)
        print("inner : ",n)
    inner(n)
n = (2,3,4,4)
outer()
print("Outer : ",n)

#Dictionary
def outer():
    def inner(n):
        n[2] = 2
        print("inner : ",n)
    inner(n)
n = {1:2,3:2,4:2,4:5}
outer()
print("Outer : ",n)

#Recurssion
def func(num):
    if num == 0:
        return
    #print(num,end=' ')
    func(num-1)
    print(num,end = ' ')
    
num = int(input("Enter a number : "))
func(num)

#sum of digits

def adding(num):
    if num == 0:
        return 0
    return (num+adding(num-1))
num = int(input("Enter a number : "))

print(adding(num))

#powers

def power(base,pow):
    if num == 0:
        return 1
    return num*power(base,pow-1)
#base = int(input("Enter a base number : "))
#pow = int(input("Enter a power number : "))

print(2,4)'''

#Reversing a string
def reversing(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reversing(s,ind-1)

l = input()
print(reversing(l,len(l)-1))

    

    



        
    






