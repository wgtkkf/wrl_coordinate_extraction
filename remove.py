# removal of directory
# Coded by Takuro TOKUNAGA
# Created: June 07 2022

import numpy as np
import shutil
import glob
import os
import time

start = time.time()

def RemoveDirectory(DirectoryPath):

    # remove the followings
    # 1. Part_N directory, N is a number
    # 2. j_Part_N.wrl files, N is a number
    # 3. .dat files
    # 4. coil.wrl file

    temp = os.listdir(DirectoryPath) # do not delete

    files = glob.glob(os.path.join(DirectoryPath + '\*.dat'))
    counter = 0
    for file in sorted(files):
        counter += 1

    try:
        for i in range(1, counter+1, 1):
            # remove directory
            try:
                rDir = 'Part_' + str(i) # rDir: Directory to be removed
                print(os.path.join(DirectoryPath, rDir))
                shutil.rmtree(os.path.join(DirectoryPath, rDir)) # directory remove
            except:
                print('No directorys are found.')

            # remove j_Part_#.wrl file
            j_wrl_file = 'j_Part_' + str(i) + '.wrl'
            try:
                os.remove(os.path.join(DirectoryPath, j_wrl_file))
            except:
                print('No j_Part files are found.')

        # remove .dat file
        for item in temp:
            if item.endswith(".dat"):
                os.remove(os.path.join(DirectoryPath, item))

        # remove coil.wrl
        Coilwrl = 'coil.wrl'
        Coilwrl = os.path.join(DirectoryPath, Coilwrl)
        os.remove(Coilwrl)

    except:
        print('Removal completion.')

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
