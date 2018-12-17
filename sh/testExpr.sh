#!/bin/bash
#test sth about str operation

#get the length of string
str="abcdef"
##echo length $str
expr length $str   # 4
echo ${#str}       # 4
expr "$str" : ".*" # 4

#get the index of the character in the string
str="abcdef"
expr index $str "a"  # 1
expr index $str "b"  # 2
expr index $str "x"  # 0
expr index $str ""   # 0

#get the appoint part of the string  
str="abcdef"
expr substr "$str" 1 3  # 从第一个位置开始取3个字符， abc
expr substr "$str" 2 5  # 从第二个位置开始取5个字符， bcdef 
expr substr "$str" 4 5  # 从第四个位置开始取5个字符， def
 
#get appoint string from string
echo ${str:2}           # 从第二个位置开始提取字符串， bcdef
echo ${str:2:3}         # 从第二个位置开始提取3个字符, bcd
echo ${str:(-6):5}        # 从倒数第二个位置向左提取字符串, abcde
echo ${str:(-4):3}      # 从倒数第二个位置向左提取6个字符, cde

#get part of string from left
str="abbc,def,ghi,abcjkl"
echo ${str#a*c}     # 输出,def,ghi,abcjkl  一个井号(#) 表示从左边截取掉最短的匹配 (这里把abbc字串去掉）
echo ${str##a*c}    # 输出jkl，             两个井号(##) 表示从左边截取掉最长的匹配 (这里把abbc,def,ghi,abc字串去掉)
echo ${str#"a*c"}   # 输出abbc,def,ghi,abcjkl 因为str中没有"a*c"子串
echo ${str##"a*c"}  # 输出abbc,def,ghi,abcjkl 同理
echo ${str#*a*c*}   # 空
echo ${str##*a*c*}  # 空
echo ${str#d*f}     # 输出abbc,def,ghi,abcjkl, 
echo ${str#*d*f}    # 输出,ghi,abcjkl   

# get part of string from right
echo ${str%a*l}     # abbc,def,ghi  一个百分号(%)表示从右边截取最短的匹配 
echo ${str%%b*l}    # a             两个百分号表示(%%)表示从右边截取最长的匹配
echo ${str%a*c}     # abbc,def,ghi,abcjkl

# replase part of string
str="apple, tree, apple tree"
echo ${str/apple/APPLE}   # 替换第一次出现的apple
echo ${str//apple/APPLE}  # 替换所有apple
 
echo ${str/#apple/APPLE}  # 如果字符串str以apple开头，则用APPLE替换它
echo ${str/%apple/APPLE}  # 如果字符串str以apple结尾，则用APPLE替换它


s1="hello"
s2="world"
echo ${s1}${s2}   # 当然这样写 $s1$s2 也行，但最好加上大括号
[ "a.txt" == a* ]        # 逻辑真 (pattern matching)
[[ "a.txt" =~ .*\.txt ]]   # 逻辑真 (regex matching)
[[ "abc" == "abc" ]]       # 逻辑真 (string comparision) 
[[ "11" < "2" ]]           # 逻辑真 (string comparision), 按ascii值比较
