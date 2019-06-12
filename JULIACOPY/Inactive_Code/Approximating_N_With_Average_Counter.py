'''
This program approximates the set size n through an
application of the Law of Large Numbers (I think the Weak one)
and with a new constant obtained after some introspection
into our initial proof. It still uses duplicate confirmation
sampling, but the average of k counters is taken instead of the median.
This uses the constant discovered for using the average counter: 2/pi
This is based on the calculations
done on May 14th, 2019.

This program also includes a test wrapper for overall
and continuous testing.

The Law of Large Numbers states that the average of samples
will converge on the expected value as the number
of trials increases towards infinity, though it doesn't
seem to say how fast the convergence happens. The speed
is of interest to our problem, so we are testing with
this program.

It currently holds multiple versions of the algorithm and
test functions to see differences (accuracy/speed) made by multi-threading,
as well as a few timeit tests to compare speeds.
'''

import math
import random
import Sampling_Until_Duplicate
import time
import datetime
import threading
import timeit
from multiprocessing.pool import ThreadPool
import timeit

def algorithm_original(n, k):
    '''
    ORIGINAL VERSION

    Original incarnation of the approximating n
    with average counter algorithm, untouched by
    speed upgrades or anything else.

    n = set size
    k = number of samples to take
    '''

    counter_sum = 0

    for i in range(k):
        counter = Sampling_Until_Duplicate.algorithm_original(n)
        counter_sum += counter
    average_counter = counter_sum / (k) # taken due to Law of Large Numbers
    
    cons = 2 / math.pi # set the c for average
    approximate_n = cons * ((average_counter - (2/3)) ** 2) #  Includes (-2/3) due to proof done on May 16. 2019

    '''CODE TO CHECK MATH PROOF
    print("\n")
    print("Average Counter                          : " + str(average_counter))
    print("Difference between Average Counter & E[X]: " + str((average_counter - (math.sqrt(n) * math.sqrt(math.pi/2)))))
    print("\n")
    '''

    expected_value = (math.sqrt(n) * math.sqrt(math.pi/2)) + (2/3)
    # expected value for comparison to see how close we really are in one run

    '''TESTING CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("N                   : " + str(n))
    print("K                   : " + str(k))
    print("X-bar               : " + str(average_counter))
    print("E[x]                : " + str(expected_value))
    print("Approximated N      : " + str(approximate_n))
    print("\n")'''
    
    return approximate_n


def algorithm(n, k): #, approximate_n_results):
    '''
    MULTI-THREADED JOINS OUTSIDE VERSION FOR MAX SPEED GAINS

    This function approximates n by applying a new constant,
    2/pi, and the Law of Large Numbers. It still uses duplicate
    confirmation sampling, but the average of k counters is taken
    instead of the median due to the Law of Large Numbers. Also
    prints a report to terminal. Returns the approximated set size.

    n = set size
    k = number of times to take a sample counter
    approximate_n_results = mutable list to ensure all approximated ns
    can be stored and analyzed, required for multithreaded testing
    '''

    #counter_sum = 0
    results = list() # required for the multi-threading to work with Sample_Until_Duplicate

    for i in range(math.floor(k/3)): #WARNING: DIVIDE BY NUMBER OF THREADS!!!!!!!
        t1 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        t2 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        t3 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        #t4 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        t1.start()
        t2.start()
        t3.start()
    t1.join()
    t2.join()
    t3.join()
        #t4.start()
        #counter = Sampling_Until_Duplicate.algorithm(n)
        #counter_sum += counter
    
    #t4.join()
    counter_sum = sum(results)
    average_counter = counter_sum / (k) # taken due to Law of Large Numbers
    
    cons = 2 / math.pi # set the c for average
    approximate_n = cons * ((average_counter - (2/3)) ** 2) #  Includes (-2/3) due to proof done on May 16. 2019

    '''CODE TO CHECK MATH PROOF
    print("\n")
    print("Average Counter                          : " + str(average_counter))
    print("Difference between Average Counter & E[X]: " + str((average_counter - (math.sqrt(n) * math.sqrt(math.pi/2)))))
    print("\n")
    '''

    expected_value = (math.sqrt(n) * math.sqrt(math.pi/2)) + (2/3)
    # expected value for comparison to see how close we really are in one run

    '''TESTING CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("N                   : " + str(n))
    print("K                   : " + str(k))
    print("X-bar               : " + str(average_counter))
    print("E[x]                : " + str(expected_value))
    print("Approximated N      : " + str(approximate_n))
    print("\n")'''
    #approximate_n_results.append(approximate_n)
    #print("\nApproximate N:" + str(approximate_n))

    return approximate_n


