def f1():
    c1=eval(input('amount:'))
    c2=eval(input('amount2:'))
    print('\1.sum\n2.subtraction\n3.multiplication\n4.division')
    choice=eval(input('enter the which operation you want:'))
    if choice ==1:
        print('sum of numbers:',c1+c2)
    elif choice ==2:
        print('subtracted values are:',c1-c2)
    elif choice ==3:
        print('the multiplicated values:',c1*c2)
    elif choice ==4:
        print('the divided values:',c1//c2)
    else:
        print('wrong attempt')




def f2():
    print('hello every one')
    print('\n1.calculator\n2.call\n3.message')
    query= eval(input('enter what you want to do now:'))
    if query ==1:
          f1()
          
#def calc(a,b):
#    sum=a+b
#     sub=a=b
#    mul=a*b
#    div=a/b
#    t=sum,sub,mul,div
 #   return sum,sub,mul,div
#t=calc(100,20)
#for x in t:
 #   print(x)



# variable length arguments example:----------
#def sum(*n):
#    result=0
#    for x in n:
#        result=result+x
#         print('the sum:',result)


#sum(10)
#sum(10,20)
#sum(10,20,30)
#sum(10,20,30,40,50)
#----------------------------------------
#def dis(**n):# '**n' i.e., ** is for no of items we can create in function

#    print('record file:')
#    for x,y in n.items():
#        print(x,'.....',y)


#dis(name='irfan',age=28,marks=100,gender='male',status='married')
#dis(mobile=809898999,email='irfanqehs@gmail.com',address='23-88/32/1',gender='male')
##dis(mobile=909989898,company='tcs',father='salar',mother='batul',brother='sardar',business='autodealing',wokring_hrs='10am-07pm')
#-------------------------------------------------------------------------------------------------------------------------------------

#global variable and local variables
a=10
def f1():
    print('f1:',a)#first fucntion we are accessing the gloabal variable 'a'
    
def f2():
    print('f2:',a)#in second function also we are accessing the global variable  'a'

#f1()
#f2()
#-----------------------------------------------------------------------------------
a=10
def f1():
    global a
    a=999
    print('f1:',a)

def f2():
    print('f2:',a)


#f2()
#f1()
#-------------------------------------------------------------------------------------































        





























    
