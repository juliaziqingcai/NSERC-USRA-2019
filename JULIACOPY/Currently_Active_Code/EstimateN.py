'''
This program is based off the 1st program 
discussed on May 30th, 2019.

It essentially pulls all the moving parts of
using the average counter, finding the best k, and
then approximating n together. It is different to
Approximating_N_With_Average_Counter, since that
algorithm just approximates n directly from an
input n and k, which is a lesser level of optimization
than what we are attempting here.

For the most basic verion started on May 30th, we have
to assume that we know the formula to get a best_k value
(which we are trying to tease out with the Binary_Search_Best_K program,
which is NOT directly used in this file)
and will use placeholder values for k in the meantime.
'''

import Sampling_Until_Duplicate
import math
import time
import datetime
import timeit


def in_interval(epsilon, actual_value, approximate_value):
    '''
    Returns a boolean indicating if the approximated value
    is within an acceptable interval of the actual value.
    '''
    lower_bound = (1-epsilon) * actual_value
    upper_bound = (1+epsilon) * actual_value
    success = (lower_bound <= approximate_value) and (approximate_value <= upper_bound)

    return success


def EstimateN_original(epsilon, delta, n):
    '''
    1ST VERSION (NO SPEED GAINS)

    We assume we know the formula to calculate a best_k
    value, but we use a placeholder for now.

    Determines a best_k value, then repeats 
    Sample Until Duplicate (SUD) k times to get
    an approximation of mu (average counter),
    and then calculates an approximation of n.
    Returns an approximation of the set size.

    epsilon = related to acceptable interval
    delta = related to probability and margin of error
    n = actual set size
    '''

    '''
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))'''

    best_k = math.floor((12 / math.pi) * (1 / ((epsilon ** 2) * delta))) # placeholder for k*(epsilon, delta), AKA # of calls to SUD
    approximate_mu = Sampling_Until_Duplicate.RSUD(n, best_k)

    approximate_n = (2 / math.pi) * ((approximate_mu - (2/3)) ** 2)

    
    # CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("----EstimateN Algorithm Run Report----\n")
    print("Epsilon                     : " + str(epsilon))
    print("Delta                       : " + str(delta))
    print("N                           : " + str(n))
    print("K*                          : " + str(best_k))
    print("# of SUD calls              : " + str(best_k))
    print("Mu~                         : " + str(approximate_mu))
    print("N~                          : " + str(approximate_n))
    print("\n")
    

    '''
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")
    '''

    return approximate_n


def NewEstimateN_original(epsilon, delta, n):
    '''
    LAYERED VERSION OF ESTIMATE_N (NO SPEED GAINS)(ORIGINAL VERSION)

    For now, we use a placeholder for the formula
    to find a best_k value since we don't know it yet.

    This version holds delta constant to 1/4 and
    uses an l value to run RSUD. The l value is calculated
    as follows:

        l = 12 * ln(1/delta)

    Calculates and returns an approximation of n by using the
    median of the counters returned by l runs of RSUD. Now that we have
    the proper relation for k*(epsilon), this function approximates n
    by running RSUD(n, k) as though delta was 1/4 and take the median
    of those counters, and approximate n from there.
    '''

    '''
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))
        '''


    #delta = 1/4 # DO NOT UNCOMMENT, not necessary now that we have actual k*(epsilon) relationship
    #best_k = math.floor((48 / math.pi) * (1 / (epsilon ** 2))) # Placeholder until we find actual k*(epsilon, delta) formula
    best_k = math.ceil(1.2632/ (epsilon ** 2))# Actual relationship based on test data
    l = math.ceil(12 * math.log((1/delta))) # This delta MUST be the input delta

    mu_array = list()
    for i in range(l):
        mu_array.append(Sampling_Until_Duplicate.RSUD_original(n, best_k))
    
    mu_array.sort()
    approximate_mu = mu_array[math.floor(l/2)]

    approximate_n = (2 / math.pi) * ((approximate_mu - (2/3)) ** 2)
    # The approximation for n is reallllllly precise for larger n, BUT for smaller n, there is some error from this

    '''
    # CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("----NewEstimateN Algorithm Run Report----\n")
    print("Epsilon                     : " + str(epsilon))
    print("Delta                       : " + str(delta))
    print("N                           : " + str(n))
    print("K*                          : " + str(best_k))
    print("L                           : " + str(l))
    print("# of SUD calls              : " + str(best_k * l))
    print("Mu~                         : " + str(approximate_mu))
    print("N~                          : " + str(approximate_n))
    print("\n")
    '''

    '''
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")
    '''

    return approximate_n


