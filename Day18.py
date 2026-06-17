'''s = "Python"
c = 0
for i in range(len(s)):
    c+=1
print(c)

def display(s,index):
    if index == len(s):
        return
    print(s[:index+1])
    display(s,index+1)

display("vamsi",0)


def display(s,index,l):
    if index == len(s)-l*1:
        return
    print(s[index:index+l])
    display(s,index+1,l)


display("vamsi",0,2)


def display(l,i):
    if i == len(l):
        return 0
    return l[i]+diplay(l,i+1)

l = [1,3,4,22,5,3]
print(display(1,0))'''


def display(l,i):
    if i == len(l):
        return 0
    return l[i]+display(l,i+1)

l = [1,4,3,2,22]
print(display(l,0))
