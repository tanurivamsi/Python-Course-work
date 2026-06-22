#Built-in Functions

import sys as a
'''print(a.argv)
print(a.path)
print(a.version)
print(a.exit())

#Platform module
import platform as p
print(p.system(),p.release(),p.processor())'''


#math Function
import math as m
'''print(m.sqrt(16))
print(m.pi)
print(m.e)

print(round(20.93))
print(m.ceil(11.110))
print(m.ceil(11.22))
print(m.ceil(11.8))
print(m.ceil(11.990))

print(m.floor(11.99))
print(m.floor(11.8))
print(m.floor(11.001))
print(m.floor(11.1))
 
print(m.factorial(5))
print(m.fabs(-20.22))
print(m.log(10,21))
print(m.sin(-20.22))
print(m.cos(-20.22))
print(m.tan(-20.22))
print(m.degrees(-20.22))
print(m.radians(-20.22))
 '''
#Random modules
'''
import random as r
r.seed(2)
print(r.random())
print(r.randint(1,10))
print(r.uniform(1,22))
n = "Vamsi"
m = ["t","f","32"]
print(r.choice(n))
print(r.choices(n,k=4))
print(r.shuffle(m))
'''

#collection module
import collections as c
'''n = "Vamsi Tanuri"
print(c.Counter(n))

d = {}
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)'''


n = "Vamsi Tanuri"
#print(c.defaultdict(int))

'''d = c.defaultdict(int)
for i in n:
        d[i]+=1

print(d)'''

'''l = []
print(c.deque(l))
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.pop()
l.pop()
l.append(10)
print(l)'''

#iterable module
from  itertools import *

a=combinations("absd",3)
print([''.join(i) for i in a])

p=permutations("absd",3)
print([''.join(i) for i in p])