def NewEstimateN_with_global_array(epsilon, delta, n):
    '''
    GLOBAL ARRAY SPEED GAIN VERSION (FASTEST CURRENT VERSION)

    For now, we use a placeholder for the formula
    to find a best_k value since we don't know it yet.

    This version holds delta constant to 1/4 and
    uses an l value to run RSUD. The l value is calculated
    as follows:

        l = 12 * ln(1/delta)

    Calculates and returns an approximation of n by using the
    median of the counters returned by l runs of RSUD. Now that we have
    the proper relation for k*(epsilon), this function approximates n
    by running RSUD(n, k) as though delta was 1/4 and take the median
    of those counters, and approximate n from there.
    '''

    
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))
        


    #delta = 1/4 # DO NOT UNCOMMENT, not necessary now that we have actual k*(epsilon) relationship
    #best_k = math.floor((48 / math.pi) * (1 / (epsilon ** 2))) # Placeholder until we find actual k*(epsilon, delta) formula
    best_k = math.ceil(1.2632/ (epsilon ** 2))# Actual relationship based on test data
    l = math.ceil(12 * math.log((1/delta))) # This delta MUST be the input delta

    mu_array = list()
    global_array = [0] * n
    for i in range(l):
        mu_array.append(Sampling_Until_Duplicate.RSUD_with_global_array(n, best_k, global_array))
    
    mu_array.sort()
    approximate_mu = mu_array[math.floor(l/2)]

    approximate_n = (2 / math.pi) * ((approximate_mu - (2/3)) ** 2)
    # The approximation for n is reallllllly precise for larger n, BUT for smaller n, there is some error from this

    
    # CODE FOR ONLY ONE RUN OF THE ALGORITHM
    print("\n\n\n")
    print("----NewEstimateN Algorithm Run Report----\n")
    print("Epsilon                     : " + str(epsilon))
    print("Delta                       : " + str(delta))
    print("N                           : " + str(n))
    print("K*                          : " + str(best_k))
    print("L                           : " + str(l))
    print("# of SUD calls              : " + str(best_k * l))
    print("Mu~                         : " + str(approximate_mu))
    print("N~                          : " + str(approximate_n))
    print("\n")
    

    
    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")
    

    return approximate_n

def test():
    '''
    TESTER FOR BOTH ESTIMATEN AND NEWESTIMATEN

    Tester function for overall program. Gives the user
    the option of choosing to test EstimateN or NewEstimateN
    after asking for all input parameters. Prints a report
    to terminal. May have to modify depending on what information
    needs to be kept until the end.
    '''

    print("\n")
    test_num = int(input("How many tests do you want to run? "))
    epsilon = float(input("Epsilon value : "))
    delta = float(input("Delta value: "))
    n = int(input("N value: "))
    successes = 0

    algorithm_choice = int(input("\nWhich algorithm do you want to test? \n" \
        + "(1) for EstimateN (2) for NewEstimateN : ")) #Gives user a choice of algorithm to test
    
    now = datetime.datetime.now()
    start = time.time()
    print("\nDate and Time at program start: " + str(now))

    if (algorithm_choice == 1): # runs EstimateN algorithm

        for i in range(test_num):
            result = EstimateN_original(epsilon, delta, n)
            if(in_interval(epsilon, n, result)):
                successes += 1
        
    else: # Runs NewEstimateN algorithm

        for i in range(test_num):
            result = NewEstimateN_original(epsilon, delta, n)
            if(in_interval(epsilon, n, result)):
                successes += 1

    success_prob = successes / test_num

    print("\n\n\n")
    print("----Test Run Report Report----\n")
    if (algorithm_choice == 1):
        print("Algorithm Run               : EstimateN")
    else:
        print("Algorithm Run               : NewEstimateN")
    print("# of Tests Run              : " + str(test_num))
    print("Epsilon                     : " + str(epsilon))
    print("Delta                       : " + str(delta))
    print("N                           : " + str(n))
    print("Pr[Success]                 : " + str(success_prob))
    print("\n")

    now = datetime.datetime.now()
    end = time.time()
    print("Date and Time at program end: " + str(now))
    print("Program Execution Time      : " + str(end - start) + " seconds")

    choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()

    while(choice_1 != 'N'): # While loop for continuous testing
        print("\n")
        
        test_num = int(input("How many tests do you want to run? "))
        epsilon = float(input("Epsilon value : "))
        delta = float(input("Delta value: "))
        n = int(input("N value: "))
        successes = 0

        algorithm_choice = int(input("\nWhich algorithm do you want to test? \n" \
            + "(1) for EstimateN (2) for NewEstimateN : ")) #Gives user a choice of algorithm to test
        
        now = datetime.datetime.now()
        start = time.time()
        print("\nDate and Time at program start: " + str(now))

        if (algorithm_choice == 1): # runs EstimateN algorithm

            for i in range(test_num):
                result = EstimateN_original(epsilon, delta, n)
                if(in_interval(epsilon, n, result)):
                    successes += 1
            
        else: # Runs NewEstimateN algorithm

            for i in range(test_num):
                result = NewEstimateN_original(epsilon, delta, n)
                if(in_interval(epsilon, n, result)):
                    successes += 1

        success_prob = successes / test_num


        print("\n\n\n")
        print("----Test Run Report Report----\n")
        if (algorithm_choice == 1):
            print("Algorithm Run               : EstimateN")
        else:
            print("Algorithm Run               : NewEstimateN")
        print("# of Tests Run              : " + str(test_num))
        print("Epsilon                     : " + str(epsilon))
        print("Delta                       : " + str(delta))
        print("N                           : " + str(n))
        print("Pr[Success]                 : " + str(success_prob))
        print("\n")

        now = datetime.datetime.now()
        end = time.time()
        print("Date and Time at program end: " + str(now))
        print("Program Execution Time      : " + str(end - start) + " seconds")

        choice_1 = (input("Do you want to run another trial? (Y/N) ")).upper()


