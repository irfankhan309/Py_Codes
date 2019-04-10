# to find the substring how many time is occured in number of indexes 

s=input('enter the main string:')
subs=input('enter the substring:')
flag=False  
irfan=-1 #variable can take any thing here like in example we taken as POS 
n=len(s)
while True:
    irfan= s.find(subs,irfan+1,n)
    if irfan ==-1:
        break
    print('found at index:',irfan)
    flag=True
if flag==False:
    print('not found')
