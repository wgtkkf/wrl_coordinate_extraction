# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Last updatae: June 07 2022

#import numpy as np
import os
import time
import itertools
from sys import exit
start = time.time()

def CoordinateCatch(WorkDir, FileName): # WorkDir: .wrl file foler

    # parameter initialization
    counter_line = 1
    counter_bracket = 1
    counter_s = 0
    counter_e = 0

    #
    join_path = os.path.join(WorkDir, FileName)

    # open
    f0 = open(join_path, 'r') # read mode

    # lines
    s_lines = [line.strip() for line in f0]
    
    # scan from the file top to the end
    for line in s_lines:

        counter_line += 1
        counter_bracket += 1

        # if "point [" is found, extraction starts from next line of "point ["
        if "point [" in line:

            counter_s += 1 # fine name counter
            counter_line_temp = counter_line

        if "coordIndex [" in line:
            counter_e += 1
            counter_bracket_temp = counter_bracket

    if counter_s != counter_e:
        #print('The number of "point [" and "]" does not match, exit.')
        exit()
    #else:
        #print('The number of "point [" and "]" is matched.')

    f0.close()

    return counter_s, counter_e

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
