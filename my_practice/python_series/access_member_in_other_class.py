import logging

logging.basicConfig(filename='log.txt',level=logging.INFO)
logging.info('a ne request came')
try:
    x=int(input('enter first num:'))
    y=int(input('enter second:'))
    print(x/y)
except ZeroDivisionError as msg:
    print('can not divide with zero')
    logging.exception(msg)
#

