#!/bin/bash


function swap()
{
  tmpfile=$(mktemp $(dirname "$1")/XXXXXX)
  mv "$1" "$tmpfile" && mv "$2" "$1" &&  mv "$tmpfile" "$2"
}

swap /home/bbs/unknown_jobs/web/Makefile /home/bbs/unknown_jobs/web/Makefile.bak

swap /home/bbs/unknown_jobs/db/Makefile /home/bbs/unknown_jobs/db/Makefile.bak

swap /home/bbs/unknown_jobs/logic/Makefile /home/bbs/unknown_jobs/logic/Makefile.bak

