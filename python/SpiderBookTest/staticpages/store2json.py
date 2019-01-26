#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import json
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)' 
headers = {'User-Ageny':user_agent}

r = requests.get('http://seputu.com', headers=headers)

#print(r.text);

soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
#html.parser

content=[];
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        list=[];
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href');
            box_title = a.get('title');
            #print (href, box_title)

            list.append({'href':href,'box_title':box_title})

        content.append({'title':h2_title,'content':list});

#print(content);
with open('test.json','w') as fp:
    json.dump(content, fp=fp, indent=4);

from lxml import etree
import re

html = etree.HTML(r.text)
rows=[]
div_mulus = html.xpath('.// *[@class="mulu"]');
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2 )> 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0].encode('utf-8')
            #print(href,box_title)
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)');
            match = pattern.search(box_title);
            if match!=None:
                date = match.group(1);
                real_title = match.group(2);

headers=['title', 'real_title', 'href', 'date'];
with open("test.csv", 'w') as f :
    f_csv = csv.writer(f,)
    f_csv.writerow(headers);
    f_csv.writerows(rows)
