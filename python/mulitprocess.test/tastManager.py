#!/usr/bin/python3
#coding:utf-8
#服务进程(taskManager.py)(linux版)
import random,time,queue
from multiprocessing.managers import BaseManager
#实现第一步：建立task_queue和result_queue，用来存放任务和结果
task_queue=queue.Queue()
result_queue=queue.Queue()

class Queuemanager(BaseManager):
    pass
# 将Queue对象在网络中暴露
Queuemanager.register('get_task_queue',callable=lambda:task_queue)
Queuemanager.register('get_result_queue',callable=lambda:result_queue)

#实现第三步：绑定端口8001，设置验证口令‘qiye’。这个相当于对象的初始化
key = 'qiye';
manager=Queuemanager(address=('',8001),authkey=key.encode('utf-8'))

#实现第四步：启动管理，监听信息通道
manager.start()

#实现第五步：通过管理实例的方法获得通过网络访问的Queue对象
task=manager.get_task_queue()
result=manager.get_result_queue()


#实现第六步：添加任务
for url in ["ImageUrl_"+str(i) for i in range(10)]:
    print('put task %s ...' %url)
    task.put(url)
#获取返回结果
print('try get result...')
for i in range(10):
    print('result is %s' %result.get(timeout=10))
#关闭管理
manager.shutdown()

 
