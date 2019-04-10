rec={}
n=(int(input('enter no of students:')))
i=1
while i<=n:
    name=input('enter the student name:')
    marks=input('enter the %of the student')
    rec[name]=marks
    i=i+1
print('name of student','\t','% of marks')
for x in rec:
    print('\t',x,'\t\t',rec[x])
        
