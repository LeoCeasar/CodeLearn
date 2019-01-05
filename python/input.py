#!/usr/bin/python
#coding=utf_8

str = raw_input("Enter your input:");

if str == 'next' or str== '':
    str2 = input("Enter your input next:");
    if str2=='':
        print 'bad boy!';
    else:
        print "Result " ,str2;
else:
    print "you are welcome! received:", str;
