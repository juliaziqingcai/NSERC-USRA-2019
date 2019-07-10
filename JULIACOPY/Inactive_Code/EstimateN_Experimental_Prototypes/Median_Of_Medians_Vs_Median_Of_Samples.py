'''
This program compares the accuracy of using the median 
of the medians versus the median of the samples overall
to approximate the median of a set. Done for the May 8th
2019 set of tests after the bounded inequality.

The median of medians is currently obtained through
bucket sorting through groups of 5 for greater run-time
efficiency, but can also be modified for other group sizes.

Inlcudes a test wrapper function for repeated and continous
testing.
'''

import math
import random

def get_approximated_medians(n,k):
    '''
    Obtains two approximated medians:
    1) The median of medians through bucket sort
    in groups of 5
    2) The median of the overall samples
    Returns these two in a list
    
    n = set size
    k = related to the number of samples to take
    '''
    random.seed()
    samples = list()
    
    for i in range((10*k)+5): # iterate
        index = random.randint(0, (n-1))
        samples.append(index)
        
    medians = list()
    for j in range(0, (2*k) + 1):
        subsection = samples[(5*j):(5*j)+5]
        subsection.sort()
        medians.append(subsection[2])
    
    medians.sort()
    samples.sort()
    
    return [medians[k], samples[(5*k)+2]]


def single_run( n, delta, k):
    ''' Compares a single run of the median of medians and the median 
    of samples to the true median.
    Prints report, and returns both medians.
    
    n = size of set
    delta = margin of error
    k = related to samples taken.
    '''
    medians = get_approximated_medians(n, k)
    approximate_median = medians[0]
    sample_median = medians[1]
    real_median = math.floor(n/2)
    
    '''TEST ONLY CODE for one run
    print("\nMedian of Medians   : " + str(approximate_median))
    print("Median of Samples   : " + str(sample_median))
    print("True Median         : " + str(n/2))
    '''

    
    return [approximate_median, sample_median]


def sample_median_better(test_num, n, delta, k):
    ''' Tests if the median of the medians or the median of samples is closer
    to the true median on average with a printed report.
    
    test_num = number of test runs for algorithm
    n = set size
    delta = margin of error
    k = related to number of samples taken
    '''
    sample_median_success = 0
    for i in range(test_num):
        medians = get_approximated_medians(n, k)
        approximate_median = medians[0]
        sample_median = medians[1]
        real_median = math.floor(n/2)
        if (abs(real_median - sample_median) < abs(real_median - approximate_median)):
            sample_median_success += 1
    probability = sample_median_success / test_num
    print("\n\n")
    print("# Trials                    : " + str(test_num))
    print("N                           : " + str(n))
    print("Delta                       : " + str(delta))
    print("K                           : " + str(k))
    print("Real Median                 : " + str(real_median))
    print("Pr[sample median is better] : " + str(probability))
    

def test_wrapper():
    '''
    This is the test wrapper for the overall program.
    Allows repeated and overall comparisons between the
    median of medians and the median of samples by prompting
    the user for values to plug in the terminal.
    '''
    
    print("\n\n")
    test_num = int(input("How many tests do you want to run? "))
    n= int(input("What set size do you want to use? "))
    delta = float(input("What delta do you want to use? "))
    k = int(input("What k value do you want to use? "))
    sample_median_better(test_num, n, delta, k)
    choice = (input("\nDo you want to try another run (Y/N)? ")).upper()
    
    while (choice != "N"):
        print("\n\n")
        test_num = int(input("\n\nHow many tests do you want to run? "))
        n= int(input("What set size do you want to use? "))
        delta = float(input("What delta do you want to use? "))
        k = int(input("What k value do you want to use? "))
        sample_median_better(test_num, n, delta, k)
        choice = input("\nDo you want to try another run (Y/N)? ")    
        
# Tests
        
#sample_median_better(1000, 10000, 0.1, 2)
#test_wrapper()