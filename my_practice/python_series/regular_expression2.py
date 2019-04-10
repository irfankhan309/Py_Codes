import re
def reg():
    s=input('enter registration number:')
    m=re.fullmatch('TS[0-2][0-9][A-Z]{2}\d{4}',s)
    if m!=None:
        print('valid Number')
    else:
        print('invalid number')

def reg1():
    s=input('enter mobile number:')
    m=re.fullmatch('(0|91|\+91)?[6789]\d{9}',s)
    if m!=None:
        print('valid number')
    else:
        print('invalid number')
#-------------------------------------------------------------
















    
