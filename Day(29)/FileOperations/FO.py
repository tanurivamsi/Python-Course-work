'''F = open('Sample.txt','r')
print(F.read())
F.seek(0)
print(F.readline())
F.seek(0)
print(F.readlines())
F.close()

'''
'''try:
    F = open('Sample.txt','r')
except FileNotFoundError:
    print("File is not found ")

else:
    print(F.read())
    F.seek(0)
    print(F.readline())
    F.seek(0)
    print(F.readlines())
    F.close()'''
'''

#With (Recommanded)
with open('Sample.txt','r') as F:
    print(F.read())
    F.seek(0)
    print(F.readline())
    F.seek(0)
    print(F.readlines())

    '''
'''with open('Sample.txt','a') as W:
    W.write("\nvamsi\nramya")'''
'''with open('Samples.txt','a') as W:
    W.write("\nvamsi\nramya")'''

'''with open('Samples.txt','w') as W:
    W.write("\nvamsi\nramya\njaya\nsrinu")

with open('Samples.txt','w+') as W:
    print("w+ mode")
    W.write("\nvamsi\nramya\njaya\nsrinu\n")
    W.seek(0)
    print(W.read())


with open('Samples.txt','r+') as W:
    print("r+ mode")
    print(W.read())
    W.seek(0)
    W.write("\nvamsi\nramya\njaya\nsrinu\n")


with open('Samples.txt','a+') as W:
    print("a+ mode")
    W.write("\nvamsi\nramya\njaya\nsrinu")
    W.seek(0)
    print(W.read())

import os
os.mkdir("Sample2")
os.rmdir("Sample2")'''

#Regular Expressions
import re
'''p = '[a-z]'
t = 'camsi'
r = re.match(p,text)
print(r.group()if r else "No match found ")'''

'''
pattern = '[a-z]'
t = 'vamsi123@gmail.com'
r = re.search(pattern,t)
print(r.group() if r else "No match found ")'''


'''
pattern = '[a-z]'
t = 'vamsi123@gmail.com'
r = re.findall(pattern,t)
print(r)
'''

'''pattern = '[a-z]'
t = 'vamsi123@gmail.com'
r = re.finditer(pattern,t)
for i in r:
    print(i.group(),i.start())'''

'''p = '[1-9]{9}'
t = '123456789'
r = re.fullmatch(p,t)
print(r.group()if r else "No match found ")'''

'''p = 'r[,a+yn]'
t = 'python,java,maths'
r = re.fullmatch(p,t)
print(r)'''

p = '[1-9]{2}'
t = 'python : 12,maths : 20,science : 99'
r = re.sub(p,"**",t)
print(r)



    
    
    
    
    


    
