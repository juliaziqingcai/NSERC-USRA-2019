'''
This program is meant to find a k value lower than the
bounded value suggested by the mathematical proof:

1 < k < (3/pi)*((epsilon^2) * delta)

by using Binary Search on varying values of epsilon
and delta to see test results.

There includes 2 commented out sections:
    -A series of overnight tests that were performed
    -A work area for implementing subprocess integration

'''

import math
import random
import Approximating_N_With_Average_Counter
import Sampling_Until_Duplicate
import datetime
import time
import statistics
import sys


def in_interval_original(c, mu, epsilon):
    '''
    ORIGINAL VERSION (NO SPEED GAINS)

    Tests to see if the counter is within the acceptable
    interval. Returns a boolean indicating success/failure.

    n = actual set size
    k = samples to take (2k+1)
    epsilon = [(1-epsilon)n, (1+epsilon)n] acceptable range for the
                approximated mu
    '''

    lower_bound = (1-epsilon) * mu
    upper_bound = (1+epsilon) * mu

    c_success = (lower_bound <= c) and (c <= upper_bound)

    return c_success


def binary_search_best_k_original(epsilon, delta, test_num, n):
    '''
    ORIGINAL VERSION (NO SPEED GAINS)

    Takes in an epsilon and delta value to test to find a value
    for k within 1 <= k <= (3/pi)*(1/(epislon^2 * delta)) using binary
    search. Returns the best k, by returning the lower boundary when
    the search stops.
    '''
    low = 1
    initial_high = (3/math.pi) * (1/ ((epsilon ** 2) * delta))
    high = initial_high
    mu = math.sqrt(((math.pi * n) / 2 )) + (2 / 3)
    '''
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))
    '''

    while (high > low+1): # +1 is ok because it is strictly greater, and not '>=', which requires +2 to prevent infinite loop
        middle = math.floor((low + high) / 2)
        success_total = 0
        for i in range(test_num): # test_num = total number times we run RSUD to count number of successes
            c = Sampling_Until_Duplicate.RSUD(n, middle)
            if (in_interval_original(c, mu, epsilon)):
                success_total += 1
        pr_success = success_total / test_num
        if (pr_success >= (1-delta)):
            high = middle
        else:
            low = middle
    
    '''
    print("\n------------------------")
    print("N:           : " + str(n))
    print("# of Tests   : " + str(test_num))
    print("Epsilon      : " + str(epsilon))
    print("Delta        : " + str(delta))
    print("Mu           : " + str(mu))
    print("Best K Found : " + str(low))
    print("Initial High : " + str(initial_high))

    
    now = datetime.datetime.now()
    end = time.time()
    print("\nDate and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(math.floor(end - start)) + " seconds")
    '''
    return low


def output_results_original(epsilon, delta, test_num, n, filename, trials):
    '''
    ORIGINAL

    Allows for results to be written to a LibreOffice datasheet for
    easier transcription and manipulation, instead of manually
    copying results. Also outputs a summary of results. Due to the
    extra file writing, please put in an integer for trials >= 2

    epsilon = related to the accepted interval
    delta = related to the confidence interval
    test_num = number of tests to conduct, > 2
    n = actual set size
    filename = string that represents the file name
    trials = number of trials to run for each set of values
    '''
    file = open( filename + '.ods', 'a') #appends, so we don't overwrite

    now = datetime.datetime.now()
    start = time.time()
    file.write("\n")
    file.write("\nDate and Time at program start: " + str(now))
    
    result_array = list()

    file.write("\nEPSILON IS NOW " + str(epsilon) + "\n") 
       
    for i in range(trials):
        result = binary_search_best_k_original(epsilon, delta, test_num, n)
        result_array.append(result)
        line = str(result) + "\n"
        file.write(line)
    
    now = datetime.datetime.now()
    end = time.time()
    total_time = math.floor(end - start)

    # CODE FOR COMPARING FOUND K AND THEORETICAL K AND MU
    initial_high = (3/math.pi) * (1/ ((epsilon ** 2) * delta))
    mu = math.sqrt(((math.pi * n) / 2 )) + (2 / 3)

    file.write("\nDate and Time at program end: " + str(now))
    file.write("\nProgram Execution Time      : " + str(total_time) + " seconds")
    file.write("\n\n Summary of Results\n")
    file.write("\nTotal Time Taken:\n")
    file.write(str(total_time) + " s\n")
    file.write("~" + str((total_time / 3600)) + " hours\n")
    file.write(str((total_time / trials)) + "s/trials\n")
    file.write("\nVariance: \n")
    file.write(str(statistics.pvariance(result_array)))
    file.write("\nAverage K Found:\n")
    file.write(str(statistics.mean(result_array)))
    file.write("\nInitial High:\n")
    file.write(str(initial_high))
    file.write("\nMu:\n")
    file.write(str(mu))



#------------------ TESTING SECTION BEGINS (epsilon, delta, test_num, n)---------------------------------------------------------------------------------
#binary_search_best_k(0.1, 0.2, 700, 5000)


# May 21st OVERNIGHT TESTS: This will test test_num from 400-1000
''' MAY 21st Overnight Tests
# Based on these tests, 100 tests ~ 100 seconds (maybe extra 6s)
for test_num in range(400, 1100, 100):
    for j in range(10):
        binary_search_best_k(0.1, 0.1, test_num, 1000)'''

