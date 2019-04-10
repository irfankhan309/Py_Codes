class info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def about(self):
        print('my name :',self.name)
        print('my age:',self.age)

class student(info):
    def __init__(self,marks,number):
        self.marks=marks
        self.number=number

    def sinfo(self):
        print('marks:',self.marks)
        print('roll number :',self.number)


class employee(info):
    def __init__(self,ID,salary):
        self.ID=ID
        self.salary=salary

    def einfo(self):
        print('employee ID number :',self.ID)
        print('employee salary:',self.salary)

