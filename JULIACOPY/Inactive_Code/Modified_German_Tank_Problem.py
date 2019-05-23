'''
This program is based off the modified version of the
German Tank Problem explored on May 10th, 2019.

Our modified version does sampling with replacement,
keeps track of the minimum value sampled, and uses all of S.

The original problem does sampling without replacement,
keeps track of the maximum value sampled, and uses subsets.

This also includes a series of test wrappers based off the different
levels of integration with previous algorithms as outlined    approximation_array = list()
    for i in range((2* k)+ 1):
        approximation_array.append(Appromixmating_N.algorithm(n))
    approximation_array.sort()
    approximate_n = approximation_array[k]
in the notes for May 10th and 13th, 2019 that allow for repeated and
continuous testing.
'''

import math
import random
import Approximating_N_With_2kPlus1_Samples # imported for level 2 of testing 
import datetime
import time

def modified_german_tank_formula(n, k):
    '''
    This is a modified version of the german tank formula in which
    we sample WITH replacement, record the MIN value seen, and use the
    whole set. Returns an approximation of the set size calculated by
    the following formula:

            n~ = (#samples + 1) * (min. of samples)
    
    n = set size
    k = number of samples to take
    '''

    random.seed()
    samples = list()
    
    for i in range(k):
        index = random.randint(1, n)
        samples.append(index)
    
    samples.sort()
    min_sample = samples[0]

    return (len(samples) + 1) * (min_sample)


def modified_german_tank_formula_median(l, n, k):
    '''
    This is the test wrapper so that we can run the modified german tank 
    formula 2l + 1 times and take the median of the approximated set sizes 
    to hopefully achieve a more accurate result. Also tests out the
    efficacy of the average of the samples taken and allows the user to 
    compare the two simultaneously. Prints a report to the terminal.
    Returns the median of the approximated set sizes.

    l = related to 2l+1 runs of algorithm
    n = set size
    k = # of samples to take in one run of modified formula
    ''' 

    approximate_ns = list()
    
    for i in range((2*l)+1):
        approximate_ns.append(modified_german_tank_formula(n, k))
    
    approximate_ns.sort()
    average_approximate_n = math.floor((sum(approximate_ns)) / len(approximate_ns))
    median_approximate_n = math.floor(approximate_ns[l] + (approximate_ns[l] * 0.5))

    '''TESTING ONLY CODE for test_wrapper()
    print("\n\n\n")
    print("-------------------------------------------")
    print("L                      : " + str(l))
    print("N                      : " + str(n))
    print("K                      : " + str(k))
    print("Median Approximate N   : " + str(median_approximate_n))
    print("Average Approximate N  : " + str(average_approximate_n))
    print("\n")
    '''

    return median_approximate_n


def test_wrapper1():
    ''' 
    This is a test wrapper to for Level 1 (Pink Bracket) 
    of the code try for May 10th. Only tests the efficacy of the modified 
    german tank formula directly above. Repeatedly prompts the user for 
    values and allows for continuous testing with varying values.
    '''
    print("\n\n")
    l = int(input("L value: "))
    n = int(input("N value: "))
    k = int(input("K value: "))
    modified_german_tank_formula_median(l, n, k)
    choice_1 = (input("\nDo you want to run another trial? (Y/N) ")).upper()
    while (choice_1 != 'N'):
        choice_2 = (input("Do you want to use the same values? (Y/N) ")).upper()
        print("\n\n")
        if (choice_2 != 'Y'):
            l = int(input("L value: "))
            n = int(input("N value: "))
            k = int(input("K value: "))
            
        modified_german_tank_formula_median(l, n, k)
        choice_1 = (input("\nDo you want to run another trial? (Y/N) ")).upper()

#Tests for test_wrapper1()
#test_wrapper1()



