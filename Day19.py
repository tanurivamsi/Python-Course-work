#lambda functions
#It is a Anonumus function to expression
'''
Syntax
lambda arguments : statement
print(function_name(parameters))


adding = lambda a,b :a+b
print(adding(1,3))


wish = lambda name :f"{name}! Welcome to the course "
print(wish("vamsi"))

tax = lambda price: f'GST of {price} is : {(price*0.18)+price}'
print(tax(200))

g = lambda a,b : a if a>b else b
print(g(1,3))

iseven = lambda a:f"{a} is Even " if a%2==0 else f"{a} is odd"
print(iseven(3))


charge = lambda a : a if a>99 else a+30
print(charge(11))
print(a)

#nested lambda if conditions
login = True
instock = True

status = lambda login,instock =("You can buy" if instock else "Out of stock")if login else "login first" 
print(status(login,instock))

l = [1,3,4,4,2]
r = list(map(lambda i:i**2,l))
print(r)

d = {'a':1,'b':2,'c':3}
D = dict(map(lambda x:x*2,d.values()))
print(D)

l = [1,23,45,44,43]
f = list(filter(lambda x:x%2==0,l))
print(f)

from functools import reduce
l = [1,23,45,44,43]
a = reduce(lambda x,i:x+i,l)
m = reduce(lambda x,i:x*i,l)
d = reduce(lambda x,i:x if x>i else i,l)
print(a,m,d)'''

d = {"a":10,"b":43,"c":1,"d":9}

a = dict(sorted(d.items(),key=lambda i:i[1],reverse = True))
print(a)


