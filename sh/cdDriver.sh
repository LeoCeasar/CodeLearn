#!/bin/bash
#a shell do with controal cdDriver 

read -p "How many times do you want to exec:" n
if [[ $n -eq 0 ]] || [ -z $n ] || [ ! -n $n ] ;
then
    echo "Can not be zero ..."
    exit 0
fi

read -p "How long times do you want to sleep:" time
if [[ $time -eq 0 ]] || [ -z $n ] || [ ! -n $n ];
then
    echo "Can not be zero ..."
    exit 0
fi

for((i=0;i<$n;i++));
do
   eject             # 让光驱弹出
   sleep $time
   eject -t          # 让光驱合上
done
