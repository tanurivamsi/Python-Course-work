#1) Single Inheritence
'''class w1:
    def me():
        print("You can message ")
class w2:
    def cal(me):
        print("you can call")
v = w1()
v.me()
v2 = w2()
v2.cal()
v2 = me()'''


#2)Multiple Inheritence
'''class w1:
    def me(self):
        print("You can message ")
class w2:
    def call(self):
        print("you can call")
class w3:
    def media(self):
        print("you can send media")
class w4:
    def status(self):
        print("you share status")
class w5(w1,w2,w3,w4):
    def location(self):
        print("you can share location ")
v = w5()
v.me()
v.call()
v.media()
v.status()
v.location()
#v2.cal()
#v2 = me()'''

#3)Multi-Level Inheritence
'''class w1:
    def me(self):
        print("You can message ")
class w2(w1):
    def call(self):
        print("you can call")
class w3(w2):
    def media(self):
        print("you can send media")
class w4(w3):
    def status(self):
        print("you share status")
class w5(w4):
    def location(self):
        print("you can share location ")
v = w5()
v.me()
v.call()
v.media()
v.status()
v.location()
v2 = w3()
v2.media()
v2.me()
v2.call()'''

#4)Hierarchy Inheritence

class w1:
    def me(self):
        print("You can message ")
class w2(w1):
    def emoji(self):
        print("you can send emojis")
class w3(w1):
    def stickers(self):
        print("you can send stickers")
'''class w4(w3):
    def status(self):
        print("you share status")
'''
'''
v = w2()
v2 = w3()
v.me()
v.emoji()
v2.stickers()
v2.me()

#5)Hybrid inheritence
class w1:
    def me(self):
        print("You can message ")
class w2(w1):
    def emoji(self):
        print("you can send emojis")
class w3(w1):
    def stickers(self):
        print("you can send stickers")
class w4(w3,w2):
    def gif(self):
        print("you share status")


v = w2()
v2 = w3()
print("Version-1 : ---------------------------------------------------------")
v.me()
v.emoji()
print("Version-2 : -----------------------------------------------------------")
v2.stickers()
v2.me()
v3 = w4()
print("Version-4 ---------------------------------------------------------------")
v3.me()
v3.emoji()
v3.stickers()
v3.gif()
'''

#Super Kerword

'''class w1:
    def status(self):
        print("You can message ")
class w2(w1):
    def status(self):
        super().status()
        print("you can send emojis")
class w3(w2):
    def status(self):
        super().status()
        print("you can send stickers")
v = w3()
v.status()'''

#Multiple in without super keyword
class w1:
    def status(self):
        print("You can message ")
class w2():
    def status(self):
        print("you can send emojis")
class w3(w1,w2):
    def status(self):
        w1.status(self)
        w2.status(self)
        print("you can send stickers")

v = w3()
v.status()



