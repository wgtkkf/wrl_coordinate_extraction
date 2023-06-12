# Coded by Takuro TOKUNAGA
# Update history
# Created: April 20 2022
# Updataed: June 07 2022 / August 02, 03 2022 / June 12, 2023

import numpy as np
import time
import pandas as pd
import glob
import os
from sys import exit
import shutil
import re
start = time.time()

def JudgeCalculation(WorkDir, FolderName, czmax, czmin, coradius, cx, cy):

    FolderName = FolderName.replace('.wrl', '')      # remove .wrl

    dat_add = FolderName + '.dat'
    dat_path = os.path.join(WorkDir, dat_add)

    wrl_add = FolderName + '.wrl'
    wrl_path = os.path.join(WorkDir, wrl_add)

    # open
    mf = pd.read_csv(dat_path, sep=" ", header=None) # mf: merged file, .dat file of surrounding parts
    mf.columns = ["x", "y", "z"]
    row, col = mf.shape                   # row & column of matorix
    mfx = np.zeros(row, dtype='float64')  # mfx: coordiante part x
    mfy = np.zeros(row, dtype='float64')  # mfy: coordiante part y
    mfz = np.zeros(row, dtype='float64')  # mfz: coordiante part z
    dist = np.zeros(row, dtype='float64') # dist: distance table

    for i in range(0, row):
        mfx[i] = mf.iat[i,0] # x line
        mfy[i] = mf.iat[i,1] # y line
        mfz[i] = mf.iat[i,2] # z line

    # distance calculation from coil center of gravity, x-y plane
    for i in range(0, row):
        dist[i] = np.sqrt(np.power(mfx[i]-cx, 2.0) + np.power(mfy[i]-cy, 2.0))


    # call quick sort for judge 1 & 2 & 3
    quickSort(mfx, 0, row-1)  # object, min (=0), max (=row-1)
    quickSort(mfy, 0, row-1)  # object, min (=0), max (=row-1)
    quickSort(mfz, 0, row-1)  # object, min (=0), max (=row-1)
    quickSort(dist, 0, row-1) # object, min (=0), max (=row-1)

    # debug
    print('part: '+ str(wrl_add) + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(abs(cx - abs(mfx[row-1]))) + ' ' + str(abs(cy - abs(mfy[row-1]))) + ' ' + str(coradius))

    # flag initialization
    skipflag = 0              # 0: not skippded / 1: skipped

    # set parameters
    zmargin = 5               # unit: mm
    rmargin = zmargin         # unit: mm
    filter_distance = 100     # unit: mm
    filter_thicness = 10      # unit: mm

    # judge 0: far parts
    if abs(dist[0]) > filter_distance: # this is a fitting parmater
        print(FolderName + ' Distance [mm]: ' + str('{:.2f}'.format(dist[0])) + ',' + ' Too far part, skipped')
        skipflag = 1

    # judge 1 & judge 2: small thickness parts (filter 1 for noise parts removal)
    elif abs(abs(mfz[0])-abs(mfz[row-1])) <= filter_thicness or np.std(mfz) < filter_thicness: # 10, this is a fitting parmater
        print(FolderName + ' Noise part, skipped')
        skipflag = 1

    # judge 3: upper z and lower z: region 1
    elif mfz[0] > czmax + zmargin or mfz[row-1] < czmin - zmargin:
        print(FolderName + ' Region 1, skipped')
        skipflag = 1

    # judge 4: outside of a coil: region 2
    elif mfz[0] >= czmin - zmargin and mfz[row-1] <= czmax + zmargin and dist[0] >= coradius + rmargin:
        print(FolderName + ' Region 2, skipped')
        skipflag = 1

    # judge 5: inside of a coil, region 1 & 3
    elif abs(cx - abs(mfx[row-1])) < coradius*0.60 and abs(cy - abs(mfy[row-1])) < coradius*0.60: # 60 %, this is a fitting parameter
        print(FolderName + ' Region 1 & 3, inside of the coil, skipped')
        skipflag = 1

    else: # "s_... .wrl" is the remaining files to be used for clearance check
        src = wrl_path # source
        dest = WorkDir + '\s_'+ FolderName + '.wrl' # s: screened, dest: destination
        shutil.copy(src,dest)
        skipflag = 0

    return skipflag

###
# quick sort
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]   # pivot

    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
# Function to do Quick sort

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
