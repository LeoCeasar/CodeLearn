#!/usr/local/python
#coding=utf-8

import random

#
#    lambda只是一个表达式，函数体比def简单很多。
#    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
#    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
sum = lambda arg1, arg2: arg1 + arg2;

def printstr( st):
	print (st);

	return random.choice([True, False]);

def changeDate (date):
	date = "change for";
	if (printstr(date)):
		print ("printstr is do well");
	else :
		print ("printstr is not do well");

a = "i";
print("first ",a);
changeDate(a);
print("last :",a);

def foo (arg1, arg2="OK", *tupleArg, **diArg):
	print ("arg1 = ", arg1);
	print ("arg2 = ", arg2);

	for i, element in enumerate(tupleArg):
		print ("tupleArg %d-->%s"%(i, str(element)));

	if (diArg):
		for key in diArg:
			print ("diArg %s-->%s"%(key,diArg[key]));

myList = ["my1","my2"];
myDict = {"name":"Tom", "age":22};

foo("formal_args", arg2="ageSecond", a = 1);
print ("*"*49);
foo(123, myList, myDict);
print ("*"*40);
foo(123, rt=123, *myList, **myDict);
"""
16
　　　参数中如果使用“*”元组参数或者“**”字典参数，这两种参数应该放在参数列表最后。并且“*”元组参数位于“**”字典参数之前。
　　　关键字参数rt=123,因为函数foo(arg1,arg2="OK",*tupleArg,**dictArg)中没有rt参数，所以最后也归到字典参数中。

代码第14行
　　元组对象前面如果不带“*”、字典对象如果前面不带“**”，则作为普通的对象传递参数。
　　多余的普通参数，在foo(123,myList,myDict)中，123赋给参数arg1，myList赋给参数arg2，多余的参数myDict默认为元组赋给myList。
"""
