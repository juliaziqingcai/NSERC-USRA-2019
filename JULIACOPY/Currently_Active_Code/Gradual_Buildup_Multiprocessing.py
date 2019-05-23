'''
This file is just a series of exercises in which I learn
the different steps to using the Multiprocessing
module in Python. Different steps are commented
out to allow for manipulation of different capabilities.

May 16th, 2019 - May 22nd, 2019
'''


from multiprocessing import Process
import time
import random


'''TESTING HOW MANY PROCESSORS THIS MACHINE HAS
import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())
'''

'''
#BASIC DUAL PROCESS SETUP/RUNNING

def func1(name):
    random.seed()
    print ('start func1')
    n = random.randint(1, 10)
    time.sleep(n)
    print(name)
    print ('end func1')
    return 22

def func2():
    random.seed()
    print ('start func2')
    n = random.randint(1, 10)
    time.sleep(n)
    print ('end func2')
    return n


if __name__=='__main__':
    p1 = Process(target = func1, args=('Julia', ))
    p2 = Process(target = func2)
    p1.start(), p2.start() # can start 2 processes at once
'''

##############################
from multiprocessing import Pool
import curses
'''
#LEARNING HOW TO RETURN VALUES FROM DIFFERENT FUNCTIONS WHILE MULTIPROCESSING
def square(x):
    return x ** 2


def cube(y):
    return y ** 3


if __name__ == '__main__':
    pool = Pool(processes=20)
    result_squares = pool.map_async(square, range(10))
    result_cubes = pool.map_async(cube, range(10))

    print (result_squares.get(timeout=1))
    print (result_cubes.get(timeout=1))
'''


##############################
'''# Q:CAN MULTIPROCESSING ONLY HAPPEN IN MAIN?????
# A: NO, IT CAN HAPPEN ANYWHEREEEEEE, YEAAAAAAAA

def square(x):
    return x ** 2


def cube(y):
    return y ** 3

def func3():
    pool = Pool(processes=20)
    result_squares = pool.map_async(square, range(10))
    result_cubes = pool.map_async(cube, range(10))

    print (result_squares.get(timeout=1))
    print (result_cubes.get(timeout=1))

#if __name__ == '__main__':
 #   func3()

func3()
'''


##############################
'''
# Q: Can we do multiple input parameters?
# A: Yes, must use the pool.apply() function.

def func4(x, y):
    return ((x ** 2) - y)



if __name__ == '__main__':
    pool = Pool(processes=20)
    result = pool.apply_async(func4, args=(5, 3))

    print (result)

'''


##############################
'''
import multiprocessing as mp
import time

def foo_pool(x):
    return x*2

def foo_pool2(x, y):
    return y - x

result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
    pool = mp.Pool()
    for i in range(1000,2000, 10):
        pool.apply_async(foo_pool, args = (i,), callback = log_result)
        #MUST HAVE THE COMMA WHEN THERE IS ONLY ONE ARGUMENT
    pool.close()
    pool.join()
    print(result_list)
    return result_list

if __name__ == '__main__':
    apply_async_with_callback()
    '''


##############################
'''
import multiprocessing
from itertools import product

def merge_names(a, b):
    return '{} & {}'.format(a, b)

if __name__ == '__main__':
    names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(merge_names, product(names, repeat=2))
    print(results)
    '''

##############################
'''
import multiprocessing
from functools import partial
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def merge_names(a, b):
    return '{} & {}'.format(a, b)

if __name__ == '__main__':
    names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
    with poolcontext(processes=3) as pool:
        results = pool.map(partial(merge_names, b='Sons'), names)
    print(results)
'''