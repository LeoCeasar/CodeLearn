#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import time, threading, os

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock();

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
    #tmp = GetCurrentThreadId();
    print('id: %s  blance: %s' %(os.getpid(), threading.current_thread().name));
    #print('id: %s  blance: %s' %(os.getpid(), str(balance)));

def run_thread(n):
    lock.acquire();
    for i in range(100000):
        try:
            #lock.acquire();
            change_it(n)
        except Exception as e:
            print(e);
        finally:
            #lock.release();
            pass;
    lock.release();

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
