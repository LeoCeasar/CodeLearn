#########################################################################
#    File Name: mycowsay.sh
#       Author: huangjinqiang
#        Email: ligelaige@gmail.com
# Created Time: 2014年04月28日 星期一 18时41分33秒
#########################################################################
#!/bin/bash

CMD=cowsay
say=$1
$CMD "Hello, "$say
#$CMD "Hello, Jinqiang!"
if [ $? -ne 0 ];then
    echo "please enter following command to install"
    echo "sudo apt-get install $CMD"
    echo "or"
    echo "sudo aptitude install $CMD"
    exit
fi
#dir=/usr/share/cowsay/cows/
dir=/usr/share/cowsay/
for filename in `ls $dir`
do
    if [ $# -eq 0 ];then
        read key
    fi
    if [ "$key" = "" ];then
        key="Hello, " $say
    fi
    name=${filename%".cow"}    
    $CMD -f $name $key
done
