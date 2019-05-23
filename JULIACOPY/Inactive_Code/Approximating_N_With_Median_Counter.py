'''
This program is based off the May 1st, 2019 basic algorithm
discussed to approximate n through duplicate confirmation
sampling and the constant discovered (c = 1/2ln(2)) with
the median of 2k+1 sample counters.

It finds that approximately 50%, the approximated n
is within the middle n/2 of S.

It also includes a test function to look at algorithm efficiency.

@author Julia Cai, Alexa de Grandmont
version. 1.0.0
Last Revision: May 16th, 2019
'''

import random
import math
import Sampling_Until_Duplicate

def algorithm(n, k):
    '''
    This is the original version of the algorithm that returns
    an approximated n~ based on duplicate confirmation sampling.
    Returns the approximated n~.
    
    n is the set size
    '''

    counter_array = list()
    
    for i in range((2*k)+1):

        counter = Sampling_Until_Duplicate.algorithm(n)

        counter_array.append(counter)
    
    counter_array.sort()
    median_counter = counter_array[k]
    cons = 1 / (2* (math.log(2))) # set the c for median
    approximate_n = cons * (median_counter ** 2)
    
    
    '''TESTING ONLY CODE for one run
    print("The orignal set size is: " + str(n) + "\n")
    print("The counter is at: " + str(counter) + "\n")
    print("The approximated set size is: " + str(approx_n))
    
    error_bound = math.ceil(0.25 * n)
    #error bound is 0.25 as it is n/4 on either side of the median
    return ( (abs(n - approximate_n)) <= error_bound ) 
    '''
    return approximate_n
        
  
  
def test(test_num):
    '''
    This is the test function for the algorithm above.
    Prints a report to terminal.
    
    test_num = number of tests to run
    '''    
    success = 0
    for i in range(test_num):
        if (algorithm()):
            success += 1
    print("\n\n\n\n")
    print("\n_________________________________________________________\n\n")
    print("Set Size Used: " + str(n) +"\n")
    print("Total Trials:  " + str(test_num) + "\n")
    print("Successes:     " + str(success) + "\n")
    print("_________________________________________________________")
    
    
#test(1000)