import re
s=input('enter mobile  number:')
m=re.fullmatch('(0|91|\+91)?[6789]\d{9}',s)
if m!=None:
    print('valid number')
else:
    print('invalid number')
    
