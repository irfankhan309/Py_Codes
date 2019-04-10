import test
test.hotel()
test.take_away()

import time


def test1():
    print("*"*80)
    print("if you had your meal please make the payment")
    table=100
    table=int(input("enter the table number:"))
    if table==100:
        print("please wait for your bill!")
        time.sleep(5)
        chicken=65
        mutton=230
        bread=59
        total=chicken+mutton+bread
        time.sleep(10)
        print("the total bill is:",total)
        print("*"*80)    



def test2():
    
    table=100
    table=int(input("hai please enter your table for your parked vehicle bill:"))
    if table==100:
        print("your parked vehicle time till now 1:30hrs")
        min=30
        onehour=50
        twoh=60
        threeh=70
        print("your bill is for 1:30hr:",min + onehour)
        print("visit again, thanks")



def test3():
    print("hai welcome to boating")
    table=100
    table=int(input("enter your table number for alloted boat for your:"))
    if table==100:
        print("your alloted boat is BT100")
        print("tariff details for boating")
        print("*"*80)
        print("the bill for spent time is:150")
        print("*"*80)
        


















