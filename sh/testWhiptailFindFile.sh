#!/bin/bash

FindFile()
{
	FindDIR= $(whiptail --title "文件查找" --inputbox "输入查找文件路径" 1060 /home/test/ 3>&1 1>&2 2>&3 )
	FindName= $(whiptail --title "文件查找" --inputbox "输入查找文件名称" 1060 3>&1 1>&2 2>&3 )

	if [ -n $FindName ];
	then
		F= $(find $FindDIR -name "*$FindName*" -print)
		N= $(find $FindDIR -name "*$FindName*" |wc-l)
		whiptail --title "查找结果$N条记录" --yes-button "继续查找" --no-button "退出查找" --yesno "$F" 00
	fi
}

#"$F"00这两个0代表不限制高度和宽带这样输出来的结果可以有下拉栏，如果1560的话多的就不显示出来
#0继续1退出查找
#做个循环($?上一条命令执行的值1/0)
while [ "$?" -ne 1 ]
do
	FindFile
done
