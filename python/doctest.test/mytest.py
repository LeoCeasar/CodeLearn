#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import testDoc

def multiply(a, b):
    print(a * b);
    return a * b;

if __name__=='__main__':
    import doctest;
    doctest.testmod(verbose=True);