def algorithm2(n, k): #, approximate_n_results):
    '''
    MULTI-THREADED JOINS INSIDE VERSION

    Same as above, except it tests out slight
    modifications that change over time (eg, comparing
    non-threaded to threaded, putting joins inside or outside of
    for-loop, etc.)

    n = set size
    k = number of times to take a sample counter
    '''

    #counter_sum = 0
    #Sampling_Until_Duplicate.counter_sum_reset()
    results = list()

    for i in range(math.floor(k/3)):
        t1 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        t2 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        t3 = threading.Thread(target=Sampling_Until_Duplicate.algorithm, args=(n, results))
        t1.start()
        t2.start()
        t3.start()
        #counter = Sampling_Until_Duplicate.algorithm3(n)
        #counter_sum += counter
    t1.join()
    t2.join()
    t3.join()
    counter_sum = sum(results)
    average_counter = counter_sum / (k) # taken due to Law of Large Numbers
    
    cons = 2 / math.pi # set the c for average
    approximate_n = cons * ((average_counter - (2/3)) ** 2) #  Includes (-2/3) due to proof done on May 16. 2019

    '''CODE TO CHECK MATH PROOF
    print("\n")
    print("Average Counter                          : " + str(average_counter))
    print("Difference between Average Counter & E[X]: " + str((average_counter - (math.sqrt(n) * math.sqrt(math.pi/2)))))
    print("\n")
    '''

    expected_value = (math.sqrt(n) * math.sqrt(math.pi/2)) + (2/3)
    # expected value for comparison to see how close we really are in one run

    '''TESTING CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("N                   : " + str(n))
    print("K                   : " + str(k))
    print("X-bar               : " + str(average_counter))
    print("E[x]                : " + str(expected_value))
    print("Approximated N      : " + str(approximate_n))
    print("\n")'''
    
    #approximate_n_results.append(approximate_n)
    return approximate_n

result_list = []

def result_list_reset():
    global result_list
    result_list = []

def summation(number):
    result_list.append(number)
    #print("Added Number: " + str(number))


def algorithm_threadpool(n, k):
    '''
    THREADPOOL VERSION

    n = set size
    k = number of samples to take
    '''

    #counter_sum = 0
    result_list_reset()
    
    p = ThreadPool(processes = 6)
    for i in range(k):
        pool_output = p.apply_async(Sampling_Until_Duplicate.original_algorithm, args= (n, ), callback= summation)
        #counter = Sampling_Until_Duplicate.algorithm3(n)
        #counter_sum += counter
    p.close()
    p.join()
    counter_sum = sum(result_list)
    #print(counter_sum)
    average_counter = counter_sum / (k) # taken due to Law of Large Numbers
    
    cons = 2 / math.pi # set the c for average
    approximate_n = cons * ((average_counter - (2/3)) ** 2) #  Includes (-2/3) due to proof done on May 16. 2019

    '''CODE TO CHECK MATH PROOF
    print("\n")
    print("Average Counter                          : " + str(average_counter))
    print("Difference between Average Counter & E[X]: " + str((average_counter - (math.sqrt(n) * math.sqrt(math.pi/2)))))
    print("\n")
    '''

    expected_value = (math.sqrt(n) * math.sqrt(math.pi/2)) + (2/3)
    # expected value for comparison to see how close we really are in one run

    '''TESTING CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("N                   : " + str(n))
    print("K                   : " + str(k))
    print("X-bar               : " + str(average_counter))
    print("E[x]                : " + str(expected_value))
    print("Approximated N      : " + str(approximate_n))
    print("\n")'''
    #print("\nApproximated N: " + str(approximate_n))
    return approximate_n


def test_wrapper1():
    '''
    SINGLE RUN OF ALGORITHM TESTER

    This is the test wrapper for the one run of the algorithm that
    allows for continuous testing with varying values
    by prompting the user for input in the terminal.
    '''
    print("\n")
    n = int(input("N value: "))
    k = int(input("K value: "))
    
    approximate_n = algorithm(n, k)
    print("\n\n\n")
    print("N                   : " + str(n))
    print("K                   : " + str(k))
    print("Approximated N      : " + str(approximate_n))
    print("\n")

    choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

    while(choice_1 != 'N'):
        choice_2 = (input("Do you want to use the same values? (Y/N) ")).upper()
        if (choice_2 != 'Y'):
            print("\n")
            n = int(input("N value: "))
            k = int(input("K value: "))

        approximate_n = algorithm(n, k)
        print("\n\n\n")
        print("N                   : " + str(n))
        print("K                   : " + str(k))
        print("Approximated N      : " + str(approximate_n))
        print("\n")
        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

# Tests
#test_wrapper1()


