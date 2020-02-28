import re
import urllib.request

# It matches the vehicle number validation 
def registratio_num_check():  #TS 09 AA 1234
    q = input('enter vehicle registration number:')
    try:
        pattern = 'TS[012][0-9][A-Z]{2}\d{4}'
        match = re.fullmatch(pattern,q)
        matched = match.group()
        last_number = matched[6:]
        if last_number == '0000':
            print('enterd number is not valid with all zeros\'s')
        else:
            print('enterd number is valid',matched)
    except Exception as msg:
        print('you enterd number is wrong:',msg)


registratio_num_check()




# it matched the given mail id 
def check_mail():
    q = input('enter you gmail address only:')
    pattern = '\w[a-zA-Z0-9_.]*@(gmail|yahoo)[.][\w]+'
    match = re.fullmatch(pattern,q)
    if match != None:
        print('valid mail ID',q)
    else:
        print('mail id is not valid please enter valid one')


# check_mail()


# grabbing the phone and pin numbers from websites using regular expression
def scrap():
    url = ('http://www.redbus.in/info/contactus')
    u = urllib.request.urlopen(url)
    text = u.read()
    # number = re.findall('\d{3}[-]\d{8}',str(text))
    number = re.findall('[+91]\d{10}',str(text))
    pin = re.findall('[ -]\d{6}',str(text))
    li =[]
    for p in pin:
        if p.startswith('-'):
            pp = p.replace('-','')
            li.append(pp)
            print(pp)




# grabbing the titles from websites using regular expression

def webscraping():
    sites = ['http://www.rediff.com','http://www.google.com']
    for site in sites:
        print('searching...',site)
        u = urllib.request.urlopen(site)
        text = u.read()
        title = re.findall('<title>.*</title>',str(text),re.IGNORECASE)
        index = title[0]
        print(index)



# matching the valid mobile number with re
def mobile():

    pattern = '[6-9]\d{9}'
    q = input('enter mobile:')
    match = re.fullmatch(pattern,q)
    if match != None:
        print('you entered you mobile number:',q)
    else:
        print('this number is exceeded limit or gien below numbers')



# matching the email validate
def email():
    mail_pattern = '[a-zA-Z._]*[0-9]*@[a-z]*.com'
    q = input('enter you mail:')
    match = re.fullmatch(mail_pattern,q)
    if match !=None:
        print('you entered email:',q)
    else:
        raise ('entered maild id is not secured or all sensitive characters')


# finding the phone numbers in file using regular expression
def file():
    f1 = open('first.txt','r')
    f2 = open('second.txt','w')
    pattern = '[6-9]\d{9}'

    for line in f1:
        list = re.findall(pattern,line)
        for number in list:
            f2.write(number + '\n')
    print('extracted all number ')
    f1.close()
    f2.close()

























