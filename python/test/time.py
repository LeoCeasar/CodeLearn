#!/usr/bin/python
#coding=utf-8

import time;

ticks = time.time();
print (ticks);

localtime = time.localtime(time.time());
print (localtime);
print (time.asctime(localtime));

import calendar

cal = calendar;
print (cal.iterweekdays);
