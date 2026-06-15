#Functions --> It is a reusable block of code and performing the tasks
'''
1) Reusable
2) Debugging
3) reduce Repetation
4) 
'''

'''
def iseven(num):
    if num%2==0:
        return f"{num} is Even "
    else:
        return f"{num} is not Even "

num = int(input("Enter a number : "))
print(iseven(num))
'''


'''def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return f"Factorial of {num} is {fact}"
    

num = int(input("Enter a number : "))
print(fact(num))


def isprime(num):
    for i in range(1,num//2):
        if i%2 == 0:
            return f"{num} Not is a prime number"
    return f"{num} a Prime nummber"
num = int(input("Enter anumber : "))
print(isprime(num))

#Type of Arguments

# 1) Positioning Argument
#example :
def details(name,email,password):
    print("Name : ",name)
    print("Email-Id : ",email)
    print("Password : ",password)

details("Vamsi","vamsi@gmail.com0","1211212ddsmkdNk")
details("Vamsi","vamsi@gmail.com0","1211212ddsmkdNk")
details("Vamsi","vamsi@gmail.com0","1211212ddsmkdNk")


# 2) Keyword Arguments

def details(name,email,password):
    print("Name : ",name)
    print("Email-Id : ",email)
    print("Password : ",password)

details(name="Vamsi",email="vamsi@gmail.com0",password="1211212ddsmkdNk")
details(email="Vamsi",password="vamsi@gmail.com0",name="1211212ddsmkdNk")

# 3) default arguments

def details(name,email,password ="Default_9392929"):
    print("Name : ",name)
    print("Email-Id : ",email)
    print("Password : ",password)

details(name="Vamsi",email="vamsi@gmail.com0")


# 4) Variable length arguments

def details(*names):
    print("Name : ",names)

details("Vamsi","vamsi@gmail.com0")
'''

def details(**names):
    print("Name :",names)

details(j1="Vamsi",j2="vamsi@gmail.com0")







