import datetime
import time

class supermarket:
    def __init__(self,owner,workers):
        self.owner=owner
        self.workers=workers

    def mrng_login(self):
        login=eval(input("please login with your ID:"))
        time.sleep(3)
        if login==10786:
            print("irfan, access permitted!")
            t=datetime.datetime.now()
            print("irfan logined at",t)
        elif login==88909:
            print("supervisor accessed(sam)")
            t=datetime.datetime.now()
            print("supervisor login at",t)
        elif login==88910:
            print("floor incharge(john)")
            t=datetime.datetime.now()
            print("floor incharge john login at",t)
            time.sleep(3)
        else:
            t=datetime.datetime.now()
            print("wrong ID you have entered acess denied at",t)
            time.sleep(2)

    def first_meet(self):
        time.sleep(2)
        print("this is morning time first meet to implement the project and consider about the drawbacks")
        t=datetime.datetime.now()
        print('current time is',t)
        list=[1,2,3,4,5]
        time.sleep(1)
        for x in list:
            time.sleep(1)
            print(x)
        print("thanks")
        time.sleep(2)

    def docs(Self):
        print("*"*40)
        time.sleep(2)
        t=datetime.datetime.now()
        print("documentation work is in progress at:",t)
        time.sleep(2)
        print("*"*40)
        time.sleep(2)

    def lunch(self):
        t=datetime.datetime.now()
        print("lunch time starts at- 01:00pm")
        time.sleep(3)
        print("the current time is:",t)
        time.sleep(3)


    def brake(Self):
        t=datetime.datetime.now()
        time.sleep(2)
        brake=eval(input("enter your ID number:"))
        if brake==10786:
            time.sleep(3)
            print("sorry you are not permitter out side for the breake")
            time.sleep(3)
        elif brake==88909:
            time.sleep(2)
            print("you just have 10min time outside for breake")
        elif brake==88910:
            time.sleep(2)
            print("yo have olny 30 minutes permitted for breake outside")
            time.sleep(2)
            

            

    def evn_logout(self):
        logout=eval(input("enter ID:"))
        time.sleep(2)
        if logout==10786:
            t1=datetime.datetime.now()
            print("you are logged out at",t1)
        elif logout==88909:
            t=datetime.datetime.now()
            print("you are logged out",t)
        elif logout==88910:
            t=datetime.datetime.now()
            print("you are logged out",t)
        else:
            t=datetime.datetime.now()
            print("wrong attempt at ",t)
    def string(self):
        st=(input("enter the strings:"))
        subst=(input("enter the substring to search in string:"))
        if subst in st:
            print(subst ," is found in string")
        else:
            print(subs,"is not found in string")

    def strings(self):
        time.sleep(2)
        stri=input("enter the your order to check :")
        time.sleep(2)
        sstri=input("enter your ordered to check :")
        time.sleep(2)
        if sstri in stri:
            time.sleep(2)
            print(sstri,"you have ordered",sstri)
        else:
            print(sstri,"not ordered any thing till now",sstri)
            
        
            
            


        
        
    

sm=supermarket('irfan','khan')
sm.mrng_login()
sm.first_meet()
sm.docs()
sm.brake()
sm.lunch()
sm.strings()
sm.evn_logout()
sm.string()
