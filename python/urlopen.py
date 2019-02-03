#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys
import ssl

if sys.version_info[0] ==3:
    from urllib.request import urlopen,Request
else:
    from urllib import urlopen,Request

ssl._create_default_https_context = ssl._create_unverified_context

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = "http://www.baidu.com"

req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
print(urlopen(req).read())

