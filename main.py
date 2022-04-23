# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Last updated: April 22 2022

import time
import sys
sys.path.append('../python_codes/')
from comments import begin  # import function
from comments import end  # import function
from extraction import CoordinateCatch  # import function
from output import writetofile  # import function

start = time.time()

def main():
    begin()
    num1 = CoordinateCatch()[0]
    num2 = CoordinateCatch()[1]
    writetofile(num1, num2)
    end()

if __name__ == "__main__":
    main()

# time display
elapsed_time = time.time()-start
