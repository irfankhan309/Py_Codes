def sum_dec(func):
    def inner(a,b):
        return a+b
    
    return inner

def sub_dec(func):
    def inner(a,b):
        c=a+b
        c1=c*2
        return c1
    
    return inner


@sub_dec
@sum_dec

def add(a,b):
    print('the values of sum:',a+b)

add(2,4)






#-------------------------

def wish_dec(func):
    def inner(name):
        print('heyaa how are you',name)
    return inner

def wish_dec1(func):
    def inner(name):
        print('as salamu alykum,kaifa haal',name)
    return inner
 



@wish_dec1
@wish_dec
def wish(name):
    print('hai',name)

wish('sam')
wish('irfan')

#------------------------------------------
#generators example 3

def mobile(num):
    def inner(std):
        print('the number is:',std)
        
    return inner

def mob1(num):
    def inner(std):
        print('this is finally phone number you are seeing here',std)
    return inner

@mob1
@mobile

def code(std):
    print('the code is',std)

code(91)
code(8008469093)
code(9030139353)



























