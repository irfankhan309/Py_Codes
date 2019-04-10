class student:
	def __init__(self,sno,sname):
		self.sno=sno
		self.sname=sname
	
	
	def sinfo(self):
		print("the student number is:",self.sno)
		print("the student name is:", self.sname) 
		
s1=student('08DN1A0526', 'irfankhan')
s1.sinfo() 