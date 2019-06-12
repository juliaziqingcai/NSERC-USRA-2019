'''
BASED ON COMPLETE MISUNDERSTANDING OF MICHIEL'S PROMPT
AND INSTRUCTIONS DUE TO HIM USING THE SAME VARIABLE FOR
EVERYTHING


Approximates N based on new program discussed on
May 29th, 2019. 

New dual-layered version of ApproxN with
an application of Chernoff's Bound/Inequality.
Tests if k (# of times Sample Until Duplicate is run)
is smaller by applying Chernoff's Bound when epsilon
is very small. 
    
Theoretical upper error bound for the New K is:

    New K >= (12/pi) * (1/(epsilon^2)) * 12 * (log(1/delta))
    
Theoretical upper error bound for the New K is:

    Old K >= (3/pi)*((epsilon^2) * delta)
'''

import Binary_Search_Best_K
import time
import datetime
import math

def newApproxN(epsilon, delta, n, best_k):
    
    '''
    ORIGINAL VERSION (NO SPEED GAINS ANYWHERE AT ALL)

    New dual-layered version of ApproxN with
    an application of Chernoff's Bound/Inequality.
    Tests if k (# of times Sample Until Duplicate is run)
    is smaller by applying Chernoff's Bound when epsilon
    is very small. Prints a report to terminal. Returns the
    new approximated n.
    
    Theoretical upper error bound for the New K is:

        New K >= (12/pi) * (1/(epsilon^2)) * 12 * (log(1/delta))
    
    Theoretical upper error bound for the New K is:

        Old K >= (3/pi)*((epsilon^2) * delta)
    '''
    
    l = math.ceil(12 * (math.log((1/delta))))

    y_array = list()
    for i in range(l):
        y_array.append(Approximating_N_With_Average_Counter.get_average_counter(n, best_k))
    
    y_array.sort()
    median = y_array[(math.floor(l/2))]

    cons = 2 / math.pi # set the c for average
    approximate_n = cons * ((median - (2/3)) ** 2) #  Includes (-2/3) due to proof done on May 16. 2019

    return approximate_n


def compare_k(epsilon, delta, n, trials):
    
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))
    print("FUNCTION HAS STARTED")

    test_num = 700
    l = math.ceil(12 * (math.log((1/delta))))
    best_k = Binary_Search_Best_K.binary_search_best_k_original(epsilon, 1/4, test_num, n)
    result = list()

    successes = 0
    lower_bound = (1-epsilon) * n
    upper_bound = (1+epsilon) * n

    for i in range(trials):
        approximate_n = newApproxN(epsilon, delta, n, best_k)
        if((lower_bound <= approximate_n) and (approximate_n <= upper_bound)):
            successes += 1
    
    success_prob = successes/ trials

    print("\n\n\n")
    print("Epsilon             : " + str(epsilon))
    print("Delta               : " + str(delta))
    print("N                   : " + str(n))
    print("Best K Found        : " + str(best_k))
    print("New K               : " + str(l * best_k))
    print("Pr[Success]         : " + str(success_prob))
    print("\n")
    
    now = datetime.datetime.now()
    end = time.time()
    print("\nDate and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(math.floor(end - start)) + " seconds")


# TESTING


now = datetime.datetime.now()
start = time.time()
print("\nDate and Time at program start: " + str(now))
print("FILE HAS STARTED EXECUTION")
compare_k(0.1, 0.1, 100, 1)
