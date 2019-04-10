import re
def reg():#inthis function we just searching the pattern in string
    count=0
    matcher=re.finditer('ab','abababababaaa')
    for m in matcher:
        count=count+1
        print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
    print('the number of occurance:',count)
    
def regex():
    matcher=re.finditer('[abc]','a7b@k9z')
    for m in matcher:
        print(m.start(),'....',m.group())

def regex1():#in this example we just finding the a-z only..
    matcher=re.finditer('[a-z]','a7b@k9z')
    for m in matcher:
        print(m.start(),'...',m.group())


def regex2():#in this function we just taking 0-9 only
    matcher=re.finditer('[0-9]','a7b@k9z')
    for m in matcher:
        print(m.start(),'....',m.group())
        

def re3():
    matcher=re.finditer('[^a-zA-Z0-9]','a7b@k9z')
    for m in matcher:
        print (m.start(),'....',m.group())
        
def re4():
    matcher=re.finditer('[a-zA-Z0-9]','a7b@k9z')
    for m in matcher:
        print(m.start(),'...',m.group())
        

# predifined character in regular expressions....

def prere():# in this function we can find out where space is available
    matcher=re.finditer('\s','a7b @k9z')
    for m in matcher:
        print(m.start(),'....',m.group())

def prere1():
    matcher=re.finditer('\S','a7b @k9z')
    for m in matcher:
        print(m.start(),'....',m.group())

def prere2():#in this function we can find the where only digits availaleb
    matcher =re.finditer('\d','a7b @k9z')
    for m in matcher:
        print(m.start(),'...',m.group())
        
def prere3():# in this function we can have everything except digits 
    matcher=re.finditer('\D','a7b @k9z')
    for m in matcher:
        print(m.start(),'..',m.group())

def prere4():# in this function we have everything except special character and spaces
    matcher =re.finditer('\w','a7b @k9z')
    for m in matcher:
        print(m.start(),'...',m.group())

def prere4():#in this \W we can have only special character 
    matcher=re.finditer('\W','a7b @k9z')
    for m in matcher:
        print(m.start(),'...',m.group())

def prere5():# with '.' we can have everty thing in string....
    matcher=re.finditer('.','a7b @k9z')
    for m in matcher:
        print(m.start(),'....',m.group())

#qauntifiers.........................

def qntf():
    matcher=re.finditer('a+','abaabaaab')
    for m in matcher:
        print(m.start(),'....',m.group())

def qnti():
    matcher=re.finditer('a*','abaabaab')
    for m in matcher:
        print(m.start(),'....',m.group())
        



def fullmatc():
    s=input('enter pattern to check:')
    m=re.fullmatch(s,'abcdefgh')
    if m!=None:
        print('full string matched')
    else:
        print('full string not matched')

def search():
    s=input('enter pattern to check:')
    m=re.search(s,'abaabaaab')
    if m!=None:
        print('mathc is available')
        print('first occurance with start index:{} and  index:{}'.format(m.start(),m.end()))
    else:
        print('full string not matched')

def reg():
    s=input('enter registration Number:')
    m=re.fullmatch('TS[012][0-9][A-Z]{2}\d{4}',s)
    if m!=None:
        print('valid Number')
    else:
        print('invalid Number')
        










































































        






























        
        





































        





















































































