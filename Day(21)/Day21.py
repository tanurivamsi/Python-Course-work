'''def display():
    for i in range(1,11):
        yield i

p = display()
for i in range(5):
    print(next(p))'''


'''def fact(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

p = fact(100)

try:
    while True:
        print(next(p))
except StopIteration:
    print("End of the Iteration") 

def fact(n):
    return [i for i in range(1,n+1) if i%n==0]
def generators(res):
    for i in res:
        yield i

res = fact(10)
facts = generators(res)

for i in range(len(res)):
    print(next(facts))'''

def prime():
    res = []
    for n in range(2,101):
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            res.append(n)

    return res
def generators(res):
    for i in res:
        yield i

res = prime()
g = generators(res)

for i in range(len(res)):
    print(next(g))

