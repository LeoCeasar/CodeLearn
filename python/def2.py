#!/usr/local/python
#coding=utf-8

global st;
st = "output"

def printall(*vartyple):
	st = "output " + " in all :";
	print(globals());
	print(locals());
	print (st);
	for var in vartyple:
		print (var);

#print(PYTHONPATH);
printall(1,"23","456","7890");
print(st);
