# rename of .dat file
# Coded by Takuro TOKUNAGA
## Last updatae: June 07 2022

import numpy as np
import shutil
import os
import time

start = time.time()

def RenameToCoil(WorkDir, arg_num):

    coil_wrl = 'Part_' + str(arg_num) + '.wrl'
    rename_wrl = 'coil.wrl'

    wrl_path = os.path.join(WorkDir, coil_wrl)
    rename_path = os.path.join(WorkDir, rename_wrl)

    src = wrl_path # source
    dest = rename_path # destination
    shutil.copy(src,dest)


def RenameInOrder(WorkDir): # WorkDir: .wrl file foler
    #
    wril_files = glob.glob(os.path.join(WorkDir, '*.wrl'))

    i = 1
    for file in wril_files:
        os.rename(file, WorkDir + 'Part_' + str(i) + '.wrl')
        i+=1

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
