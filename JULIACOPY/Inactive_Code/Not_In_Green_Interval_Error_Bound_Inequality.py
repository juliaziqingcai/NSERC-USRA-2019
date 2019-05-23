'''
This program is based off the inequality that the
probability that an approximated median (obtained through
taking the median of 2k+1 samples) is bounded by an upper
error bound as follows:

    Pr(m~ != acceptable) <= 2e^[(-4/3)*(delta^2)*k]

It includes a test function to see if the inequality holds.
'''

import math
import random


def get_approximate_median(n,k):
    '''Calculates approximate median by taking 2k+1 samples and returns the
    median of these samples. Returns the approximated median.
    
    n = set size
    k = related to the 2k+1 samples to take
    '''
    random.seed()
    samples = list()
    
    for i in range((2*k)+1): # iterate
        index = random.randint(0, (n-1))
        samples.append(index)
    
    samples.sort()
    
    return samples[k]


def in_green_interval(n, delta, k):
    ''' Tests if the approximated median is within the green (acceptable)
    interval. Returns a boolean indicating this status. Also prints a report
    for each run.
    
    n = set size
    delta = margin of error
    k = related to 2k+1 samples to take
    '''
    approximate_median = get_approximate_median(n, k)
    real_median = math.floor(n/2)
    
    in_green = abs(((2 * approximate_median) / n) - 1) <= delta
    
    '''TEST ONLY CODE FOR ONE RUN OF ALGORITHM
    print("_______________________________________________")
    print("N                       : " + str(n))
    print("Delta                   : " + str(delta))
    print("K                       : " + str(k))
    print("Real Median             : " + str(real_median))
    print("M~                      : " + str(approximate_median))
    print("Within Green?           : " + str(in_green))
    '''
    
    return in_green
    
    
def test(test_num, n, delta, k):
    ''' This is the test function for the overall program and inequality.
    Tests if the probability that the approximated median falls outside of 
    the green interval is upper bounded by the following figure:
    
                2(e**((-4/3)*(delta**2)*k))
                
    Also prints a report about this to terminal.
    
    test_num = # of tests to run the algorithm
    n = set size
    delta = margin of error
    k = related to 2k+1 samples to take
    '''
    exponent = (-4/3) * (delta**2) * k
    error_bound = 2 * math.exp(exponent)
    fail = 0
    for i in range(test_num):
        if not(in_green_interval(n, delta, k)):
            fail += 1
    probability = fail / test_num
    print("\n\n\n")
    print("_______________________________________________")
    print("***************FINAL REPORT********************")
    print("N                       : " + str(n))
    print("Delta                   : " + str(delta))
    print("K                       : " + str(k))
    print("# Trials                : " + str(test_num))
    print("Failures                : " + str(fail))
    print("Pr[not green]           : " + str(probability))
    print("Error Bound             : " + str(error_bound))
    print("Inequality Holds?       : " + str(probability <= error_bound))
    print("\n\n\n")


        
# Tests

#test(test_num, n, delta, k)
#test(1000, 100000, 0.1, 100)

