'''s = "Python"
for i in range(len(s)):
    for k in range(i+1,len(s)):
        print(s[i],s[k],sep='',end=' ')'''

'''
l = [[1,2,3],[4,5,6],[7,8,9]]
s = 0
for i in l:
    for j in i:
        s += j
print(f"Sum of {l} is : {s}")

'''

'''
d = {"123444":{"pin":"45673","balance":2300},
     "123434":{"pin":"4566","balance":3300},
     "123454":{"pin":"4565","balance":4300},
     "123433":{"pin":"4562","balance":5300},
     "123334":{"pin":"456232","balance":6300},
     }

#e = int(input("Account number :"))
for i in d:
    print("Account No :",i)
    print("Balance ",d[i]['balance'])'''
'''n = int(input("Enter a number to print * :"))
for row in range(n):
    for col in range(n):
        print("*",end=" ")
    print()'''

'''n = int(input("Enter a number to print * :"))
for row in range(n):
    for col in range(n):
        print(col%2,end=" ")
    print()'''

'''n = int(input("Enter a number to print * :"))
for row in range(n):
    for col in range(n):
        print(row%2,end=" ")
    print()'''


'''n  = int(input("Enter a number :"))
for i in range(n):
    for j in range((n-i)):
        print("*",end=" ")
    print()'''

'''n  = int(input("Enter a number :"))
for i in range(n):
    for s in range(n-i-1):
        print(" ",end=" ")
    for s in range(i+1):
        print("*",end=" ")
    
    print()
n  = int(input("Enter a number :"))
for row in range(n):
    for spa in range(row):
        print(" ",end=" ")
    for col in range(n-row):
        print("*",end=" ")
    
    print()

    
n = int(input("Enter a number to print * :"))
for row in range(n):
    #print(row%2,end=" ")
    for col in range(n):
        print((row+col)%2,end=" ")
    print()'''

n  = int(input("Enter a number :"))
c = 1
for i in range(n):
    for s in range(i+1):
        print(str(c).zfill(2),end=" ")
        c+=1
    print()
