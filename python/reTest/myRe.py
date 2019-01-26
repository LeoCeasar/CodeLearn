#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import re;

pattern = re.compile(r'\d+');

result1 = re.match(pattern, '192abc')

if result1:
    print(result1.group());
else:
    print ('fetch error of result 2');

result2 = re.match(pattern, 'abc192')
if result2:
    print(result2.group());

else:
    print ("fetch error of result 2")