def n1_vs_n2(l, n, k):
    '''
    On May 13th, we discussed using the approximated set size n1 from the
    median of the duplicate confirmation sample algorithm (Approximating_N_With_2k+1_Samples algorithm)
    and using n1 as input for the modified_german_tank_formula_median to get
    another approximation for n, called n2 to see if we can get a better estimate
    for n.

    This is function that tests out if n1 or n2 is closer to the actual set size for one run.
    This prevents cheating by using the value of n itself directly for sampling. 
    Prints a report to terminal. Returns a boolean indiciating if n2 is closer or not.

    n1 = approximated set size from the Approximating_N_With_2k+1_Samples algorithm
    n2 = approximated set size from the modified_german_tank_formula_median
         above in this file, using n1 as the n input value
    
    l = related to 2l+1 odd times to run/sample with modified german tank formula
    n = actual set size
    k = related to 2k+1 odd times to run/sample with duplicate confirmation sampling formula
    '''

    n1 = Approximating_N_With_2kPlus1_Samples.algorithm(n, k)   #approximation_array[k]
    n2 = modified_german_tank_formula_median(l, n1, math.floor(math.sqrt(n1)))
    # use n1 and sqrt(n1) as input for algorithm 2

    n2_better = abs(n-n2) <= abs(n-n1)
    
    '''#TESTING ONLY CODE for one run
    print("\n\n\n")
    print("-------------------------------------------")
    print("L                      : " + str(l))
    print("K                      : " + str(k))
    print("N                      : " + str(n))
    print("N1                     : " + str(n1))
    print("N2                     : " + str(n2))
    print("N2 Closer to N         : " + str(n2_better))
    print("\n")'''
    
    return n2_better

# Tests n1_vs_n2(l,n, k)
#n1_vs_n2(100, 100, 100)   


def test_wrapper2():
    '''
    This is the test wrapper function to compare a larger
    number of test runs for the n1_vs_n2 function directly above.
    Repeatedly prompts the user for values and allows for continuous 
    testing with varying values. Prints a report to terminal.
    '''
    
    print("\n\n")
    test_num = int(input("How many tests do you want to run? "))
    l = int(input("L value: "))
    n = int(input("N value: "))
    k = int(input("K value: "))

    n2_success = 0

    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))
    

    for i in range(test_num):
        if(n1_vs_n2(l, n, k)):
            n2_success += 1

    print("\n")
    print("-------------------------------------------")
    print("Number of tests        : " + str(test_num))
    print("L                      : " + str(l))
    print("K                      : " + str(k))
    print("N                      : " + str(n))
    print("Pr[N2 Closer to N]     : " + str(n2_success/test_num))
    print("\n")
    
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")

    choice_1 = (input("\nDo you want to run another trial? (Y/N) ")).upper()

    while (choice_1 != 'N'):

        print("\n\n")
        test_num = int(input("How many tests do you want to run? "))
        choice_2 = (input("Do you want to use the same values? (Y/N) ")).upper()

        if (choice_2 != 'Y'):
            l = int(input("L value: "))
            n = int(input("N value: "))
            k = int(input("K value: "))
            
        n2_success = 0

        now = datetime.datetime.now()
        start = time.time()
        print("\nDate and Time at program start: " + str(now))

        for i in range(test_num):
            if(n1_vs_n2(l, n, k)):
                n2_success += 1

        print("\n")
        print("-------------------------------------------")
        print("Number of tests        : " + str(test_num))
        print("L                      : " + str(l))
        print("K                      : " + str(k))
        print("N                      : " + str(n))
        print("Pr[N2 Closer to N]     : " + str(n2_success/test_num))
        print("\n")
        
        now = datetime.datetime.now()
        end = time.time()
        print("Date and Time at program end: " + str(now))
        print("Program Execution Time      : " + str(end - start) + " seconds")

        choice_1 = (input("\nDo you want to run another trial? (Y/N) ")).upper()



#Tests for test_wrapper2()
test_wrapper2()

