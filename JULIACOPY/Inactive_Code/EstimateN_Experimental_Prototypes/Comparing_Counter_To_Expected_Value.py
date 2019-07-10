'''
This program is based off the simplified proof
for the expected value of the counter (#test_num) done
using the Birthday Problem from May 8th, 2019. It allows
the user to compare the actual counter value and the
expected value of the counter in the algorithm for
approximating n~ through duplicate confirmation sampling.

It also includes a test function to allow for comparison.
'''

import random
import math

def compare_counter(counter, n):
    '''
    This function allows us to compare the expected value of the counter, based
    on the calculations done with an integral and coming to the conclusion
    that based on n, E[counter] = sqrt(pi/2) * sqrt(n). Based off simplified
    proof done on May 8th, 2019. Prints out a report
    
    counter = actual algorithm counter value
    n = the set size
    '''
    expected_value = math.floor((math.sqrt(math.pi/2)) * (math.sqrt(n)))
    print("N is:               " + str(n))
    print("Expected Value is:  " + str(expected_value))
    print("Counter is:         " + str(counter))
    print("Within error bound? " + \
          str((abs(counter - expected_value)) <= (0.25 * counter)))
    

def algorithm(n):
    '''
    This is a slightly modified version of the basic algorithm
    that approximates n~ through duplicate confirmation sampling.
    The addition is the embedding of the compare_counter function
    that allows the user to compare the actual counter and the
    expected value during each iteration. 
    
    n is the set size
    '''
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
        
    compare_counter(counter, n)

    '''TESTING ONLY CODE for test()
    cons = 1 / (2 * (math.log(2))) # set the c we found
    approximate_n = math.floor(cons * (counter ** 2))
    
    print("The orignal set size is: " + str(n))
    print("The counter is at: " + str(counter))
    print("The approximated set size is: " + str(approximate_n))
    
    error_bound = math.ceil(0.25 * n)
    #error bound is 0.25 as it is n/4 on either side of the median
    return ( (abs(n - approximate_n)) <= error_bound )
    '''
        
  
def test(test_num, n):
    '''
    This is the test function for the overall program.
    Prints a report to terminal
    
    test_num = number of tests to run
    n = set size
    '''    
    success = 0
    for i in range(test_num):
        if (algorithm(n)):
            success += 1
    print("\n\n\n\n")
    print("\n_________________________________________________________\n\n")
    print("Set Size Used: " + str(n) +"\n")
    print("Total Trials:  " + str(test_num) + "\n")
    print("Successes:     " + str(success) + "\n")
    print("_________________________________________________________")
    

#test(1000, 1000)
#algorithm(10000)