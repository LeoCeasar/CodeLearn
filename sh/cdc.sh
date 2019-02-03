#!/bin/sh
#关于正则表达式的匹配问题
if test -z "$1";then
    echo "error parament";
    return 
elif [[ "$1" =~ ^s[a-zA-Z0-9_]*$ ]];then
    dir="spider.py"
elif [[ "$1" =~ ^S[a-zA-Z0-9_]*$ ]];then
    dir="gitHub/SpiderBook"
elif [[ "$1" =~ ^(g)(.*)$ ]];then
    dir="gitHub/"
else
    dir="CodeLearn"
fi
echo $dir

allPath="/home/Dr/coder/"${dir}

cd ${allPath}
