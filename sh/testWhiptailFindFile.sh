#!/bin/bash

FindFile()
{
	FindDIR= $(whiptail --title "�ļ�����" --inputbox "��������ļ�·��" 1060 /home/test/ 3>&1 1>&2 2>&3 )
	FindName= $(whiptail --title "�ļ�����" --inputbox "��������ļ�����" 1060 3>&1 1>&2 2>&3 )

	if [ -n $FindName ];
	then
		F= $(find $FindDIR -name "*$FindName*" -print)
		N= $(find $FindDIR -name "*$FindName*" |wc-l)
		whiptail --title "���ҽ��$N����¼" --yes-button "��������" --no-button "�˳�����" --yesno "$F" 00
	fi
}

#"$F"00������0�������Ƹ߶ȺͿ������������Ľ�������������������1560�Ļ���ľͲ���ʾ����
#0����1�˳�����
#����ѭ��($?��һ������ִ�е�ֵ1/0)
while [ "$?" -ne 1 ]
do
	FindFile
done
