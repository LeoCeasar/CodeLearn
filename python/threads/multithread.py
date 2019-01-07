#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s) ....' %(name, os.getpid())) ;

if __name__=='__main__':
    print ('Parent processi %s will start' % os.getpid());
    p = Process(target=run_proc, args=('test',));
    print('Child process will start');
    p.start()
    p.join();
    print('Child process end');
