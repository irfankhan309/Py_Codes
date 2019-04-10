def some():
    try:
        print('this is try outer block')
        try:
            print(10+2)
            print(100*2)
            print(1000//25)
            print(100/0)
        except ZeroDivisionError:
            print('sorry 0 is not dividable')
        finally:
            print('now we are in finally block')
        print('now we are in outer try block')

    except ValueError:
        print('sory  this is value error')

    finally:
        print('this is outer finally block')
    print('this is also outer try block statement')

#some()

# this is nested function just for practicing my self
def things(x,y):
    print('this is logger')
    z=x*x
    zz=y*y
    print(z,zz)
    
    def some(a,b):
        print('the value  of a:',a)
        print('the values of b:',b)
        print('sum of :',a+b)
        print(b*b)
    some(10,20)
    some(5,4)
    some(2,4)
#things()

#----------------------------------------------------------
def exception():
    try:
        x=int(input('enter the first value:'))
        y=int(input('enter the second value:'))
        sum=x+y
        print(sum)
        if sum==10:
            print('tested ok')
        else:
            print('sorry wrong input')
        sub=x/y
        print(sub)
    except (ZeroDivisionError,ValueError):
        print('sorry if statement is not mached')
    finally:
        ('i will exectute whether exception raised or not')
#exception()


#here what is the difference between the exceptions and normal termination
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg



age=int(input('enter your age:'))
if age>60:
    raise TooYoungException('sorry conatct imam sahb')
elif age<18:
    raise TooOldException('sory contact your parents')
else:
    print('thanks for the regirstration')



    
































