#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
export PATH=$PATH:~/Scripts
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

#~ ALIASES

alias rtorrent='dtach -A /tmp/rtorrent rtorrent'
alias pacman='sudo pacman-color'
alias rsync='rsync -r -u -h --progress'
alias scp='scp -r'

#~ /ALIASES