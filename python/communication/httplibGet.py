#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
try:
    import httplib
except ImportError as e:
    import http.client as httplib
conn = None

try:
    conn = httplib.HTTPConnection("www.zhihu.com");
    conn.request("GET", "/");
    response = conn.getresponse();
    print(response.status, response.reason);
    print ('-' * 40);
    
    headers = response.getheaders();
    for h in headers:
        print(h)
    print('_' * 40);
    
    print(response.msg)
except Exception as e:
    print (e);
finally:
    if conn:
        conn.close();
