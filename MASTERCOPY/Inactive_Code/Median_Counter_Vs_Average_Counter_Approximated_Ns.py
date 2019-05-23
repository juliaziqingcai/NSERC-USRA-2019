'''
This program compares how the approximations
for n compare when using the median of the counters
vs using the average of the counters. Essentially
compares the precision/success of the following
two files:

    Approximating_N_With_Median_Counter.py
    Approximating_N_With_Average_Counter.py

Based off the May 15th, 2019 realization that we were
using two different concepts that each had a
corresponding constant to use for approximating n.

    For median counter  => use c = 1/2ln(2)
    For average counter => use c = 2/pi

@author Julia Cai, Alexa de Grandmont
version. 1.0.0
Last Revision: May 16th, 2019
'''

import random
import math
import Approximating_N_With_Median_Counter
import Approximating_N_With_Average_Counter
import datetime
import time

def median_vs_average_counter(n, k, epsilon):
    '''
    This function is one run comparing the approximated set
    sizes using the median counter vs using the average counter.
    Prints a report to terminal and returns a list of Boolean
    values indicating the success of both approximations.

    n = set size
    k = related to samples taken in both algorithms
    epsilon = related to accepted interval for the approximated n   
    '''

    n_median = Approximating_N_With_Median_Counter.algorithm(n, k)
    n_average = Approximating_N_With_Average_Counter.algorithm(n, k)

    lower_bound = (1-epsilon) * n
    upper_bound = (1+epsilon) * n
    n_median_success = (lower_bound <= n_median) and (n_median <= upper_bound)
    n_average_success = (lower_bound <= n_average) and (n_average <= upper_bound)

    '''# TESTING ONLY CODE FOR ONE RUN OF THE ALGORITHM
    print("\n")
    print("------------------------------------------------")
    print("N Value                  : " + str(n))
    print("K Value                  : " + str(k))
    print("Epsilon Value            : " + str(epsilon))
    print("N Median                 : " + str(n_median) + "    Success: " + str(n_median_success))
    print("N Average                : " + str(n_average) + "    Success: " + str(n_average_success))
    print("\n")'''
    
    successes = [n_median_success, n_average_success]
    return successes

# Tests
#median_vs_average_counter(100, 100, 0.25)


def test_wrapper():
    '''
    This is the test wrapper that allows for continuous
    and repeated testing of the overall program by
    prompting the user for input values in the terminal.
    Prints a final report to terminal.
    '''

    print("\n")
    test_num = int(input("How many tests would you like to run? "))
    n = int(input("N value: "))
    k = int(input("K value: "))
    epsilon = float(input("Epsilon value: "))

    total_n_median_success = 0
    total_n_average_success = 0

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    for i in range(test_num):
        
        successes = median_vs_average_counter(n, k, epsilon)
        #if (successes[0]):
         #   total_n_median_success += 1

        if (successes[1]):
            total_n_average_success += 1

    #pr_n_median_success = total_n_median_success / test_num
    pr_n_average_success = total_n_average_success / test_num

    print("\n")
    print("FINAL REPORT")
    print("------------------------------------------------")
    print("# of Tests               : " + str(test_num))
    print("N Value                  : " + str(n))
    print("K Value                  : " + str(k))
    print("Epsilon Value            : " + str(epsilon))
    print("Pr[N Median Success]     : " + str(pr_n_median_success))
    print("Pr[N Average Success]    : " + str(pr_n_average_success))
    print("\n")
    
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")
    
    choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

    while(choice_1 != 'N'):

        print("\n")
        test_num = int(input("How many tests do you want to run? "))
        choice_2 = (input("Do you want to use the same values? (Y/N) ")).upper()

        if (choice_2 != 'Y'):
            n = int(input("N value: "))
            k = int(input("K value: "))
            epsilon = float(input("Epsilon value: "))

        total_n_median_success = 0
        total_n_average_success = 0

        now = datetime.datetime.now()
        start = time.time()
        print("\nDate and Time at program start: " + str(now))

        for i in range(test_num):
            successes = median_vs_average_counter(n, k, epsilon)
            if (successes[0]):
                total_n_median_success += 1
            if (successes[1]):
                total_n_average_success += 1
    
        pr_n_median_success = total_n_median_success / test_num
        pr_n_average_success = total_n_average_success / test_num
    
        print("\n")
        print("FINAL REPORT")
        print("------------------------------------------------")
        print("# of Tests               : " + str(test_num))
        print("N Value                  : " + str(n))
        print("K Value                  : " + str(k))
        print("Epsilon Value            : " + str(epsilon))
        print("Pr[N Median Success]     : " + str(pr_n_median_success))
        print("Pr[N Average Success]    : " + str(pr_n_average_success))
        print("\n")
        
        now = datetime.datetime.now()
        end = time.time()
        print("Date and Time at program end: " + str(now))
        print("Program Execution Time      : " + str(end - start) + " seconds")
        
        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

# Tests
#test_wrapper()