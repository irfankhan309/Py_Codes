import logging

logging.basicConfig(filename='myfile.txt',format='%(asctime) %(message)s',filemode='w')
logger=logging.getLogger('FIRST APP')
logger.setLevel(logging.DEBUG)
logger.debug('iam debug')
