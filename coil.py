# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Last updatae: June 07 2022

import numpy as np
import time
import pandas as pd
import glob
import os
from sys import exit
import shutil
import re
start = time.time()

def CoilCoordinate(WorkDir, arg_num):

    # read merged files, .data
    coil_path = 'Part_' + str(arg_num) + '.dat'
    join_path = os.path.join(WorkDir, coil_path)

    # open, coil .dat
    mf = pd.read_csv(join_path, sep=" ", header=None) # mf: merged file
    mf.columns = ["x", "y", "z"]
    row, col = mf.shape # row & column of matorix
    cfx = np.zeros(row, dtype='float64') # mfx: coordiante part x
    cfy = np.zeros(row, dtype='float64') # mfy: coordiante part y
    cfz = np.zeros(row, dtype='float64') # mfz: coordiante part z

    for i in range(0, row):
        cfx[i] = mf.iat[i,0] # x line
        cfy[i] = mf.iat[i,1] # y line
        cfz[i] = mf.iat[i,2] # z line

    # zmax
    cfzmax = max(cfz)
    # zmin
    cfzmin = min(cfz)

    # xmax
    cfxmax = max(cfx)
    # ymax
    cfymax = max(cfy)

    # x-y plane center of gravity (cog)
    cogx = sum(cfx)/row
    cogy = sum(cfy)/row

    # x-y plane outer radius
    rx = abs(cfxmax - cogx)
    ry = abs(cfymax - cogy)

    # averaged maximum outer radius
    roave = 0.5*(rx+ry)

    return cfzmax, cfzmin, roave, cogx, cogy

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
