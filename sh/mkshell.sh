#!/bin/sh
#����ָ��shell�ű�ʹ�õĺ��ֽ��������н���
##������֮�󲻻��Զ�ִ�н������Ĳ���
#############/////////#!/bin/bash//���Զ�ִ�н������Ĳ���
help()
{
echo "--mkshell.sh [filename]
--help help text"
	exit 0
}


if [ $# != 1 ] || [ $1 = "--help" ]
then 
	help
fi
	

FileName=$1;

echo "#!/bin/bash" > $FileName;

chmod 755 $FileName;

