#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import threading, time, random

class Counter(threading.Thread):
    def __init__(self, lock, threadName):
        '''
            @summary init 
            @param lock:锁对象,
            @param threadName : 线程名称
        '''
        super(Counter, self).__init__(name = threadName)
        self.lock = lock;
    
    def run(self):
        '''
            @summary：重写父类run 方法，在线程启动后执行该方法内的代码。
        ''' 
        global count;
        self.lock.acquire();
        
        for i in range(100):
            count = count + 1;
        self.lock.release();

lock = threading.Lock();
for i in range(5):
    Counter(lock, "thread-" + str(i)).start();
time.sleep(2);
print(count)
