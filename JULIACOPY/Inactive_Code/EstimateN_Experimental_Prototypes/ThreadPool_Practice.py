'''
For learning/practicing the completely undocumented ThreadPool
from Python's Multiprocessing module. This module lacks tests and
documentation.

This is another attempt to gain speed for the overall
approximation of n testing.

The issue with using Pool by itself is that every process Pool
generates gets its own separate copy. ThreadPool should allow
us to parallelize work on shared memory, so let's hope it gives
us some speed and the ability to test a range of inputs together.
'''


from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import Multiprocess_Number_Doubler
import os, time
import timeit

'''
# ---TESTS DIFFERENCE BETWEEN POOL AND THREADPOOL
# This will create 5 different processes, although the 'hi outside of main()' will
# only print once. You can see that there are different PIDs for the different
# calls to hello() though, which is different from the ThreadPool implementation
# below, which only uses the same process (same PID) and uses threads instead.


print("hi outside of main()")

def hello(x):
    print("inside hello()")
    print("Proccess id: ", os.getpid())
    time.sleep(3)
    return x*x

if __name__ == "__main__":
    p = Pool(processes = 5)
    pool_output = p.map(hello, range(3))

    print(pool_output)

# THREADPOOL VER.

print("hi outside of main()")

def hello(x):
    print("inside hello()")
    print("Proccess id: ", os.getpid())
    time.sleep(3)
    return x*x

if __name__ == "__main__":
    p = ThreadPool(processes = 5)
    pool_output = p.map(hello, range(3))

    print(pool_output)

'''


# ---TESTING TIME DIFFERENCES BETWEEN POOL AND THREADPOOL
# Discovered that ThreadPool is objectively faster. 
# In this particular code snippet, 10 times faster (or by one
# order of magnitude). But there seems to be a very small
# limit on how many processes we can through at the CPU at once.
# The test numbers are very small.
# Current Limits: f1 -> number = 50, f2 -> number = 257

result_list = []

def summation(number):
    result_list.append(number)


def f1():
    p = Pool(processes = 6)
    pool_output = p.map(doubler, range(100))
    

def f2():
    p = ThreadPool(processes = 6)
    #pool_output = p.map(doubler, range(100))
    for i in range(10):
        pool_output = p.apply_async(Multiprocess_Number_Doubler.doubler, args= (i, ), callback= summation)
    p.close()
    p.join()
    print(result_list)
    #total_sum = sum(result_list)
    #print(total_sum)

print("\n")
#print(timeit.repeat(stmt=f1, repeat = 5, number = 50)) # if we do number=50, it crashes from too many files open
#print(timeit.timeit(stmt=f1, number=2))
print("\n")
#print(timeit.repeat(stmt=f2, repeat = 5,  number = 5)) # number = 257 is the limit here.



f2()







