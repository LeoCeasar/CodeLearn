#!/bin/sh
#因为这是shell脚本原先想实现的目的是通过cd 命令行在终端进行目录的切换，但是好像不能输出， 所以添加一个命令 alias mkcd=". ./mkcd.sh" 然后在终端使用mkcd可以达到目的

if test -z "$1";
then
    echo "error command"
    exit 0
fi
mkdir $1
cd $1
