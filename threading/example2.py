#!/usr/bin/python

import threading
import time


class LVAPSendConfig(threading.Thread):

    def __init__(self, thread_id, new_bw_shaper):
        threading.Thread.__init__(self)
        self.__thread_id = thread_id
        self.__new_bw_shaper = new_bw_shaper

    def run(self):
        print("Starting ", self.__thread_id, self.__new_bw_shaper)
        print_time(self.__thread_id, 5)
        print("Exiting ", self.__thread_id, self.__new_bw_shaper)

def print_time(threadName, delay):
    time.sleep(delay)
    print("%s: %s" % (threadName, time.ctime(time.time())))

# Create new threads
thread1 = LVAPSendConfig("Thread-1", 100)
thread2 = LVAPSendConfig("Thread-2", 10)

# Start new Threads
thread1.start()
time.sleep(10)
thread2.start()

print("Exiting Main Thread")