#!/usr/bin/python3
#coding=utf_8


import sys
import os
import stat
from optparse import *

def creFile(path, mod):
	bRet = False;
	if os.path.exists(path):
		print("the file " + path + " is already exists")
	else:
		fo = open(path, "w");
		fo.write(strTmp);
		fo.close();

        #赋予执行权限
		#os.chmod(options.path, stat.S_IRWXU | stat.S_IXOTH | stat.S_IXGRP)
		os.chmod(path, mod);
		#os.chmod(options.path, 0o755);
		#这里如果不加0o的话默认是十进制，会进>行转换为八进制，所以需要在前面加0o
		#os.system('chmod 755 ' + options.path) #linux	
		bRet = True;
	return bRet;


versionStr = '1.0.0.1';

hstr = ' make file for python and open it with vim';
descriptionStr = "which can reduce the time for edit a file of python and write the first two lines in it every time";

parser = OptionParser(hstr, description=descriptionStr, version=versionStr);

parser.add_option('-m', '--make', action='store', dest='path', help='input your file name');
parser.add_option('-e', '--edit', action='store_true', dest='edit', help='if you want to edit it, then add it.if you dont want to edit the file what you make you just want to make it,then do not add this option');


#options, args = parser.parse_args(sys.argv[1:0]);
options, args = parser.parse_args();

#如果后面不添加一个空格则无法在后面空出一行空白行
strTmp = "#!/usr/bin/python3\r\n# _*_ coding: utf-8 _*_\r\n \r\n ";

if options.path:
		if creFile(options.path, 0o755):
			if options.edit:
				os.system('vim ' + options.path +' +4');#跳到指定行数
		else:
			pass;
else :
	if len(args)==1:
		if creFile(args[0], 0o755):
			if options.edit:
				os.system('vim ' + args[0] +' +4');#跳到指定行数
			else:
				pass;
		else:
			pass;
	else:
		parser.print_help();
