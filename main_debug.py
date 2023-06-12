# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Update history
# Updated: June 07 2022 / August 02, 2022 / March 14, 2023 / June 12, 2023

# Memo:
# For debugging, only judgement routine is functional

######################################################################
# ReadFirst before running - presupposition:                         #
# Coil spring file needs to be located at the end of .wrl file group #
######################################################################

import time
import sys
import glob
import os
from comments import begin               # import function, called in the main
from comments import end                 # import function, called in the main
from sizescreen import screenfilesize    # import function, called in the main
from remove import RemoveDirectory       # import function, called in the main
from extraction import CoordinateCatch   # import function, called in the main
from output import writetofile           # import function, called in the main
from merge import FileMerge              # import function, called in the main
from coil import CoilCoordinate          # import function, called in the main
from calculation import JudgeCalculation # import function, called in the main
from rename import RenameToCoil          # import function, called in the main

def main():
    start = time.time()

    # specify your folder of .wrl files, this is referred in the external functions
    wrl_dir = 'C:\codes_NHK\CADScreening\example_cad_1'

    # judgement routine starts
    begin()

    # change the number to the maximum of .dat file
    counter = 65

    # judge which extracted .dat is the coil, rename the file
    coil_zmax = CoilCoordinate(wrl_dir, counter)[0]     # call function, coil
    coil_zmin = CoilCoordinate(wrl_dir, counter)[1]     # call function, coil
    coil_oradius = CoilCoordinate(wrl_dir, counter)[2]  # call function, coil
    coil_center_x = CoilCoordinate(wrl_dir, counter)[3] # call function, coil
    coil_center_y = CoilCoordinate(wrl_dir, counter)[4] # call function, coil

    counter_skip = 0
    # comparison and judgement
    for i in range(1, counter+1, 1):
        wrl_file = 'Part_' + str(i) + '.wrl'

        if i < counter:
            # calculation & judge
            sflag = JudgeCalculation(wrl_dir, wrl_file, coil_zmax, coil_zmin, coil_oradius, coil_center_x, coil_center_y) # call function, '\' symbol cannot be used in Visual Studio

            if sflag==1:
                counter_skip += 1
            else:
                counter_skip += 0
        elif i == counter:
            print('This is a coil, part number: ' + str(counter) + '. Renamed.')
            RenameToCoil(wrl_dir, i) # call function, rename

    print('Total ' + str(counter_skip) + ' parts were skipped.')

    # judgement routine ends
    end()

    # time display
    elapsed_time = time.time()-start
    print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")

if __name__ == "__main__":
    main()
