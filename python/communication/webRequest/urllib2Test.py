#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
#import urllib2
import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context;

request = urllib.request.Request('http://www.zhihu.com');
response = urllib.request.urlopen(request);
html = response.read();

'''
url = 'www.zhihu.com';
postData = {'username':'qiye','password':'qiye_pass'};
req = urllib.request.Request(url. data);
response = urllib.request.urlopen(req);
html = response.read();
'''
print(html);



