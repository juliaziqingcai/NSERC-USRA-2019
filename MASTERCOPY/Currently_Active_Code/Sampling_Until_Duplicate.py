'''
Function to return the counter after
sampling until duplicate on a given set size.
Made into its own separate file so that calling
upon it will be easier and modularized.

@author Julia Cai
version 1.0.0
Last Revision May 16th, 2019
'''


import math
import random


def algorithm(n):
    '''
    This function performs the confirmation
    sampling until duplicate algorithm over
    a give set size of n. Returns the current
    counter as soon as it encounters a duplicate.

    n = set size
    '''
    
    random.seed()
    counter = 0
    arr = list()
        
    for j in range(n): # fill new array
        arr.append(0)
        
    while(True): # iterate
        index = random.randint(0, (n-1))
        counter += 1
        if (arr[index] == 0):
            arr[index] = 1
        else:
            break # break when duplicate found
    
    return counter