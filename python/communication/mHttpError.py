#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import urllib
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context;

url = 'http://www.google.com';
try:
    response = urllib.request.urlopen(url) 
    data = response.read();
    #print(response);
    print(data);
except urllib.HTTPError as e:
    if hasattr(e, 'code'):
        print('Error code :', e.code)
