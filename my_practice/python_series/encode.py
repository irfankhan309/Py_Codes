import logging


logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

print('this  is Has-A relations ship example(compostion)')
class car:
    def __init__(self,no,color):
        self.no=no
        self.color=color
    def getinfo(self):
        print('the car no:{},and color:{} '.format(self.no,self.color))

class employee:
    def __init__(self,eno,esal,car):
        self.eno=eno
        self.esal=esal
        self.car=car
    def display(self):
        print('the employee number:',self.eno)
        print('the employee salary:',self.esal)
        print('the employee details are:')
        self.car.getinfo()

c=car(2222,'grey')
e=employee(101,45000,c)
e.display()
print('*'*30)

#----------------------second example for composition,(IS-A relationship)

class parent:
    def __init__(self,pname,age):
        self.pname=pname
        self.age=age
    def getinfo(self):
        print('his parent name:{} and age {}'.format(self.pname,self.age))

class child:
    def __init__(self,cname,cage,cscl,parent):
        self.cname=cname
        self.cage=cage
        self.cscl=cscl
        self.parent=parent
    def display(self):
        print('the child name:',self.cname)
        print('the child age:',self.cage)
        print('the child school :',self.cscl)
        print('the parent details here:')
        self.parent.getinfo()

p=parent('sam',52)
c=child('john',15,'avcr',p)
c.display()

#---------------------------------------------------------------------------

class toyota:
    def __init__(self,regno,tnover):
        self.regno=regno
        self.tnover=tnover
    def getinfo(self):
        print('the toyota registration number :{},and turnover {}'.format(self.regno,self.tnover))

        



































    
    



































        
            

        
    
                
