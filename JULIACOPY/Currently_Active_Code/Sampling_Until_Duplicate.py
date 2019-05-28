'''
Function to return the counter after
sampling until duplicate on a given set size.
Made into its own separate file so that calling
upon it will be easier and modularized.
'''

import math
import random

def algorithm(n, results):
    '''
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
    '''This function performs the confirmation
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
import timeit
'''
# Discovered that as n gets bigger, appending is slower by a lot.
print("\n")
print(timeit.repeat("for i in range(9999, 10000): algorithm(i)", "from __main__ import algorithm", repeat = 5, number = 100))
print("\n")
print(timeit.repeat("for i in range(9999, 10000): algorithm2(i)", "from __main__ import algorithm2", repeat =5,  number = 100))
'''