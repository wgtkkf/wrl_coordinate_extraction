# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Last modified: April 22 2022

#import numpy as np
import time
import itertools
from sys import exit
start = time.time()

def CoordinateCatch():

    # parameter initialization
    counter_line = 1
    counter_bracket = 1
    counter_s = 0
    counter_e = 0

    # open
    f0 = open('example_general/Part_9.wrl', 'r') # read mode

    # lines
    s_lines = [line.strip() for line in f0]

    # scan from the file top to the end
    for line in s_lines:

        counter_line += 1
        counter_bracket += 1

        # if "point [" is found, extraction starts from next line of "point ["
        if "point [" in line:
            #print(line)

            counter_s += 1 # fine name counter
            counter_line_temp = counter_line
            #print(str(counter_line_temp))

        if "coordIndex [" in line:
            counter_e += 1
            counter_bracket_temp = counter_bracket
            #print(str(counter_bracket_temp))

    if counter_s != counter_e:
        print('The number of "point [" and "]" does not match, exit.')
        exit()
    #else:
        #print('The number of "point [" and "]" is matched.')

    f0.close()

    return counter_s, counter_e

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
