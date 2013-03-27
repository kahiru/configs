
#! /usr/bin/env python2
import os
import re
import sys
import string
def main(pattern='',replacement=''):
	ncolor='\033[00m'
	color='\033[00;32m'
	patt=unicode()
	replacement=unicode()
	if len(sys.argv)!=1:
		patt=sys.argv[1]
		if len(sys.argv) == 3:
			replacement =sys.argv[2]
		else:
			replacement=raw_input('Replace with: ')
	else:
		patt=raw_input(ncolor+'Pattern to replace: '+color)
		replacement=raw_input(ncolor+'Replace with: '+color)
	sobory=os.listdir(os.getcwd())
	patt=re.compile(patt)
	renamed=list()
	for file in sobory:
		renamed.append(re.sub(patt,color+replacement+ncolor,file))
	num=0
	tprint=False
	for file in renamed:
		if file != sobory[num]:
			print(ncolor+string.replace(sobory[num],re.search(patt,sobory[num]).group(0),color+re.search(patt,sobory[num]).group(0)+ncolor))
			print(color+'-> '+ncolor+re.sub(patt,color+replacement+ncolor,sobory[num])+ncolor)
			tprint=True
		num=num+1
	if tprint:
		if __name__!='__main__':
			res=list()
			res.append(sobory)
			res.append(renamed)
			return res
		ok=raw_input(ncolor+'Does this look ok? [y/N] '+color)
		if ok=='n' or ok=='N':
			print(ncolor)
			exit()
		elif ok=='y' or ok=='Y':
			num=0
			for file in sobory:
				if file != renamed[num]:
					os.rename(file, renamed[num])
				num=num+1
			for each in os.listdir(os.getcwd()):
				print(color+each+ncolor)
		else:
			print('No matches found in current directory.')
	print(ncolor)
	
if __name__=='__main__':
	main()
