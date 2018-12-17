#!/usr/bin/python
#coding=utf_8

import re;
import os;
import time;

#str.split(string) 分割字符串
##'连接符'.join(list) 将列表组成字符串
def changePicName(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        print(path, 'not real path');
        return False;
    elif os.path.isfile(path):
        filePath=os.path.split(path);
        lists = filePath[1].split('.');
        fileExt = lists[-1];
        imgExt = ['bmp','jpeg','gif','psd','png','jpg'];
        if fileExt in imgExt:
            #os.rename(path, filePath[0]+'/'+lists[0]+ '_fc.'+ fileExt);
            i+=1;
            #或者

            #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        
            #if file_ext in img_ext:

            print('ok---'+fileExt)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            changePicName(os.path.join(path,x)) #os.path.join()在路径处理上很有用

imgDir = '\\home\\D.r\\python\\test\\img';
imgDir = imgDir.replace('\\','/')
start = time.time()
i = 0
changePicName(imgDir);

c = time.time() - start

print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))


