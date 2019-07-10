'''
Function to return the counter after
sampling until duplicate on a given set size.
Made into its own separate file so that calling
upon it will be easier and modularized.

Includes multiple versions for different implementations
and attempts to optimize. 
'''

import math
import random
import timeit

def algorithm(n, results):
    '''
    MULTI-THREADED VERSION

    This function performs the confirmation
    sampling until duplicate algorithm over
    a give set size of n. Returns the current
    counter as soon as it encounters a duplicate.

    n = set size
    '''
    
    random.seed()
    counter = 0
    arr = [0] * n #Initialize array this way to be faster we hope

    '''arr = list()
        
    for j in range(n): # fill new array
        arr.append(0)'''
        
    while(True): # iterate
        index = random.randint(0, (n-1))
        counter += 1
        if (arr[index] == 0):
            arr[index] = 1
        else:
            break # break when duplicate found
    results.append(counter)
    #print("\nCounter is: " + str(counter))
    return counter


def algorithm2(n):
    '''
    APPEND VERSION (NO MULTI-THREADING)

    This function performs the confirmation
    sampling until duplicate algorithm over
    a give set size of n. Returns the current
    counter as soon as it encounters a duplicate.
    This version appends a bunch of zeroes to a list
    to create the array to iterate over. It is much slower
    than the multiplicative version we have running above.

    n = set size
    '''
    random.seed()
    counter = 0
    #arr = [0] * n #Initialize array this way to be faster we hope
    
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



# TIME TESTS
'''
# Discovered that as n gets bigger, appending is slower by a lot.
print("\n")
print(timeit.repeat("for i in range(9999, 10000): algorithm(i)", "from __main__ import algorithm", repeat = 5, number = 100))
print("\n")
print(timeit.repeat("for i in range(9999, 10000): algorithm2(i)", "from __main__ import algorithm2", repeat =5,  number = 100))
'''

def algorithm_original(n):
    '''
    ORIGINAL VERSION (NO SPEED UPGRADES)

    This function performs the confirmation
    sampling until duplicate algorithm over
    a give set size of n. Returns the current
    counter as soon as it encounters a duplicate.

    n = set size
    '''
    
    random.seed()
    counter = 0
    arr = [0] * n #Initialize array this way to be faster we hope
    '''arr = list()
        
    for j in range(n): # fill new array
        arr.append(0)'''
        
    while(True): # iterate
        index = random.randint(0, (n-1))
        counter += 1
        if (arr[index] == 0):
            #changed_pos.append(index)
            arr[index] = 1
        else:
            break # break when duplicate found
    #results.append(counter)
    #print("\nCounter is: " + str(counter))
    return counter

def algorithm_with_global_array(n, global_array):
    '''
    GLOBAL ARRAY SPEED GAINS

    This function performs the confirmation
    sampling until duplicate algorithm over
    a give set size of n. Returns the current
    counter as soon as it encounters a duplicate.

    n = set size
    '''
    
    random.seed()
    counter = 0
    changed_pos = list()
    #arr = [0] * n #Initialize array this way to be faster we hope
    '''arr = list()
        
    for j in range(n): # fill new array
        arr.append(0)'''
        
    while(True): # iterate
        index = random.randint(0, (n-1))
        counter += 1
        if (global_array[index] == 0):
            changed_pos.append(index)
            global_array[index] = 1
        else:
            break # break when duplicate found
    #results.append(counter)
    #print("\nCounter is: " + str(counter))
    for i in changed_pos:
        global_array[i] = 0
    return counter


def RSUD_original(n, k):
    '''
    RETURNS AVERAGE COUNTER (ORIGINAL VERSION)

    Runs the Sample_Until_Duplicate algorithm
    k times and returns the average counter, which is basically
    an approximation of mu.

    n = set size
    k = number of samples to take
    '''

    counter_sum = 0

    for i in range(k):
        #changed_pos = list()
        counter_sum += algorithm_original(n)#, changed_pos)

    average_counter = counter_sum / k # taken due to Law of Large Numbers
    
    return average_counter


def RSUD_with_global_array(n, k, global_array):
    '''
    GLOBAL ARRAY SPEED GAINS (QUICKETS OVERALL)

    Runs the Sample_Until_Duplicate algorithm
    k times and returns the average counter, which is basically
    an approximation of mu.

    n = set size
    k = number of samples to take
    '''

    counter_sum = 0

    for i in range(k):
        counter_sum += algorithm_with_global_array(n, global_array)

    average_counter = counter_sum / k # taken due to Law of Large Numbers
    
    return average_counter


