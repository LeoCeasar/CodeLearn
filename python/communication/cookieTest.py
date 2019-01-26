#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
'''
in Python2:

import cookielib

in Python3:

import http.cookiejar
'''
import urllib;
try:
    import cookielib;
except ImportError as e:
    import http.cookiejar as cookielib;

import ssl
ssl._create_default_https_context = ssl._create_unverified_context;

#url = "www.zhihu.com"
url = "http://www.zhihu.com"

cookie = cookielib.CookieJar()
openerC = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie));
responseC = openerC.open(url)

i = 0;

for item in cookie:
    i += 1;
    print('\n')
    print(str(i) + item.name + ':' + item.value)


opener = urllib.request.build_opener();
email = "1111@qq.com";
opener.addheaders.append( ('Cookie', 'email='+ email) ) 

req = urllib.request.Request(url);
response = opener.open(req);

print('\n')
print('\n')
print('\n')
print('\n')
print(response.headers)
retdata = response.read();
print('\n')
print(retdata);