# May 22nd OVERNIGHT TESTS
# This will test different set sizes (n)
# Test out n = 100, 500, 2000
# Time for one run: 
'''
print("--------N = 100 STARTS------------")
for j in range(35): # ~415 seconds/each, round tp 500
    binary_search_best_k(0.1, 0.2, 700,100)
print("\n--------N = 500 STARTS------------")
for k in range(35): # ~479 seconds/each, round to 500
    binary_search_best_k(0.1, 0.2, 700,500)
print("\n--------N = 2000 STARTS------------")
for l in range(35): # ~ 737 seconds/each, round to 800
    binary_search_best_k(0.1, 0.2, 700, 2000)
'''

'''
# May 23rd OVERNIGHT TESTS
# This will test increasingly larger values of N to see if the best k found
# really tends towards a square root function
# Will test out n = 3k, 4k, 5k
output_results_original(0.1, 0.2, 700, 3000, 'May23_out', 40)
output_results_original(0.1, 0.2, 700, 4000, 'May23_out', 40)
output_results_original(0.1, 0.2, 700, 5000, 'May23_out', 40)
'''

'''
# May 24th WEEKEND TESTS
output_results_original(0.2, 0.2, 700, 100, 'Weekend_out', 90)
output_results_original(0.2, 0.2, 700, 500, 'Weekend_out', 90)
output_results_original(0.2, 0.2, 700, 1000, 'Weekend_out', 90)
output_results_original(0.2, 0.2, 700, 2000, 'Weekend_out', 90)
output_results_original(0.2, 0.2, 700, 3000, 'Weekend_out', 90)
output_results_original(0.2, 0.2, 700, 4000, 'Weekend_out', 90)
output_results_original(0.2, 0.2, 700, 5000, 'Weekend_out', 90)
'''

'''
# May 27th OVERNIGHT TESTS
output_results_original(0.2, 0.1, 700, 100, 'May27th_out', 85)
output_results_original(0.2, 0.1, 700, 500, 'May27th_out', 85)
output_results_original(0.2, 0.1, 700, 1000, 'May27th_out', 85)
output_results_original(0.2, 0.1, 700, 2000, 'May27th_out', 85)
output_results_original(0.2, 0.1, 700, 3000, 'May27th_out', 85)
output_results_original(0.2, 0.1, 700, 4000, 'May27th_out', 85)
output_results_original(0.2, 0.1, 700, 5000, 'May27th_out', 85)
'''

'''
# May 28th OVERNIGHT TESTS
output_results_original(0.1, 0.1, 700, 100, 'May28th_out', 22)
output_results_original(0.1, 0.1, 700, 500, 'May28th_out', 22)
output_results_original(0.1, 0.1, 700, 1000, 'May28th_out', 22)
output_results_original(0.1, 0.1, 700, 2000, 'May28th_out', 22)
output_results_original(0.1, 0.1, 700, 3000, 'May28th_out', 22)
output_results_original(0.1, 0.1, 700, 4000, 'May28th_out', 22)
output_results_original(0.1, 0.1, 700, 5000, 'May28th_out', 22)
'''

'''
# June 5th OVERNIGHT TESTS
output_results_original(0.01, 0.25, 500, 1000, 'June5th_out', 7)
'''

'''
# June 6th OVERNIGHT TESTS
output_results_original(0.02, 0.25, 500, 1000, 'June6th_out', 21)
output_results_original(0.03, 0.25, 500, 1000, 'June6th_out', 21)
output_results_original(0.04, 0.25, 500, 1000, 'June6th_out', 21)
'''


# June 7th WEEKEND OVERNIGHT TESTS

#output_results_original(0.01, 0.25, 500, 1000, 'June7th_out', 26)
'''
i = 0.14
for j in range(7):
    #print("\n" + str(i))
    output_results_original(i, 0.25, 500, 1000, 'June10th_out', 26)
    i += 0.01
    i = float('%.2f'%(i))
'''


#----------------------SECTION FOR WORKING ON IMPLEMENTING SUBPROCESS---------------------------------------------------
# Tests to determine runtime and therefore how many trials to fit in overnight
#output_results_original(0.1, 0.1, 700, 100, 'time_test', 5)
#binary_search_best_k_original(0.2, 0.25, 500, 1000)

#output_results_original_original(0.1, 0.25, 700, 1000, 'test', 5)

# Area to launch subprocesses(main stuff attempt I guess)

#def main():
    
    '''
# TESTING REGULAR COMMAND LINE ARGUMENT INPUT AND RESULT WRITING TO FILE
    epsilon = float(sys.argv[1]) # Command line auto-casts args to strings
    delta = float(sys.argv[2])
    test_num = int(sys.argv[3])
    n = int(sys.argv[4])
    filename = sys.argv[5]
    trials = int(sys.argv[6])

    output_results_original(epsilon, delta, test_num, n, filename, trials)
    '''
'''
# TO DO: TEST MULTIPLE EPSILON-DELTA AND SUBPROCESS LAUNCHES WITH CPU USAGE
    #num_args = len(sys.argv)
    process = subprocess.run(['python3', Binary_Search_Best_K.binary_search_best_k_original], check=True, stdout=subprocess.PIPE, universal_newlines=True)


if __name__=='__main__':
    main()
    '''