def output_results_NewEstimateN(epsilon, delta, n, filename, trials):
    '''
    ORIGINAL

    Allows for results to be written to a LibreOffice datasheet for
    easier transcription and manipulation, instead of manually
    copying results. Also outputs a summary of results. Due to the
    extra file writing, please put in an integer for trials >= 2

    epsilon = related to the accepted interval
    delta = related to the confidence interval
    n = actual set size
    filename = string that represents the file name
    trials = number of trials to run for each set of values
    '''
    file = open( filename + '.ods', 'a') #appends, so we don't overwrite

    now = datetime.datetime.now()
    start = time.time()
    file.write("\n------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\nDate and Time at program start: " + str(now))
    
    result_array = list()
    successes = 0

    file.write("\nApproximations of N \n") 
    
    for i in range(trials):
        result = NewEstimateN_original(epsilon, delta, n)
        if(in_interval(epsilon, n, result)):
            successes += 1
        result_array.append(result)
        line = str(result) + "\n"
        file.write(line)
    
    success_prob = successes / trials

    now = datetime.datetime.now()
    end = time.time()
    total_time = end - start


    file.write("\nDate and Time at program end: " + str(now))
    file.write("\nTotal Time Taken: ")
    file.write(str(total_time) + " seconds\n")
    file.write("\n----Test Run Report Report----\n")
    file.write("\n# of Trials Run                      : ")
    file.write(str(trials))
    file.write("\nEpsilon                                : ") 
    file.write(str(epsilon))
    file.write("\nDelta                                   : ") 
    file.write(str(delta))
    file.write("\nN                                        : ") 
    file.write(str(n))
    file.write("\nAcceptable Upper Bound      : ")
    file.write(str((1+epsilon)*n))
    file.write("\nAcceptable Lower Bound      : ")
    file.write(str((1-epsilon)*n))
    file.write("\nPr[Success]                        : ") 
    file.write(str(success_prob))
    file.write("\n\n")



# TESTING BEGINS
#test()

'''
# JUNE 10TH 2019 OVERNIGHT TESTS
# The purpose of these tests is to get different success probabilities for the algorithm
# And see the effect of smaller ranges of n on overall precision
for i in range(5, 105, 5):
    output_results_NewEstimateN(0.01, 0.2, i, 'June10_out', 13)
    output_results_NewEstimateN(0.1, 0.2, i, 'June10_out', 13)
    '''

'''
# JUNE 11th 2019 OVERNIGHT TESTS
output_results_NewEstimateN(0.01, 0.2, 1000000, 'June11_out', 4)
output_results_NewEstimateN(0.02, 0.2, 1000000, 'June11_out', 4)
output_results_NewEstimateN(0.1, 0.2, 1000000, 'June11_out', 4)
output_results_NewEstimateN(0.01, 0.2, 10000000, 'June11_out', 4)
output_results_NewEstimateN(0.02, 0.2, 10000000, 'June11_out', 4)
output_results_NewEstimateN(0.1, 0.2, 10000000, 'June11_out', 4)
'''

'''
# TIME TESTS
# We learned that using a global array that resets is ALWAYS faster no matter the n or epsilon WOW!!
# l=[] is ALWAYS faster than l=list() for declaring new lists in Python
# Can check with python3 -mtimeit "l=[]" and python3 -mtimeit "l=list()" in terminal
print("\n")
print(timeit.repeat("NewEstimateN_original(0.1,0.2,1)", "from __main__ import NewEstimateN_original", repeat =3, number = 1))
print("\n")
print(timeit.repeat("NewEstimateN_with_global_array(0.1,0.2,1)", "from __main__ import NewEstimateN_with_global_array", repeat =3,  number = 1))
'''
NewEstimateN_with_global_array(0.01, 0.2, 100000000)

