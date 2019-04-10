'''this program to get the output where our input is like alphanumeric but we
have to get in alphabets in sequence and digits in ascending order'''

s=input('enter some string:')
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)
#-------------------------------------------------------------------------------
# program to print charater at odd position and even position for the given string

#s=input('enter some string:')   # 1st way to print
#print('character at even position :',s[::2])
#print('character at odd position :',s[1::1])

#2nd method to print odd position and even position for the given string

#s=input('enter some string:')
#i=0
#print('the character at even position:')
#while i<len(s):
 #   print(s[i],end='')
  #  i=i+2
#print('the character at odd position:')
#i=1
#while i<len(s):
 #   print(s[i],end='')
  #  i=i+2

#-----------------------------------------------------------------------

# a program to remove the duplicates from the given string

#s=input('enter some string:')
#l=[]
#for x in s:
 #   if x not in l:
 #       l.append(x)
#output=''.join(l)
#print(output)
#-------------------------------------------------------------
 # A PROGRAM TO FIND THE NUMBER OF OCCURENCES OF EACH CHARACTER IN GIVEN STRING
s=input('enter the characters:')
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
for i,r in d.items(): # HERE i,r are key and values in the d={} we can define with any thing 
    print('{} occures {} times'.format(i,r))
    
















































    

    

