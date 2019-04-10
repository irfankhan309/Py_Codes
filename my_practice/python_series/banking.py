import logging
import datetime
import math
import os
import sys
import random

logging.basicConfig(filename='myfile.txt',format='%(message)s')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

bank='sbi bank'
while True:
    cust=eval(input('enter user name and password:'))
    if cust == 'irfan309':
        cusp=eval(input('password:'))
    if cusp == 'khan309':
        logger.info('you sign in successfully')
        deposit=eval(input('how much want to deposit:'))
        deposited = deposit
        cust=deposited  
        logger.info(cust)
        askagain=eval(input('do you want to diposit more:'))
        if askagain =='yes':
            deposit=eval(input('how much:'))
            deposited=deposit
            sum =(cust+deposited)
            logger.info('your available amount:%s',sum)
        need=eval(input('do you want to withdraw:'))
        if need == 'yes':
            withdraw=eval(input('Enter the amount to withdraw:'))
            logger.info('please wait and collect the money:')
            operate=(sum-withdraw)
            logger.info('amount available in your account:%s',operate)
            logger.info('thanks for using our bank visit again!')
    else:
        logger.info('wrong attempt try again!')
        

    
    

    
