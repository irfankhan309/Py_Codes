class supermarket:
    def __init__(self,cnumber,item,cost,qty):
        self.cnumber=cnumber
        self.item=item
        self.cost=cost
        self.qty=qty
    def total(self):
        print('*'*30)
        print('cnumber items  cost  qty')
        print('*'*30)
        print('number is:',self.cnumber)
        print('items are:',self.item)
        print('total cost:',self.cost)
        print('qyt is:',self.qty) 
        print('*'*30)
        
import time
time.sleep(4)
import random

a=[10,20,30,40,50]
b=[90,45,34,32]
c=random.choice(a)
print(c)
time.sleep(2)
d=random.choice(b)
print(d)
time.sleep(2)
e=c+d
print(e)

import math
a=10
b=20
c=math.factorial(a)
time.sleep(3)
c1=math.pow(b,2)
print(c)
print(c1)


        


    
        
