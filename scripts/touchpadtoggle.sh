#!/bin/bash
#from /usr/bin/
if [ `synclient | grep Touchpad | grep -o [0-9]` == 0 ]; then
    synclient TouchpadOff=1
    notify-send Touchpad Off
else
    synclient TouchpadOff=0
    notify-send Touchpad On
fi

