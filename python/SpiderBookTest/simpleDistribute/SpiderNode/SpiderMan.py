#!/usr/bin/python3
#coding:utf-8

from multiprocessing.managers import BaseManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser

class SpiderMan(object):

    def __init__(self):
        '''
        初始化分布式进程中工作节点的链接工作
        '''
        #第一步 使用BaseManager注册用于获取Queue的方法
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')

        #连接到服务器
        server_addr = '127.0.0.1';
        print('Connect to server %s ...' % server_addr)

        self.m = BaseManager(address=(server_addr, 8001), authkey='baike'.encode('utf-8'));
        self.m.connect();

        self.task = self.m.get_task_queue();
        self.result = self.m.get_result_queue()

        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        print('init finished');

    def crawl(self):
        while(True):
            try:
                if not self.task.empty():
                    url = self.task.get();
            
                    if url == 'end':
                        print('控制节点通知爬虫节点停止工作。。。')
                        #接着通知其他节点停止工作
                        self.result.put({'new_urls':'end', 'data':'end'})
                        return
                      
                    print('爬虫节点正在解析%s' %url.encode('utf-8'))
                    
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result.put({"new_urls":new_urls, "data":data})
            except EOFError as e :  
                print('连接控制节点失败')
                return
            except Exception as e:
                print("crawl failed")
                print(e)
                return
            #数据存储器将文件输出成指定格式

if __name__=="__main__":
    spider_man = SpiderMan()
    spider_man.crawl()
