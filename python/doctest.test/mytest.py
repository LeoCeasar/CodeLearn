#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
>>> multiply(4, 3)
12
12
>>> multiply('a', 3)
aaa
'aaa'

"""

#import testDoc

def multiply(a, b):
    print(a * b);
    return a * b;

if __name__=='__main__':
    import doctest;
    doctest.testmod(verbose=True);

multiply('1' , 3)
