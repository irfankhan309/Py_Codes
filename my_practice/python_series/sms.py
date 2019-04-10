import random
import math
import logging


def calc(a,b):
    try:
        sum=a+b
        print(sum)
        sub=a-b
        print(sub)
        div=a/b
        print(div)
    except ZeroDivisionError as msg:
        print('can not divide with zero',msg)
    else:
        print('your  got it everty thing')
    finally:
        print('finally we executed the cal')

calc(10,5)
    
