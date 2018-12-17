#!/bin/sh 
# vim: set sw=4 ts=4 et: 
ver="0.1" 

help() 
{ 
cat < . 
rotatefile -- rotate the file name 

USAGE: rotatefile [-h] filename 

OPTIONS: -h help text 
EXAMPLE: rotatefile out 
This will e.g rename out.2 to out.3, out.1 to out.2, out to out.1 
and create an empty out-file 
The max number is 10 
version $ver 
HELP 
	exit 0 
}

help
