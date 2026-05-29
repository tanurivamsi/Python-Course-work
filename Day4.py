# Operators

'''
1. Arithematic(+,-,*,/,%,**)
2.comparision(<,>,<=,>=,==,!=)
3.logical(AND,OR,NOT)
4.Assignment(+=,-=,*=,**=,%=,/=,//=)
5.Bitwise(&,|,^,~,>>,<<)
6.membership(in,not in) --> use for collection of items or elemets like[str,list,tuple,set,dict]
7.Identity(is,not is)
'''
#output Formatting
'''
1.Separated by comma  {','}
2.separated by space {sep='/t'}
3.Separated by end {end=''}
4.F String (f'')
5.formate string (.format()) 
'''

#Arithematic Operators

a = 10
b = 20
print(f"addition of {a} and {b} is : {a+b}")
print(f"subtracting of {a} and {b} is : {a-b}")
print(f"Multiplication of {a} and {b} is : {a*b}")
print(f"FloatQoefficiant of {a} and {b} is : {a/b}")
print(f"qoefficiant of {a} and {b} is : {a//b}")
print(f"Remainder of {a} and {b} is : {a%b}")

#comparision Operators

c = 10
d = 20
print(f"comparision of {c} < {d} is : {c<d}")
print(f"comparision of {c} < {d} is : {c>d}")
print(f"comparision of {c} <= {d} is : {c<=d}")
print(f"comparision of {c} >= {d} is : {c>=d}")
print(f"comparision of {c} != {d} is : {c!=d}")

#logical Operators
e = 10
f = 20
print(f"Logic of {e} AND {f} is : {e and f}")
print(f"Logic of {e} OR {f} is : {e or f}")
#print(f"Logic of {e} NOT {f} is : {e not f}")

#Assignment Operator
g = 10
g+=5
print(g)
h = 10
h+=5
print(h)
i = 10
i*=5
print(i)
j = 10
j/=5
print(j)
k = 10
k%=5
print(k)

#Bitwise Operators
print(f"and of 2 & 6 is : {2 & 6}")  #0010 & 0110
print(f"or of 2 | 6 is : {2 | 6}")  #0010 | 0110
print(f"xor of 2 ^ 6 is : {2 ^ 6}")  #0010 ^ 0110
print(f"leftShift of 2 >> 6 is : {2 >> 6}") #0010 >> 0110
print(f"RightShift of 2 << 6 is : {2 << 6}") #0010 << 0110


#Membership Operators
n = [1,2,3,4]
m = [1,2,3,4]
l = m
print(n in m)
print(l in m)
print(n not in  m)
print(l  not in  m)


#identity Operators
x = [1,2,3,4]
y = [1,2,3,4]
print(x is y)
print(x is not y)








