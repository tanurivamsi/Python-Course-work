'''class flipkart:
    d = 10
    p = ['apple','mango','goa','carrot']
    @classmethod
    def show(c):
        print(c.p)
    def login(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to the flipkart {self.username}")

    @staticmethod
    def dis():
        print("10% Discount is going on in flipkart ")

a = flipkart()
a.login("vamsi","vamsi@123")
a.dis()
a.show()'''



class instagram:
    def __init__(self,name,p):
        self.name = name
        self.__p = p
        self.f = []
        print(f"Welcome to the instagram {self.name}")
    def getpassword(self):
        return self.__p

    def setpassword(self,newpassword):
        self.__p = newpassword
        

v = instagram("vamsi","vamsi@123500")

v.name = "Ramya"
print(f"After changed name : {v.name}")

print(f"Before changed password : {v.getpassword()}")
v.setpassword("Ramya@123")
print(f"After changed password : {v.getpassword()}")
'''
class Instagram:
    def __init__(self, name, p):
        self.name = name
        self.__p = p
        self.f = []
        print(f"Welcome to Instagram {self.name}")

    def getpassword(self):
        return self.__p

    def setpassword(self, newpassword):
        self.__p = newpassword


v = Instagram("vamsi", "vamsi@123500")

# Change name
v.name = "Ramya"
print(f"After changed name : {v.name}")

# Get current password
print(f"Before changed password : {v.getpassword()}")

# Change password
v.setpassword("Ramya@123")

# Get updated password
print(f"After changed password : {v.getpassword()}")
'''

        
    
