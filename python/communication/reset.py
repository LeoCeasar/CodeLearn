#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
try:
    import urllib2;
except ImportError as e:
    import urllib.request as urllib2;

import ssl
ssl._create_default_https_context = ssl._create_unverified_context;


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req,  fp, code, msg, headers);
        result.status  = code;
        result.newurl = result.geturl();
        print(result)
        return result;

url = "http://www.zhihu.com";

response = urllib2.urlopen(url) 
isRedirected = response.geturl() == url;
if not isRedirected:
    print('reset to %s' % response.geturl());
else:
    print('not resite');

opener = urllib2.build_opener(RedirectHandler);
opener.open(url);
#print(opener.geturl())
