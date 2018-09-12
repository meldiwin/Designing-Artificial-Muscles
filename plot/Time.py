import os
from time import gmtime, strftime
import numpy as np
import sys
from math import *
from time import gmtime, strftime

total_time = 0
f = open('timess.txt', 'w')  
for dt in np.arange(0,2001,1):
        sys.stdout = f
        print dt
f.close()
        