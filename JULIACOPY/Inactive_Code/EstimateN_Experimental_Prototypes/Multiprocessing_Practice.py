import multiprocessing as mp
import numpy as np
import time
import datetime
import os
from multiprocessing import Process
import Sampling_Until_Duplicate

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
        Sampling_Until_Duplicate.algorithm(10)
    print("First Loop Done")

    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Loop Execution Time      : " + str(end - start) + " seconds")

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    for j in range(500):
        p1 = Process(target = Sampling_Until_Duplicate.algorithm, args=(10, ))
        p2 = Process(target = Sampling_Until_Duplicate.algorithm, args=(10, ))
        p3 = Process(target = Sampling_Until_Duplicate.algorithm, args=(10, ))
        p4 = Process(target = Sampling_Until_Duplicate.algorithm, args=(10, ))
        p1.start(), p2.start(), p3.start(), p4.start()
        #p.join()
    print("Second Loop Done")
    
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Loop Execution Time      : " + str(end - start) + " seconds")
    #print(procs)