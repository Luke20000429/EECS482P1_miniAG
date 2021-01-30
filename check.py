import os
import sys
import random
import numpy as np
import re

max_disk_queue = int(sys.argv[1])
num_thread = int(sys.argv[2])
len_thread = int(sys.argv[3])

disk_queue = []
thread = np.zeros(num_thread) ## 0 idle, 1 busy, -1 inactive
thread_wl = np.zeros(num_thread)+len_thread  ## decrement to 0

last_track = 0

f = open('ans', 'r')

l = 0
for line in f:
    result = line.split(' ')
    
    if result[0] == 'requester':
        result[1] = int(result[1])
        result[3] = int(result[3])
        if thread[result[1]] == 1: 
            print("line %d, thread busy"%l)
            break
        if thread[result[1]] == -1: 
            print("line %d, thread has died"%l)
            break
        disk_queue.append(result[3])
        thread[result[1]] = 1
        thread_wl[result[1]] -= 1
        if thread_wl[result[1]] == 0:
            thread[result[1]] = -1

    elif result[0] == 'service':
        result[2] = int(result[2])
        result[4] = int(result[4])
        if len(disk_queue) < max_disk_queue:
            print("line %d, disk not full"%l)
            break
        if abs(result[4]-last_track) != abs(np.asarray(disk_queue)-last_track).min():
            print("line %d, not nearest track"%l)
            print(abs(np.asarray(disk_queue)-last_track).min()) 
            break
        last_track = result[4]
        disk_queue.remove(result[4])
        thread[result[2]] = 0

    l += 1


f.close()

print("Good Job")
