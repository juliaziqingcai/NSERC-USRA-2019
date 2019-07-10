'''
This program is a test wrapper for the Approximating_N_With_Average_Counter
program that includes a function that indicates whether
the approximated set size is within an acceptable interval.

This program runs the n~ average only version
of the Median_Counter_Vs_Average_Counter_Approximated_Ns
to test against in multiprocessing. It is shrunken down
for easier use and all unnecessary parts removed.

May 22nd, 2019
'''

import random
import math
import Approximating_N_With_Average_Counter
import datetime
import time

def average_counter_n_in_interval(n, k, epsilon):
    '''
    Returns a boolean indicating if the approximated set
    size using the average counter falls within the acceptable range.

    n = actual set size
    k = k samples to take
    epsilon = related to accepted interval
    '''
    n_average = Approximating_N_With_Average_Counter.algorithm(n, k)

    lower_bound = (1-epsilon) * n
    upper_bound = (1+epsilon) * n
    n_average_success = (lower_bound <= n_average) and (n_average <= upper_bound)


    return n_average_success



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

    total_n_average_success = 0

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    for i in range(test_num):
        if (average_counter_n_in_interval(n, k, epsilon)):
            total_n_average_success += 1

    pr_n_average_success = total_n_average_success / test_num

    print("\n")
    print("FINAL REPORT")
    print("------------------------------------------------")
    print("# of Tests               : " + str(test_num))
    print("N Value                  : " + str(n))
    print("K Value                  : " + str(k))
    print("Epsilon Value            : " + str(epsilon))
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

        total_n_average_success = 0

        now = datetime.datetime.now()
        start = time.time()
        print("\nDate and Time at program start: " + str(now))

        for i in range(test_num):
            if (average_counter_n_in_interval(n, k, epsilon)):
                total_n_average_success += 1

        pr_n_average_success = total_n_average_success / test_num
    
        print("\n")
        print("FINAL REPORT")
        print("------------------------------------------------")
        print("# of Tests               : " + str(test_num))
        print("N Value                  : " + str(n))
        print("K Value                  : " + str(k))
        print("Epsilon Value            : " + str(epsilon))
        print("Pr[N Average Success]    : " + str(pr_n_average_success))
        print("\n")
        
        now = datetime.datetime.now()
        end = time.time()
        print("Date and Time at program end: " + str(now))
        print("Program Execution Time      : " + str(end - start) + " seconds")
        
        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

# Tests
test_wrapper()