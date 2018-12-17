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
expr substr "$str" 1 3  # �ӵ�һ��λ�ÿ�ʼȡ3���ַ��� abc
expr substr "$str" 2 5  # �ӵڶ���λ�ÿ�ʼȡ5���ַ��� bcdef 
expr substr "$str" 4 5  # �ӵ��ĸ�λ�ÿ�ʼȡ5���ַ��� def
 
#get appoint string from string
echo ${str:2}           # �ӵڶ���λ�ÿ�ʼ��ȡ�ַ����� bcdef
echo ${str:2:3}         # �ӵڶ���λ�ÿ�ʼ��ȡ3���ַ�, bcd
echo ${str:(-6):5}        # �ӵ����ڶ���λ��������ȡ�ַ���, abcde
echo ${str:(-4):3}      # �ӵ����ڶ���λ��������ȡ6���ַ�, cde

#get part of string from left
str="abbc,def,ghi,abcjkl"
echo ${str#a*c}     # ���,def,ghi,abcjkl  һ������(#) ��ʾ����߽�ȡ����̵�ƥ�� (�����abbc�ִ�ȥ����
echo ${str##a*c}    # ���jkl��             ��������(##) ��ʾ����߽�ȡ�����ƥ�� (�����abbc,def,ghi,abc�ִ�ȥ��)
echo ${str#"a*c"}   # ���abbc,def,ghi,abcjkl ��Ϊstr��û��"a*c"�Ӵ�
echo ${str##"a*c"}  # ���abbc,def,ghi,abcjkl ͬ��
echo ${str#*a*c*}   # ��
echo ${str##*a*c*}  # ��
echo ${str#d*f}     # ���abbc,def,ghi,abcjkl, 
echo ${str#*d*f}    # ���,ghi,abcjkl   

# get part of string from right
echo ${str%a*l}     # abbc,def,ghi  һ���ٷֺ�(%)��ʾ���ұ߽�ȡ��̵�ƥ�� 
echo ${str%%b*l}    # a             �����ٷֺű�ʾ(%%)��ʾ���ұ߽�ȡ���ƥ��
echo ${str%a*c}     # abbc,def,ghi,abcjkl

# replase part of string
str="apple, tree, apple tree"
echo ${str/apple/APPLE}   # �滻��һ�γ��ֵ�apple
echo ${str//apple/APPLE}  # �滻����apple
 
echo ${str/#apple/APPLE}  # ����ַ���str��apple��ͷ������APPLE�滻��
echo ${str/%apple/APPLE}  # ����ַ���str��apple��β������APPLE�滻��


s1="hello"
s2="world"
echo ${s1}${s2}   # ��Ȼ����д $s1$s2 Ҳ�У�����ü��ϴ�����
[ "a.txt" == a* ]        # �߼��� (pattern matching)
[[ "a.txt" =~ .*\.txt ]]   # �߼��� (regex matching)
[[ "abc" == "abc" ]]       # �߼��� (string comparision) 
[[ "11" < "2" ]]           # �߼��� (string comparision), ��asciiֵ�Ƚ�
