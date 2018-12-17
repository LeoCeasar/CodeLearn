#!/usr/bin/python
#coding=utf-8

numbers = [12, 37, 5, 42, 8, 3];
even = [];
odd = [];

while len(numbers) > 0:
    number = numbers.pop();

    if (number % 2 == 0):
        even.append(number);
    else:
        odd.append(number);
else:
    print "else out 1";

print even
print odd

i = 2;
while ( i < 100):
    j = 2;
    while (j <= (i/j)):
        if not(i%j):break;
        j = j+1;
    if (j > i/j) : print i ,"是素数";
    i = i + 1;
else:
    print "素数out";
