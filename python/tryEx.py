#!/usr/local/python
#coding=utf-8

import sys;

class MyError(RuntimeError):
	def __init__(self, arg):
		self.arg = arg;


try:
	fh = open("testfile", "w");
	try:
		fh.write("!#/usr/local/python\r\n#coding=utf-8");
	finally:
		print("close file");
		fh.close();
except IOError:
	print("Error IOError");

def mye(level):
	if level < 1:
		raise Exception("Invalid level");
	else:
		raise MyError("real level");

try:
	mye(2);
except Exception as err:
	print(err)
else:
	print("success");


print(sys.version[0]);
	
