#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import optparse
import configparser
import sys
 
from optparse import OptionParser

config = configparser.ConfigParser()
config.read("./config.ini")

# 一个帮助文档解释字符串
hstr = '%prog ' + config['system']['version'] + ' custom help string'
parser = OptionParser(hstr, description='custom description', version='%prog '+config['system']['version'])
#通过OptionParser类创建parser实例,初始参数usage中的%prog等同于os.path.basename(sys.argv[0]),即
#你当前所运行的脚本的名字，version参数用来显示当前脚本的版本。
'''
添加参数，-f、--file是长短options，有一即可。
dest='user' 将该用户输入的参数保存到变量user中，可以通过options.user方式来获取该值
action用来表示将option后面的值如何处理，比如:
XXX.py -f test.txt
经过parser.parse_args()处理后,则将test.txt这个值存储进-f所代表的一个对象，即定义-f中的dest
即option.filename = 'test.txt'
action的常用选项还有store_true,store_false等，这两个通常在布尔值的选项中使用。
 
 metavar仅在显示帮助中有用，如在显示帮助时会有：
 -f FILE, --filename=FILE    write output to FILE
 -m MODE, --mode=MODE  interaction mode: novice, intermediate, or expert
                         [default: intermediate]
如果-f这一项没有metavr参数，则在上面会显示为-f FILENAME --filename=FILENAME,即会显示dest的值
 
 defalut是某一选项的默认值，当调用脚本时，参数没有指定值时，即采用default的默认值。
 '''
"""
add_option(…):
 
    add_option 方法中前面的参数为命令的选项, 可以为等价的短名或者长名,一般是前面为短名,后面为长名.
 
可以配置的参数有以下:
    dest: 可以决定解析后,取值时的属性名, 尤其适于有多个等价参数. 不指定时就是选项不加-的字符串.
    type: 选项的值类型,值的默认类型是字符串, 这里将值指定为其他类型.
    default: 缺省值. 没有设置缺省值的为None.
    help: 选项中有 -h 时打印的 help 信息.
    metavar: 表示显示到 help 中选项的默认值；
    choices: 当 type 设置为 choices 时,需要设置此值.
    const: 指定一个常量值给选项, 该常量值将用于后面store_const和append_const,一起合用.
    action: 用于控制对选项和参数的处理,像无参数选项处理,可以设置为以下几种字符串:
        "store": 储存值到 dest 指定的属性,强制要求后面提供参数;
        "store_true": 当使用该选项时,后面的 dest 将设置为 true, 不跟参数.
        "store_false": 当使用该选项时,后面的 dest 将设置为 false. 常配合另一个 "store_true" 的选项使用同一个 dest 时使用. 不跟参数.
        "append": 储存值到 dest 指定的属性,并且是以数组的形式, 必须跟参数.
        "store_const": 用来存储参数为 const 设置的值到 dest 指定的属性当中.常用于 dest 为同名2个以上选项时的处理. 不跟参数.
        "append_const": 用来存储参数为 const 设置的数组到 dest 指定的属性当中. 不跟参数.
        "count": 使用后将给储存值到 dest 指定的属性值加1,可以统计参数中出现次数.用途不大. 不跟参数.
        "callback": 后面指定回调函数名(不加括号),会将相应opt和args传给回调函数.
        "help", "version": 对应为帮助和版本. 要另外自己设计时使用.
 
    当 action 设置为 store_ture / store_false 时, 解析参数时, 如果有值时为 Ture / False, 没有值时为 None.
    当 dest 相同时, 一个 action 设置为 store_false, 另一个 action 设置为 store_ture 时, 解析参数时,以在后面出现的为准.
 
"""
parser.add_option('-i', '--input', action='store', dest='input', help='read input data from input file')
parser.add_option('-o', '--output', action='store', dest='output', help='write data to output file')
parser.add_option('-q', '--quite', action='store_false', dest='version', help='don\'t print the version')
# parser.add_option('-v', '--version', action='store_true', dest='version', default=False, help='print the version')
# parser.add_option('-v', '--version', action='store_true', dest='version', help='print the version')
 
parser.add_option('-f', '--file', action='store', dest='file', help='file to handle')
parser.add_option('-a', '--add', action='append', dest='add', help='add to handle')
parser.add_option('-c', '--count', action='count', dest='count', help='count to handle')
parser.add_option('-d', '--count1', action='count', dest='count', help='count1 to handle')
 
#parser.add_option('-v', '--version', dest='version')
 
if parser.has_option('-f'):
    print('content -f') # parser.set_default('-f', 'myFile')
    parser.remove_option('-f')
if not parser.has_option('-f'):
    print('do not content -f')
# 用一个数组模拟命令参数
#testArgs = ['-i', 'someForInput', '-f', 'someForFile', '-vq', '-a', 'test1 test2 test3', '-c', '-d']
testArgs = [ '-i', 'someForInput', 'someForFile', 'someForFile1', '-q', '-a', 'test1 test2 test3', '-c', '-d', '-h']
options, args = parser.parse_args(sys.argv[1:])
#options, args = parser.parse_args(testArgs[0:])
print('options : %s' % options)
print('args : %s' % args)
print('test for 1');
 
if options.input:
    print('input in args : %s' % options.input)
if options.version:
    print('version 1.0.0')
 
# if options.file:
# print('file in args : %s' % options.file)
if options.add:
    print('add in args : %s' % options.add)
 
print('version in args', options.version)
