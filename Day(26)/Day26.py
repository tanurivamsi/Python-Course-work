#Polymorphism
'''class hotstar:
    def __init__(self,name):
        self.name = name
        print(f"Hi {name} ,welcome to the hotstar")
    def login(self):
        print(f"Hi {self.name} You can login")
    def dashboard(self):
        print("You can access the Dashboard")
    def search(self):
        print("You can access the search")
    def laguage(self):
        print("You can access the language")
    def playcontro(self):
        print("You can access the playControl")
    def quality(self):
        print("You can not access the Quality")
    def Ads(self):
        print("You can not  stop the Ads")

class p_h(hotstar):
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name} you can access Primium Hotstar")
    def quality(self):
        print("You can access the Quality")
    def Ads(self):
        print("You cann't get the Ads")
    def movies(self):
        print("You can access movies")
    def sports(self):
        print("You can access sports")
        
    
    

v = hotstar("Vamsi")
print("---------------------Hotstar Account--------------------")
v.login()
v.dashboard()
v.search()
v.laguage()
v.playcontro()
v.quality()
v.Ads()
print("---------------------Priemium Account--------------------")
v1 = p_h("Ramya")
v1.movies()
v1.sports()
v1.quality()
v1.Ads()
v1.login()
v1.dashboard()
v1.search()
v1.laguage()
v1.playcontro()

'''
'''


#Operator Overloading
class O_l:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
    def __lt__(self,other):
        return self.num<other.num
    def __gt__(self,other):
        return self.num>other.num
    def __mul__(self,other):
        return self.num*other.num
    def __eq__(self,other):
        return self.num==other.num
    def __str__(self,other):
        return str(self.num,other.num)

n1 = O_l(10)
n2 = O_l(22)
print(n1+n2)
print(n1>n2)
print(n1-n2)
print(n1*n2)
print(n1==n2)
print(n1<n2)
print(n1,n2)

 '''       
        
#Problems
#1)
class Printer:
    def print_file(self):
        print("Generic printing")

class InkjetPrinter(Printer):
    def print_file(self):
        print("Inkjet printing...")

class LaserPrinter(Printer):
    def print_file(self):
        print("Laser printing...")
o = Printer()
o.print_file()
o2=InkjetPrinter()
o2.print_file()
o3=LaserPrinter()
o3.print_file()

