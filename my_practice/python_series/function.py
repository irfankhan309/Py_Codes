import logging

logging.basicConfig(format='%(message)s')
log=logging.getLogger()
log.setLevel(logging.INFO)


def ask():
    s =int(input('enter the first number:'))
    sa=int(input('enter second number:'))
    div=s/sa
    log.info(div)
    sub=s-sa
    log.info(sub)
    sum=s+sa
    log.info(sum)
    mul=s*sa
    log.info(mul)
    log.info('done')

def calc():
    a=eval(input('enter first number:'))
    b=eval(input('enter second number:'))
    sum=a+b
    log.info('addition of sum :%s',sum)
    sub=a-b
    log.info('subtraction of a and b:%s',sub)
    mul=a*b
    log.info('multiplied values :%s',mul)
    total=(sum,sub,mul)
    log.info(total)
    file=open('myfile.txt','w+')
    text=file.writelines(sum,sub,mul)
    log.info(text)
    
#--programms is to taking one pic from current location to same location with new file name using file concept
def creatpic():
    f1=open('first.jpg','rb')
    f2=open('second.jpg','wb')
    bytes=f1.read()
    f2.write(bytes)
    print('new images is a with name of nature:second.jpg')



#creating csv (comma seperated values) files using python files concept that is employee info stroing into a csv file
import csv
with open('empl.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Eno','Ename','Eadd','Esal'])
    n=int(input('enter number of employes:'))
    for i in range(n):
        eno=int(input('enter employee number:'))
        ename=input('enter employee name')
        eadd=input('enter employee address:')
        esal=input('enter employee salary:')
        w.writerow([eno,ename,eadd,esal])
print('total employees data written into csv fiel successfully')
#---------------------------------------------------------------------
#a program to zip the files

from zipfile import *
f=ZipFile('all.zip','w',ZIP_DEFLATED)
f.write('test.txt')
f.write('myfile.txt')
f.write('test1.txt')
f.write('mycode.py')
f.close()
print('all.zip file is create successfull')




























        







