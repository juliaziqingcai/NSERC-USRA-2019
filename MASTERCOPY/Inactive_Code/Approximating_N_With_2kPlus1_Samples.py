'''
This program is based off the algorithm discussed
May 1st, 2019 to approximate n~ through returning the
median of 2k+1 samples of the duplicate confirmation
sampling.

Uses the Approximating_N algorithm and imports it.
It also includes a test for algorithm efficiency.
'''

import random
import math
import Approximating_N_With_Median_Counter #imported for 2k+1 samples median
    

def algorithm(n, k):
    '''
    This is the algorithm to approximate n~ by taking the
    median of 2k+1 approximated n~ samples from the Approximating_N

    
    n is the set size
    k is the sample variable to use
    '''
    approximation_array = list()
    for i in range((2* k)+ 1):
        approximation_array.append(Approximating_N_With_Median_Counter.algorithm(n, k))
    approximation_array.sort()
    approximate_n = approximation_array[k]

    '''TESTING ONLY CODE for one run
    error_bound = math.floor(0.25 * n)
    #error bound is 0.25 as it is n/4 on either side of the median
    equal = (abs(n - approximate_n)) <= error_bound
    print("\n_________________________________________________________")
    print("Sample k used:          " + str(k))
    print("Actual Set Size:        " + str(n))
    print("Approximated Set Size:  " + str(approximate_n)) 
    print("Within error bound?   : " + str(equal))
    print("_________________________________________________________")
    #return equal 
    '''

    return approximate_n
    
def test(test_num, n, k):
    '''
    This is the test function for the algorithm above.
    Prints a report to terminal.

    test_num = # of tests to run
    n = set size
    k = related to 2k+1 sample approximated n~ to take
    '''
    success = 0
    for i in range(test_num):
        if(algorithm(n, k)):
            success += 1
    print("\n_________________________________________________________")
    print("Set Size Used:          " + str(n))
    print("Sample k used:          " + str(k))
    print("Total Trials:           " + str(test_num))
    print("Successes:              " + str(success))
    print("_________________________________________________________")
        
        
#test( 100, 1000, 100)
        
