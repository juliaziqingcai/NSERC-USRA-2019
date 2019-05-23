'''
This program tests using a simple number doubling 
function as a series of multiple Processes in an attempt
to better understand how one might use the multiprocessing
module in Python. 

Processes are very fast (compared to the
Pool class), but they seem to run into crashing issues when
too many of them are started at once. This is a class
feature, as Process throws everything at the CPU
regardless of whether it can handle it or not, whereas
Pool chunks up tasks and distributes so as to prevent
crashing and resource infighting.

Process is faster, and better for simple tasks.
Pool is slower, but better for larger tasks.
They both seem to be slower than just implementing
code normally due to blocking issues.

May 22nd, 2019
'''

import multiprocessing as mp
import numpy as np
import time
import datetime
import os
from multiprocessing import Process
 

def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))
 
if __name__ == '__main__':

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    #numbers = [5, 10, 15, 20, 25]
    procs = []
 
    #for index, number in enumerate(numbers):
    for i in range(500):
        proc = Process(target=doubler, args=(i,))
        procs.append(proc)
        proc.start()
 
    for proc in procs:
        proc.join()
    
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")
    #print(procs)






'''

now = datetime.datetime.now()
start = time.time()
print("\nDate and Time at program start: " + str(now))



now = datetime.datetime.now()
end = time.time()
print("Date and Time at program end: " + str(now))
print("Program Execution Time      : " + str(end - start) + " seconds")
'''