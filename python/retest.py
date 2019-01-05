#!/usr/local/python
#coding=utf-8

import re;

line = "Cats are smarter than dogs";

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I);

print (matchObj);

if matchObj:
	print ("matchObj.group()", matchObj.group());
	print ("matchObj.group(1)", matchObj.group(1));
	print ("matchObj.group(2)", matchObj.group(2));
else:
	print ("No match")

phone = "2004-959-559 # 这是一个国外电话号码"

num = re.sub('#.*$', "", phone);
print (num)

num = re.sub('\D', "", phone);
print (num);

def double(matched):
	value = int(matched.group('value'));
	return str(value * 2);

s = 'A23Fsd45654';
print (re.sub('(?P<value>\d+)', double, s));

print(re.match('www','www.afeeling.site'));
print(re.match('site','ww.afeeling.site'));
