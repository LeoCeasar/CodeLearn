#!/bin/bash

set -x       

ipcs -m | awk '$3=="root" {print $2}' |
while read s
do
    ipcrm -m $s
done
