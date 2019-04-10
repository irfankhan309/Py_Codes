import time

def hotel():
        '''this hotel function is for booking the table with defined numbers as per requirement and taking input of from consumer
what he exactly requires\nwe have table numbers starts with 100 to 200 i.e..,\nwe have large space to book table as it containing 100 tables
starts with 100 and ends with 200
\nthanks for your interest'''
        print("welcome to BlueRose Hotel")
        
        table=int(input("enter your booked table to get your order now:"))
        if table==100:
                print("your family details:\n1.john\n2.alaska\n3.julie\n4.sam\n5.jonsen")


                print("plese wait we check what you ordered!")
                time.sleep(5)
                print("hello sir, your table no is 100,\nyour order is roasted chicken,\nthanks")
        elif table==101:
                print("hai your selected table number is 101, your oreder will server with in 20 min as others also waiting!")
        else:
                print("sorry you have attempted wrong table number!")

def take_away():
        print("please place an order:\npress the digits to order")
        print("*"*50)
        print("1.grilled chicken\n2.mutton chops\n3.manchuria\n4.noodles\n5.biryani\n6.mutton biryani")
        print("*"*50)
        order=int(input("select your dish:"))
        if order==1:
                order1=int(input("how many:"))
                gc=200
                time.sleep(5)
                print("you have ordered grilled chicken:")
                print("please pay the bill:",order1*gc)
                print("thanks,visit again Blue Rose hotel!")
        if order==2:
                order2=int(input("enter how many plates of chops:"))
                mc=150
                time.sleep(5)
                print("your orders is, mutton chops:")
                print("please pay the bill:",order2*mc)
                print("thanks,visit again Blue Rose hotel!")
        if order==3:
                order3=int(input("how many plates:"))
                mnc=80
                time.sleep(5)
                print("your order is manchuria:")
                print("please pay the bill:",order3*mnc)
                print("thanks,visit again Blue Rose hotel!")

        if order==4:
                order4=int(input("how many plates noodles:"))
                nd=70
                time.sleep(5)
                print("your oder is noodles:")
                print("please pay at counter:",order4*nd)
                print("thanks,visit again Blue Rose hotel!")

        if order==5:
                order4=int(input("how many plates biryani you want to order:"))
                bi=180
                print("your order is biryani,(",order4,")plates you have ordered:")
                time.sleep(5)
                print("please pay the bill:",order4*bi)
                print("thanks,visit again Blue Rose hotel!")
                
        if order==6:
                order6=int(input("how many plates of mutton biryani:"))
                mbi=280
                print("you have ordered mutton biryani(",order6,")plates")
                time.sleep(5)
                print("please pay the bill:",order6*mbi)
                print("thanks,visit again Blue Rose hotel!")
                












        
                
                
                
                
                
                
        
                
                
        


