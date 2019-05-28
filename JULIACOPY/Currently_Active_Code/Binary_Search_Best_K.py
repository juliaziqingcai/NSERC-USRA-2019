'''
This program is meant to find a k value lower than the
bounded value suggested by the mathematical proof:

1 < k < (3/pi)*((epsilon^2) * delta)

by using Binary Search on varying values of epsilon
and delta to see test results.

'''



import math
import random
import Approximating_N_With_Average_Counter
import datetime
import time
import statistics


def in_interval(n, k, epsilon):
    '''
    Tests to see if the approximated n is within the acceptable
    interval. Returns a boolean indicating success/failure.

    n = actual set size
    k = samples to take (2k+1)
    epsilon = [(1-epsilon)n, (1+epsilon)n] acceptable range for the
                approximated n
    '''

    n_average = Approximating_N_With_Average_Counter.algorithm(n, k)

    lower_bound = (1-epsilon) * n
    upper_bound = (1+epsilon) * n

    n_average_success = (lower_bound <= n_average) and (n_average <= upper_bound)

    return n_average_success

def output_results(epsilon, delta, test_num, n, filename, trials):
    '''
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

    file.write("\nN IS NOW " + str(n) + "\n") 
        # N for now as we are concerned with the effect of N
    for i in range(trials):
        result = binary_search_helper(epsilon, delta, test_num, n)
        result_array.append(result)
        line = str(result) + "\n"
        file.write(line)
    
    now = datetime.datetime.now()
    end = time.time()
    total_time = math.floor(end - start)

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
    

def binary_search_helper(epsilon, delta, test_num, n):
    '''Takes in an epsilon and delta value to test to find a value
    for k within 1 <= k <= (3/pi)*(1/(epislon^2 * delta)) using binary
    search. The number of tests and n value is hard-coded/fixed in the
    function. Returns the best k, by returning the lower boundary when
    the search stops.
    '''
    low = 1
    initial_high = (3/math.pi) * (1/ ((epsilon ** 2) * delta))
    high = initial_high
    #test_num = 200
    #n = 1000
    '''
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))
     '''   

    while (high > low+1):
        middle = math.floor((low + high) / 2)
        k = middle
        success_total = 0
        for i in range(test_num):
            if (in_interval(n, k, epsilon)):
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
    print("Best K Found : " + str(low))
    print("Initial High : " + str(initial_high))

    
    now = datetime.datetime.now()
    end = time.time()
    print("\nDate and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(math.floor(end - start)) + " seconds")
    '''
    return low


#------------------ TESTING BEGINS (epsilon, delta, test_num, n)--------------
#binary_search_helper(0.1, 0.2, 700, 5000)


# May 21st OVERNIGHT TESTS: This will test test_num from 400-1000
''' MAY 21st Overnight Tests
# Based on these tests, 100 tests ~ 100 seconds (maybe extra 6s)
for test_num in range(400, 1100, 100):
    for j in range(10):
        binary_search_helper(0.1, 0.1, test_num, 1000)'''

# May 22nd OVERNIGHT TESTS
# This will test different set sizes (n)
# Test out n = 100, 500, 2000
# Time for one run: 
'''
print("--------N = 100 STARTS------------")
for j in range(35): # ~415 seconds/each, round tp 500
    binary_search_helper(0.1, 0.2, 700,100)
print("\n--------N = 500 STARTS------------")
for k in range(35): # ~479 seconds/each, round to 500
    binary_search_helper(0.1, 0.2, 700,500)
print("\n--------N = 2000 STARTS------------")
for l in range(35): # ~ 737 seconds/each, round to 800
    binary_search_helper(0.1, 0.2, 700, 2000)
'''

'''
# May 23rd OVERNIGHT TESTS
# This will test increasingly larger values of N to see if the best k found
# really tends towards a square root function
# Will test out n = 3k, 4k, 5k
output_results(0.1, 0.2, 700, 3000, 'May23_out', 40)
output_results(0.1, 0.2, 700, 4000, 'May23_out', 40)
output_results(0.1, 0.2, 700, 5000, 'May23_out', 40)
'''

'''
# May 24th WEEKEND TESTS
output_results(0.2, 0.2, 700, 100, 'Weekend_out', 90)
output_results(0.2, 0.2, 700, 500, 'Weekend_out', 90)
output_results(0.2, 0.2, 700, 1000, 'Weekend_out', 90)
output_results(0.2, 0.2, 700, 2000, 'Weekend_out', 90)
output_results(0.2, 0.2, 700, 3000, 'Weekend_out', 90)
output_results(0.2, 0.2, 700, 4000, 'Weekend_out', 90)
output_results(0.2, 0.2, 700, 5000, 'Weekend_out', 90)
'''


# May 27th OVERNIGHT TESTS
output_results(0.2, 0.1, 700, 100, 'May27th_out', 85)
output_results(0.2, 0.1, 700, 500, 'May27th_out', 85)
output_results(0.2, 0.1, 700, 1000, 'May27th_out', 85)
output_results(0.2, 0.1, 700, 2000, 'May27th_out', 85)
output_results(0.2, 0.1, 700, 3000, 'May27th_out', 85)
output_results(0.2, 0.1, 700, 4000, 'May27th_out', 85)
output_results(0.2, 0.1, 700, 5000, 'May27th_out', 85)



# Tests to determine runtime and therefore how many trials to fit in overnight
#output_results(0.2, 0.1, 700, 5000, 'time_test', 5)