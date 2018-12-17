#!/bin/sh
#用于指定shell脚本使用的何种解析器进行解析
##当出错之后不会自动执行接下来的操作
#############/////////#!/bin/bash//会自动执行接下来的步骤
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

