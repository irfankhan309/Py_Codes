import logging

#logging.basicConfig(format='%(message)s')
#logger=logging.getLogger()
#logger.setLevel(logging.INFO)


def some():
    a=10
    if a==10:
        logger.info('ok')
    else:
        logger.info('wrong')


logging.basicConfig(format='%(message)s')
logger=logging.getLogger()
logger.setLevel(logging.INFO)

def cal(a,b):
    sum=a+b
    logger.info(sum)

#file hanlding..
    
myfile=open('files_handling.txt','w')
myfile.write('this is again iam trying\n')
list=['irfan\n','khan\n','pathan\n']
myfile.writelines(list)

print('data written succefully')



    



    
