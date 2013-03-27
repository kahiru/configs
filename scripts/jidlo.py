# coding=UTF-8
import urllib
import re
import sys
link=str()
if len(sys.argv)==1:
	link='http://www.kam.vutbr.cz/?p=jide'
	link=urllib.urlopen(link)
	obsah=link.read()
	patt=re.compile('a name="menza.*?\)')
	vysledky=re.findall(patt,obsah)
	num=1
	seznam=list()
	for each in vysledky:
		provoz=re.search('provoz=([0-9]{2})',each).group(1)
		odoba=re.search('\(([0-9]+:[0-9]+).*?([0-9]+:[0-9]+)',each).group(1)
		zdoba=re.search('\(([0-9]+:[0-9]+).*?([0-9]+:[0-9]+)',each).group(2)
		each=re.search('\?p=(.*?)<',each).group(1)
		each=re.sub('menu&provoz=[0-9]{2}.*?>','',each)
		if each=='Seznam jídel':
			continue
		print(str(num)+'\t'+odoba+' - '+zdoba+'\t'+each)
		seznam.append((each,provoz,(odoba,zdoba)))
		num+=1
	while True:
		try:
			x=int(raw_input('> '))
			if (x>len(seznam)) or (x<0):
				print('Out of range.')
				continue
			break
		except ValueError:
			print('Not a number.')
	if x==0:
		sys.exit(0)
else:
	x=int(sys.argv[1])
link=urllib.urlopen('http://www.kam.vutbr.cz/?p=menu&provoz='+seznam[x-1][1])
obsah=link.read()
vysledek=re.findall('<tr id.*?</tr>',obsah)
print('---------------------------------------------')
if len(vysledek)==0:
	print('Provoz je zavreny.')
	exit
for each in vysledek:
	temp=re.findall('<td.*?</td>',each)
	try:
		vaha=re.search('>([0-9]+)',temp[0]).group(1)+'g'
	except AttributeError:
		vaha=''
	nazev=re.search('>(.*?)<',temp[1]).group(1)
	cena=re.search('>([0-9]+)',temp[2]).group(1)
	print(vaha+'\t'+cena+',-\t'+nazev)
print
