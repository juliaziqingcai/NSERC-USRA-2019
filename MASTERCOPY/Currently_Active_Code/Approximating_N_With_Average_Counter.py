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

@author Julia Cai, Alexa de Grandmont
version. 1.0.0
Last Revision: May 16th, 2019
'''

import math
import random
import Sampling_Until_Duplicate
import time
import datetime

def algorithm(n, k):
    '''
    This function approximates n by applying a new constant,
    2/pi, and the Law of Large Numbers. It still uses duplicate
    confirmation sampling, but the average of k counters is taken
    instead of the median due to the Law of Large Numbers. Also
    prints a report to terminal. Returns the approximated set size.

    n = set size
    k = number of times to take a sample counter
    '''

    counter_sum = 0

    for i in range(k):
        counter = Sampling_Until_Duplicate.algorithm(n)
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


def test_wrapper1():
    '''
    This is the test wrapper for the one run of the algorithm that
    allows for continuous testing with varying values
    by prompting the user for input in the terminal.
    '''
    print("\n")
    n = int(input("N value: "))
    k = int(input("K value: "))
    
    algorithm(n, k)

    choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

    while(choice_1 != 'N'):
        choice_2 = (input("Do you want to use the same values? (Y/N) ")).upper()
        if (choice_2 != 'Y'):
            print("\n")
            n = int(input("N value: "))
            k = int(input("K value: "))
        algorithm(n, k)
        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

# Tests
#test_wrapper1()


def test_wrapper2():
    '''
    This is the continuous test wrapper for the program that
    allows for repeated and continuous testing with varying values
    by prompting the user for input in the terminal.
    '''
    print("\n")
    test_num = int(input("How many tests do you want to run? "))
    n = int(input("N value: "))
    k = int(input("K value: "))

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    approximated_n_sum = 0
    for i in range(test_num):
        approximated_n_sum += algorithm(n, k)

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
        for i in range(test_num):
            approximated_n_sum += algorithm(n, k)

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
