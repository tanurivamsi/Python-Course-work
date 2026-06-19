'''d = {"a":20,"b":30,"c":10,"d":15}
dis = dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
#gst = dict(map(lambda i:(i[0],i[1]-i[1]*0.5),d.items()))
gst = dict(filter(lambda i:(i[1]>10),d.items()))

print(gst)


#list compressions
l = []
l2 = [i for i in range(2,21,2)]
print(l2)
l3 = [i for i in range(3,21,3)]
print(l3)
l4 = [i for i in range(4,21,4)]
print(l4)

a = "Vamsi"
l = [i for i in a if i in "aeiouAEIOU"]
print(l)


I = [1,3,4,56,66,4,3]
l = [i if i%2==0 else "Odd" for i in I]
print(l)

l = [int(input(f"Enter a number {i+1}th here: "))  for i in range(10)]
print(l)
l = [[j for j in range(1,4)] for i in range(3)]
print(l)

s = set()
S = {j for j in range(1,11) }
print(S)

d = {i:i*i for i in range(1,11)}
print(d)

d = {}
for i in range(5):
    d[input("Enter student name :")]= int(input("Enter the marks :"))

print(d)

d = {input("Enter student name :"):int(input("Enter the marks :") for i in range(3)}

print(d)'''

def display():
    l = ["1..10","10..100","100..150"]
    yield  l[0]
    yield  l[1]
    yield  l[2]

scroll = display()

print(next(scroll))
print(next(scroll))
print(next(scroll))

       

           
    




