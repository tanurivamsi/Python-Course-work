'''#1 positive or negitive
n = int(input())
if n <  0:
    print("Negitive")
elif n > 0:
    print("Positive")
else:
    print(0)'''
    
#2)Even or odd
'''n = int(input())
if n%2 == 0:
    print('even number')
else:
    print("Odd Number")'''
    
#3) Divisible by 5
'''N = int(input())
if N%5 == 0:
    print("Divisible by 5")'''
    
#4)Divisible by 3 and 7 
'''n = int(input())
if n%3 == 0 and n%7 == 0:
    print("Divisible by 3 and 7")
else:
    print("Not Divisible by 3 and 7")'''
    
#5 finging leap year
'''n = int(input())
if ((n%4 == 0) and (n%100 !=0)) or (n%400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")'''
    
#6 checking Marks 
'''m = int(input())
if m < 35:
    print("fail")
else:
    print("pass")'''
    
    
#7 checking  num is 3 disits or not
'''n = (input()) 
if len(n) == 3:
    print("3-Digit number")
else:
    print("Not 3-Digit number")'''
    
# cheching vowel or not
'''a = input()
if a.lower() in "aeiou":
    print("It is a vowel")
else:
    print("Not a Vowel")'''
    
    
#Checking  greatest numbers
'''n1,n2 = list(map(int,input().split(',')))
if n1 > n2:
    print(f"the number {n1} is greater")
else:
    print(f"the number {n2} is greater")'''
    
#Checking number 0
'''a = int(input())
if a == 0:
    print("Zero")
else:
    print("Not Zero")
    
#Checking multiple of 10
m = int(input())
if m%10 == 0:
    print("Multiple of 10")
else:
    print("not Multiple of 10")'''
    
'''#age eligibility
age = int(input())
if age < 18:
    print("Not Eligible to vote")
else:
    print("Eligible to vote")
    
#checking if number is in between 1 and 100
n = int(input())
if 1 <= n <=100:
    print("In Range")
else:
    print("Not in range") '''
    
#checking  number square
n1,n2 = list(map(int,input().split(',')))
s = n2**2
if n1 == s:
    print(f"the number {n1} is square of {n2}") 
else:
    print(f"the number {n1} is not a square of {n2}")

    


