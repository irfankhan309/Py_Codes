import time
#s=input('enter any string:')#we are reversing the given string.

#time.sleep(2)
#print(''.join(reversed(s)))

#for x in reversed(s):
 #   time.sleep(2)
  #  print(x)

#------------------------------------------------------------
#JOIN method in strings
s=input('enter any string for joining:')

s1='-'.join(reversed(s))#1st way to print the string
print(s1)

for x in reversed(s): #2nd way to print reverse the string
    print(x,end='')

print(s[::-1]) #sliceing with -1 to reverse the string

ss=input('enter some string:') #4th way to reverse the string with small code
i=len(ss)-1
op=''
while i>=0:
    op=op+ss[i]
    i=i-1
print(op)


    
