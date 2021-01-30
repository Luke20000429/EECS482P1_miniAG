import os
import sys
import random
import numpy as np

num_disk_in = int(sys.argv[1])
len_in = int(sys.argv[2])
output = ""

for file in range(num_disk_in):
    data = np.random.randint(1000, size=len_in)
    np.savetxt('testdisk.in%d'%file, data, fmt="%d", delimiter='\n')
    output = output + ('testdisk.in%d'%file) + ' '
    
print(output)