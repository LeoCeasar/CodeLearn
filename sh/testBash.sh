#!/bin/bash

echo "$SHELL";
if [ "$SHELL" -eq "/bin/bash" ]
then 
  echo "your login shell is the bash (bourne again shell)"
else 
  echo "your login shell is not bash but $SHELL"
fi 
