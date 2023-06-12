# Coded by Takuro TOKUNAGA
# Created: March 14 2023
# Last updatae: June 07 2022

#import numpy as np
import os
import time
import itertools
from sys import exit
start = time.time()

def screenfilesize(WorkDir, FileName): # WorkDir: .wrl file foler
    #
    join_path = os.path.join(WorkDir, FileName)

    if os.path.getsize(join_path) > 10*1024: # 10 MB
        os.remove(join_path)

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
