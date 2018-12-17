#!/bin/bash
echo "the number of parameter are ====>$#";
echo "the name of this program is ====>$0";
echo "tha all parameters are ====>$@"

parameters="$@";

count=0;

for var in $parameters
do
    echo "The $count value        ==>$var";
    let count++;
done    
