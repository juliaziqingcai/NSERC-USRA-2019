#!/usr/bin/python

'''
This file is for learning how to use the multithreading
module in Python.

May 22nd, 2019 - Current
'''


import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self): #run() is called by invoking start(), which starts a new thread
      print("Starting " + self.name)
      print_time(self.name, 2, self.counter)
      print("Exiting " + self.name)
      return 3

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      print(counter)
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")

thread1.join()