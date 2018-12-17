#!/usr/local/python
#coding=utf-8

try:
	fh = open("testfile", "w");
	try:
		fh.write("!#/usr/local/python\r\n#coding=utf-8");
	finally:
		print "close file";
		fh.close();
except IOError:
	print "Error IOError";
