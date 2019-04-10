#THIS IS METHOD RESOLUTION ORDER (MRO),using C3 algorithm , (Linearization)
#1.magine you were implementing a programming language that featured inheritance.
#2.When you first approach this topic you decide:
#a child class will have all of the functions and attributes that it’s parent classes should have!

#Now this may work for the vast majority of scenarios but what would happen if two parent classes both implemented,
# the same function or attribute? How do you decide what function or attribute takes precedence?

class A:
    def m1(self):
        print('this is A class')
class B:
    def m1(self):
        print('this is class B')
class C:
    def m1(self):
        print('this is C class')

class Z:
    def m1(self):
        print('this is D class')

class X(A,B):
    def m1(self):
        print('this is X class')


class Y(B,C):
    def m1(self):
        print('this is Y class')

class P(X,Y,C,Z):#PXAYBCZO
    pass
    #def m1(self):
     #   print('this is P class')

                
p=P()
p.m1()
