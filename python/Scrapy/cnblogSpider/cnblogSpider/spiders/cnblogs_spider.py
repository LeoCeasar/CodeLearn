#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import scrapy
from scrapy import Selector

class CnblogsSpider(scrapy.Spider):
    name = "cnBlogs";
    allowed_domains = ["cnblogs.com"]
    start_urls = [
            "http://www.cnblogs.com/qiyeboy/default.html?page=1"
            ]

    def parse(self, response):
        papers = response.xpath(".// *[@class='day']")

        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]

            #print (url, title, time, content);
            item = CnblogsSpider(url = url, title = title, time = time, content = content)
            yield item

        next_page = Selector(response = response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url = next_page[0], callback = self.parse);
