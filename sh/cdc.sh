#!/bin/sh
#关于正则表达式的匹配问题
if test -z "$1";then
    echo "error parament";
    return 
elif [[ "$1" =~ ^s\w*$ ]];then
    dir="spider.py"
elif [[ "$1" =~ ^S\w*$ ]];then
    dir="SpiderBook"
else
    dir="CodeLearn"
fi
echo $dir

allPath="/home/Dr/coder/"${dir}

cd ${allPath}