def test_wrapper2():
    '''
    MULTI-THREADED TESTER

    This is the continuous test wrapper for the program that
    allows for repeated and continuous testing with varying values
    by prompting the user for input in the terminal. It currently
    runs a multithreaded version of the test function to hopefully
    gain some speed.
    '''
    print("\n")
    test_num = int(input("How many tests do you want to run? "))
    n = int(input("N value: "))
    k = int(input("K value: "))

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    #approximated_n_sum = 0
    results = list()
    for i in range(math.floor(test_num/2)):
        t1 = threading.Thread(target=algorithm, args=(n, k, results))
        t2 = threading.Thread(target=algorithm, args=(n, k, results))
        #approximated_n_sum += algorithm(n, k)
        t1.start()
        t2.start()
    t1.join()
    t2.join()
    approximated_n_sum = sum(results)
    final_approximated_n = math.floor(approximated_n_sum / test_num)
    expected_value = math.floor(math.sqrt(n) * math.sqrt(math.pi/2))

    print("\n\n\n")
    print("# of Tests                  : " + str(test_num))
    print("N                           : " + str(n))
    print("K                           : " + str(k))
    print("Average Approximated N      : " + str(final_approximated_n))
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
        
        now = datetime.datetime.now()
        start = time.time()
        print("\nDate and Time at program start: " + str(now))

        #approximated_n_sum = 0
        results = list()
        for i in range(math.floor(test_num/2)):
            t1 = threading.Thread(target=algorithm, args=(n, k, results))
            t2 = threading.Thread(target=algorithm, args=(n, k, results))
            #approximated_n_sum += algorithm(n, k)
            t1.start()
            t2.start()
        t1.join()
        t2.join()
        approximated_n_sum = sum(results)
        final_approximated_n = math.floor(approximated_n_sum / test_num)
        expected_value = math.floor(math.sqrt(n) * math.sqrt(math.pi/2))

        print("\n\n\n")
        print("# of Tests                  : " + str(test_num))
        print("N                           : " + str(n))
        print("K                           : " + str(k))
        print("Average Approximated N      : " + str(final_approximated_n))
        print("\n")
        
        now = datetime.datetime.now()
        end = time.time()
        print("Date and Time at program end: " + str(now))
        print("Program Execution Time      : " + str(end - start) + " seconds")

        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

# Tests
#test_wrapper2()


def test_wrapper3():
    '''
    ORIGINAL TESTER (NO SPEED UPGRADES)

    This test wrapper tests the accuracy of testing with a for-loop
    instead of multithreading the tests.
    '''
    print("\n")
    test_num = int(input("How many tests do you want to run? "))
    n = int(input("N value: "))
    k = int(input("K value: "))

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    approximated_n_sum = 0
    #results = list()
    for i in range(math.floor(test_num)):
        #t1 = threading.Thread(target=algorithm, args=(n, k, results))
        #t2 = threading.Thread(target=algorithm, args=(n, k, results))
        approximated_n_sum += algorithm_threadpool(n, k)
        #t1.start()
        #t2.start()
    #t1.join()
    #t2.join()
    #approximated_n_sum = sum(results)
    final_approximated_n = math.floor(approximated_n_sum / test_num)
    expected_value = math.floor(math.sqrt(n) * math.sqrt(math.pi/2))

    print("\n\n\n")
    print("# of Tests                  : " + str(test_num))
    print("N                           : " + str(n))
    print("K                           : " + str(k))
    print("Average Approximated N      : " + str(final_approximated_n))
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
        
        now = datetime.datetime.now()
        start = time.time()
        print("\nDate and Time at program start: " + str(now))

        approximated_n_sum = 0
        #results = list()
        for i in range(math.floor(test_num)):
            #t1 = threading.Thread(target=algorithm, args=(n, k, results))
            #t2 = threading.Thread(target=algorithm, args=(n, k, results))
            approximated_n_sum += algorithm_threadpool(n, k)
            #t1.start()
            #t2.start()
        #t1.join()
        #t2.join()
        #approximated_n_sum = sum(results)
        final_approximated_n = math.floor(approximated_n_sum / test_num)
        expected_value = math.floor(math.sqrt(n) * math.sqrt(math.pi/2))

        print("\n\n\n")
        print("# of Tests                  : " + str(test_num))
        print("N                           : " + str(n))
        print("K                           : " + str(k))
        print("Average Approximated N      : " + str(final_approximated_n))
        print("\n")
        
        now = datetime.datetime.now()
        end = time.time()
        print("Date and Time at program end: " + str(now))
        print("Program Execution Time      : " + str(end - start) + " seconds")

        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

#test_wrapper3()


# TIMING TESTS
'''
# TIME TESTS JOINS OUTSIDE VS. JOINS INSIDE
print("\n")
print(timeit.repeat("algorithm(1000, 250)", "from __main__ import algorithm", repeat = 5, number = 100))
print("\n")
print(timeit.repeat("algorithm2(1000, 250)", "from __main__ import algorithm2", repeat = 5,  number = 100))
'''

# TIME TESTS MULTI-THREAD OUTSIDE JOIN VS THREADPOOL 
# RESULT: Multiprocessing module still blocks, is about 4 times slower.
'''
print("\n")
print(timeit.repeat("algorithm_threadpool(1000, 250)", "from __main__ import algorithm_threadpool", repeat = 5, number = 100))
print("\n")
print(timeit.repeat("algorithm(1000, 250)", "from __main__ import algorithm", repeat = 5,  number = 100))'''