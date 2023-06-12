# Coded by Takuro TOKUNAGA
# Created: May 2 2022
# Last updatae: June 07 2022

import numpy as np
import time
import pandas as pd
import glob
import os
from sys import exit
start = time.time()

def FileMerge(WorkDir, FolderName):

    ### merge coordinates of a part ###
    # txt file merge

    join_path = os.path.join(WorkDir, FolderName.replace('.wrl', ''))
    txt_files = glob.glob(join_path + '\*.txt')
    output_path = os.path.join(WorkDir, FolderName.replace('.wrl', '.dat'))

    # show the txt files to be merged
    #with open(join_path + '\m' + str(FolderName.replace('.wrl', '')) +'.dat', 'w') as outfile:
    with open(output_path, 'w') as outfile:
        for txt_file in txt_files:

            # Open each file in read mode
            with open(txt_file) as infile:

                # read the data from file1 and
                outfile.write(infile.read())

            #outfile.write("\n") # generates vertical spaces between files

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
