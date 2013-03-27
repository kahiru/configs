#!/bin/bash
export BROWSER=firefox
export EDITOR=vim

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

case $1 in
xfce4)
	export DE=xfce &
	exec dbus-launch startxfce4
	;;
subtle)
	exec nm-applet &
	exec volumeicon &
	exec subtle
	;;
i3)
	exec xbindkeys &
	exec uim-toolbar-gtk-systray &
	exec clipit -d -n &
	exec dunst &
	exec xset dpms 300 600 900 &
	exec nm-applet &
	exec volumeicon &
	exec nitrogen --restore &
	exec mpdscribble &
	exec i3
	;;
openbox)
	exec xbindkeys &
	exec uim-toolbar-gtk-systray &
	exec clipit -d -n &
	exec dunst &
	exec xset dpms 300 600 900 &
	exec nm-applet &
	exec volumeicon &
	exec nitrogen --restore &
	exec tint2 &
	exec openbox
	;;
KDE)
	nitrogen --restore &
	exec startkde
	;;
*)
	exec dbus-launch startxfce4
	;;
esac
