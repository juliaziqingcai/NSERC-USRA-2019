'''
Multiprocessing attempt version of Approximating_N_With_Average_Counter
program. Turns out this is slower than the original. This lead to the
realization that Python's multiprocessing module classes have a
blocking issue, where they wait for something to terminate before
starting the next thing. Apparently this is the Global Interpreter Lock (GIL).

Lesson learned.

May 22nd, 2019
'''


import math
import random
import Sampling_Until_Duplicate
import multiprocessing as mp
from multiprocessing import Pool
import curses



counter_sum = 0

def counter_sum_reset():
    global counter_sum
    counter_sum = 0

def add_to_counter_sum(current_counter):
    global counter_sum 
    counter_sum += current_counter

def algorithm(n, k):
    #counter_sum = 0
    pool = mp.Pool()
    for i in range(k):
        pool.apply_async(Sampling_Until_Duplicate.algorithm, args=(n,),\
             callback = add_to_counter_sum)
    pool.close()
    pool.join()
    
    average_counter = counter_sum / (k) # taken due to Law of Large Numbers
    
    cons = 2 / math.pi # set the c for average
    approximate_n = cons * ((average_counter - (2/3)) ** 2) 
    # Includes (-2/3) due to proof done on May 16. 2019
    #print("\nApproximated N: " + str(approximate_n) + "\n")
    return approximate_n

#if __name__=='__main__':
    #algorithm(1000, 150)
    #algorithm(n, k)
    #counter_sum_reset()