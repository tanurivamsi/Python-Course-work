# 1)
'''l = list(map(int,input().split()))
print("length : ",len(l))
print("sorted list : ",sorted(l))
print("minimum : ",min(l))
print("maximum : ",max(l))

# 2)
t = tuple(input("Tuple : ").split())
pro = input("Product : ")
pri = int(input("Price : "))
set_values = set(map(int,input("Set values : ").split()))

print("Tuple : ",t)
di = {}
di[pro] = pri
print("Dictionary : ",di)
print("Set  : ",set_values)

# 3)
s = int(input())
bonus = 0
if s >= 70000:
    bonus = 0.2*s
elif s >= 50000:
    bonus = 0.15*s
elif s >= 30000:
    bonus = 0.1*s
else:
    bonus = 0.05*s

print("Bonus : ",bonus)

# 4)
age = int(input())
if age >= 18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")'''

# 5)





#Conditional statements Example program
#example :- 1
'''Data = {
    "Vamsi":{"Status":True,"Python":95,"mysql":88,"flask":99},
    "gaya":{"Status":False,"Python":None,"mysql":None,"flask":None},
    "Vasu":{"Status":True,"Python":65,"mysql":78,"flask":89},
    "Venu":{"Status":True,"Python":55,"mysql":68,"flask":59},
    "Varsha":{"Status":True,"Python":25,"mysql":28,"flask":49},
    }
name = input("Enter Student name : ")

if name in Data:
    if Data[name]['Status']:
        total = Data[name]['Python']+Data[name]['mysql']+Data[name]['flask']
        avg = total/3
        if avg > 90:
            print(f"congractulation {name}!!! . youu got marsks {total} and First grade")
        elif avg > 70:
            print(f"congractulation {name}!!! . you got marsks {total} and Distinction")
        elif avg > 50:
            print(f"congractulation {name}!!! . you got marsks {total} and pass need practice")
        elif avg < 35 :
            print(f"Sorry {name} . you got fail")
            
        else:
            print(f"Sorry {name} . you didn't attend the exam bring with your parents ")
            S
    
            
else:
    print(f"The name {name} is not Recorded")
    '''
#example :- 2
name = (input("Enter your Name here : "))
budget = int(input("Enter your budget here : "))
if budget > 50000:
    print(f"{name} You can go a trip!!!")
elif budget > 30000:
    print(f"{name} You can go a pub!!!")
elif budget > 10000:
    print(f"{name} You can go to buy a mobile!!!")
elif budget > 5000:
    print(f"{name} You can go a shopping!!!")
elif budget < 1000:
    print(f"{name} You can bet")
else : 
    print(f"{name} You can take")
