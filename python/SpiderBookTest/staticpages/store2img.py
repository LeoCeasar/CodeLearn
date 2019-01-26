#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import urllib.request as urllib
from lxml import etree
import requests

def Schedule(blocknum ,blocksize ,totalsize):
    '''
    blocknum:已经下载的数据块
    blocksize:数据块的大小
    totalsize:远程的文件大小
    '''
    per = 100.0 * blocknum * blocksize / totalsize;
    
    if per > 100:
        per = 100;
    
    print('当前下载进度: %d ' % per)
user_agent = 'Mozilla/4.0 (compatible; MSIZE 5.5; Wiondows NT)'
headers = {'User-Agent': user_agent};
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers = headers);

html = etree.HTML(r.text);
img_urls = html.xpath('.//img/@src')
i = 0;
for img_url in img_urls:
    urllib.urlretrieve(img_url, './img/img'+str(i)+'.jpg',Schedule)
    i += 1
