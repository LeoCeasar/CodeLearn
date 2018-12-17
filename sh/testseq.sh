seq 100 | grep -v "7" | awk '$0%7!=0{print}'
