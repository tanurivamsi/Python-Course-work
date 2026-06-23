#Date and time Modules
from datetime import date,time,datetime,timedelta
'''t = date.today()
print(t)
print(t.year)
print(t.day)
print(t.month)
print(t.weekday())
print(t.isoweekday())
print(f"Valid date : {date(2026,6,23)}")
print(f"Valid time : {time(20,6,2)}")

t = datetime.now()
print(t)
print(f"day : {t.day}")
print(f"year : {t.year}")
print(f"month : {t.month}")
print(f"hour : {t.hour}")
print(f"minut : {t.minute}")
print(f"seconds : {t.second}")
'''

#Recommanded formatting for date and time
'''
n = datetime.now()
print(n.strftime("%A %d %B %Y %I:%M:%S  %p"))


print(n+timedelta(days=2))
print(n+timedelta(hours=2))
print(n+timedelta(seconds=2))'''

#exceptional handling

'''
try:
    #n = int(input("Enter your age here : "))
    #print(b)
    #print(3+"11")
    l = [1,2,34,3]
    #print(l[10])
    d = {1:2,3:2,4:1}
    #print(d[10])
except ValueError:
    print("Enter valide age: ")
except NameError:
    print("Enter valide Name: ")
except TypeError:
    print("Enter valide Type: ")
except IndexError:
    print("Enter valide Index: ")
except KeyError:
    print("Enter valide key: ")
else:
    print(f"age : {n}")
finally:
    print("Thankyou")
'''
'''try:
    #n = int(input("Enter your age here : "))
    #print(b)
    #print(3+"11")
    l = [1,2,34,3]
    #print(l[10])
    d = {1:2,3:2,4:1}
    print(d[10])
except (ValueError,NameError,TypeError,IndexError,KeyError) as a:
    print("Enter valide Data :",a)

else:
    print(f"age : {n}")
finally:
    print("Thankyou")'''


#Recommended Exceptional handling syntax
'''try:
    #n = int(input("Enter your age here : "))
    print(b)
    print(3+"11")
    l = [1,2,34,3]
    print(l[10])
    d = {1:2,3:2,4:1}
    print(d[10])
except Exception as a:
    print("Enter valide Data :",a)

else:
    print(f"age : {n}")
finally:
    print("Thankyou")'''

try:
    n = int(input("Enter your amount : "))
    if n < 0:
        raise Exception("Enter the value from Zero only")
except Exception as a:
    print("Enter valide Data :",a)

else:
    print(f"amount : {n}")
finally:
    print("Thankyou")





