#!/usr/bin/python
#coding=utf-8


"""
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""
class Employee:
	empCount = 0;

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1;
	
	def displayCount(self):
		print "Total Employee %d" %Employee.empCount

	def displayEmployee(self):
		print "Name:",self.name,", salary:",self.salary;

tmp = Employee("D.R", 1111);
tmp.displayCount();
tmp.displayEmployee();
