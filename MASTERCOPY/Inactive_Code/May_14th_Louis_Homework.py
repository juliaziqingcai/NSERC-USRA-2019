'''
This program is the 2nd idea to test for approximating
n thought of on May 14th, 2019 and explained to Louis by Michiel, then
explained to Julia who then attempted to code it.

This approximation of n takes the median of k samples of counters
and uses the 1st constant formula:

    n~ => median_counter * (1/2ln(2))

Also includes a test wrapper for 1 run of the algorithm.
'''

import math
import random

def algorithm(n, k):
    '''
    This function approximates n by using the median
    counter as the k in the final equation. We use the old
    constant calculated on May 1st (1/2ln(2)). Returns the
    approximated n.

    n = set size
    k = number of times to take a sample counter
    '''

    samples_array = list()

    for j in range((2*k)+1):

        random.seed()
        counter = 0
        arr = list()
        
        for i in range(n): # fill new array
            arr.append(0)
        
        while(True): # iterate
            index = random.randint(0, (n-1))
            if (arr[index] == 0):
                arr[index] = 1
                counter += 1
            else:
                break
        
        samples_array.append(counter)
    
    samples_array.sort()
    median_counter = samples_array[k]
    
    cons = 1 / (2 * math.log(2)) # set the c we found
    approximate_n = math.floor(cons * (median_counter ** 2))

    #TESTING CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("N                   : " + str(n))
    print("K                   : " + str(k))
    print("Median Counter      : " + str(median_counter))
    print("Approximated N      : " + str(approximate_n))
    print("\n")

    return approximate_n

def test_wrapper1():
    '''
    This test wrapper tests one run of the algorithm
    with continuously and with varying inputs as prompted
    to the user in the terminal.
    '''
    print("\n")
    n = int(input("N: "))
    k = int(input("K: "))
    algorithm(n, k)

    choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()
    while (choice_1 != 'N'):
        choice_2 = (input("Do you want to use the same values? (Y/N) ")).upper()
        if (choice_2 == 'N'):
            print("\n")
            n = int(input("N: "))
            k = int(input("K: "))
        algorithm(n, k)

        choice_1 = input("Do you want to run another trial? (Y/N) ")

test_wrapper1()