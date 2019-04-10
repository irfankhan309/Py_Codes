class trip:
    def __init__(self,tkno,name):
        self.tkno=tkno
        self.name=name
    def tinfo(self):
        print('NAME:',self.name)
        print('TICKET NO:',self.tkno)

t=trip('ABC123','irfan')
t.tinfo()
