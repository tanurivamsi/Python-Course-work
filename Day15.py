'''n = int(input("Enter : "))
m = n//2
for row in range(n):
    if row<=m:
        for col in range(row+1):
            print("*",end='')
    else:
        for col in range(n-row):
            print("*",end='')
        
    print()'''
    
'''n = int(input("Enter : "))
m = n//2
for row in range(n):
    if row<=m:
            print("*"*(row+1),end='')
    else:
            print("*"*(n-row),end='')
        
    print()'''

'''n = int(input("Enter : "))
m = n//2
for row in range(n):
    if row<=m:
        print(" "*(m-row),end=' ')
        print("*"*(row+1),end=' ')
    else:
        print(" "*(row-m),end=' ')
        print("*"*(n-row),end=' ')
        
        
    print()

n = int(input("Enter : "))
mid = n//2
for row in range(n):
    for col in range(n):
        if row == 0 or row==n-1 or row==0 or col==row or col+row==4 or col == n-1 :
            print(' * ',end=' ')
    else:
        print(' ',end=' ')
        
        
    print()

    
'''
#print A Pattern

n = int(input("Enter a number to print A : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or row == m or col == n-1 or col==0 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print B Pattern

n = int(input("Enter a number to print B : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or row == m or col == n-1 or col==0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print C Pattern
n = int(input("Enter a number to print C : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0  or col==0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print B Pattern

n = int(input("Enter a number to print D : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or col == n-1 or col==0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print E Pattern

n = int(input("Enter a number to print E : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==m or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print F Pattern

n = int(input("Enter a number to print F : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row == m :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print G Pattern

n = int(input("Enter a number to print F : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row ==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print H Pattern

n = int(input("Enter a number to print H : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==m or col==n-1 or col == 0 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()



#print H Pattern

n = int(input("Enter a number to print H : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==m or col==n-1 or col == 0 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()


#print I Pattern

n = int(input("Enter a number to print I : "))
m = n//2
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col == m :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print J Pattern

n = int(input("Enter a number to print J: "))

for row in range(n):
    for col in range(n):

        if row == 0:                      # Top horizontal line
            print("*", end=" ")

        elif col == n//2 and row < n-1:   # Vertical line
            print("*", end=" ")

        elif row == n-1 and col <= n//2:  # Bottom horizontal line
            print("*", end=" ")

        elif col == 0 and row >= n//2:    # Left side curve
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
#print K Pattern

n = int(input("Enter a number to print J : "))
m = n//2
for row in range(n):
    for col in range(n):
        if col == 0 or (row == m and row <=0) :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print L Pattern

n = int(input("Enter a number to print L : "))
m = n//2
for row in range(n):
    for col in range(n):
        if col == 0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print M Pattern

n = int(input("Enter a number to print N : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == 0 or col == n-1 or row<c_m or row == col :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print O Pattern

n = int(input("Enter a number to print O : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == 0 or col == n-1 or row==0 or row == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print P Pattern

n = int(input("Enter a number to print P : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == 0 or (col == n-1 and row<=m) or row==0 or row == m  :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print q Pattern

n = int(input("Enter a number to print q : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == n-1 or (col == 0 and row<=m) or row==0 or row == m  :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print R Pattern

n = int(input("Enter a number to print r : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == n-1 or col == 0 or row==0 or row == m:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()
#print T Pattern

n = int(input("Enter a number to print T : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if col == m or row==0:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print S Pattern

n = int(input("Enter a number to print S : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row == 0 or row==n-1 or row == m or (col==0 and row <= m) or (col==n-1 and row >= m):
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print U Pattern

n = int(input("Enter a number to print U : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row == n-1 or col==0 or col==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print X Pattern

n = int(input("Enter a number to print X : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row+col == 4 or row == col :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()

#print Z Pattern

n = int(input("Enter a number to print X : "))
m = n//2
#c_m = (row+col==4)//2
for row in range(n):
    for col in range(n):
        c_m = (row+col==4)//2
        if row == 0 or row == n-1 or row+col == 4 :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()



    




