#!/bin/sh

if test -z "$1";
then
    echo "error command"
    exit 0
fi
echo `mkdir $1`

echo `cd "./"$1`
