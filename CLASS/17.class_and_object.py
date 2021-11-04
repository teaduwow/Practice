#類別class 物件object
class phone:
    def __init__ (self,os,number,is_waterproof):  #底線案兩次 變長底線
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = phone ("ios",123,True)
print (phone1.os)

phone2 =phone ("android",456,False)
print (phone2.number)