# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Last update: June 07 2022

import numpy as np
import os
import time
import itertools
from sys import exit
start = time.time()

def writetofile(args, arge, WorkDir, FileName): # args=arge

    if args != arge:
        #print('The number of "point [" and "]" does not match, exit.')
        exit()
    #else:
        #print('The number of "point [" and "]" is matched.')

    start_line = np.zeros(args,dtype=np.int64)
    end_line = np.zeros(arge,dtype=np.int64)

    counter1 = 0
    counter2 = 0
    line_counter = 1

    #
    join_path = os.path.join(WorkDir, FileName)

    # file open
    f0 = open(join_path, 'r') # read mode

    # lines
    s_lines = [line.strip() for line in f0]

    # scan from the file top to the end
    for line in s_lines:
        line_counter += 1

        if "point [" in line:
            temp1 = line_counter
            start_line[counter1] = temp1
            counter1 += 1

        if "coordIndex [" in line:
            temp2 = line_counter
            end_line[counter2] = temp2
            counter2 += 1

    # 2nd run, reset counter
    line_counter = 1

    # make directory
    join_directory = os.path.join(WorkDir, FileName.replace('.wrl', ''))
    os.mkdir(join_directory)

    for i in range(0,args):

        f1 =  open(join_directory + "\coordinate_" + str(i) + ".txt", 'w')  # write mode

        for line in s_lines:
            line_counter += 1
            if line_counter > start_line[i] and line_counter < end_line[i]-2:
                line = line.replace(',', '')
                line = line.replace('    ', ' ')
                line = line.replace('  ', ' ')
                line = line.replace('  ', ' ')
                f1.write(line)
                f1.write('\n')

        f1.close()

        # reset counter
        line_counter = 1

    f0.close()

    return 0

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
