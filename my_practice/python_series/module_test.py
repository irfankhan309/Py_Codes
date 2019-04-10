import os,sys

fname=input('enter file name:')
if os.path.isfile(fname):
    print('file exists:',fname)
    f=open(fname,'r')
else:
    print('file doesnt exisits:',fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print('the number of line:',lcount)
print('the number of words:',wcount)
print('the number of characters:',ccount)


#######################################################33

#binay data that is reading the binary data of image and writing to another place

