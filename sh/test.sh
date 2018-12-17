seq 10 >file
while read a
do
echo $a
dd &>/dev/null
done <file

