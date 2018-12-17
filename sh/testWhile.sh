#!/bin/bash

# 显示一系列数字

#while [ $count -le 6 ]; do
#    echo $count
#    count=$((count + 1))
#done
#echo "finished"

while :;
do
	read -p '>' p
	
	if [ x"$p" = x  ]
	then
		continue
	elif [ $p = "exit" ]
	then
		exit 0;
	fi
	
	echo ">$p"
done
