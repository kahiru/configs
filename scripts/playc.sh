#!/bin/bash
#from /usr/bin/
case $1 in
'prev')
    ncmpcpp prev
    ;;
'play')
    ncmpcpp toggle
    ;;
'next')
    ncmpcpp next
    ;;
*)
    exit 0
    ;;
esac
