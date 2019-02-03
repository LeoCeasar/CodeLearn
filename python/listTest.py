#!/usr/bin/python
#coding=utf-8

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4 , 5, 6, 7, 8];

print list1;
print list2[1:5];

del list2[2];
print list2;

list1.append('123');
print len(list1);

list3 = list1 + list2;
print list3;

if 3 in list2:
    print "OK";
else :
    print "FALSE";

if 2 in list2:
    print "OK";
else :
    print "FALSE";

