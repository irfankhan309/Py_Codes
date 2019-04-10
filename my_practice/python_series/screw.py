import math
import random
import os
import sys
import logging


logging.basicConfig(filename='myfile.txt',format='%(message)s')
log=logging.getLogger()
log.setLevel(logging.INFO)

log.info('hei')
