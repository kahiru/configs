#!/bin/python

import urllib
import re
import os
nazev=raw_input('Manga name: ')
temp=''
print '--------------------'
for pismeno in nazev:
	if pismeno==' ':
		pismeno='+'
	temp=temp+pismeno
nazev=temp
url='http://mangable.com/search/?series_name='+nazev+'&submit=Search'
link=urllib.urlopen(url)
stranka=link.read()
x=re.compile('<ul id="comprehensive_list">((.|\n)*?)</ul>')
y=re.compile('<a href=(.*?)</a>')
blok=re.findall(x, stranka)
vsechny=re.findall(y,blok[0][0])
if len(vsechny)==1:
	print 'Nothing found.'
	print '--------------------'
	exit()
counter=0

for each in vsechny:
	if counter%2==0:
		mname=[each.split('>')[1],each.split('"')[1]]
		if each.split('"')[3]=='complete':
			num=str((counter/2)+1)+': *\t'
		else:
			num=str((counter/2)+1)+': +\t'
		print num+mname[0]

	if counter%2==1:
		lastchap=each.split('>')[1]
		print '\t'+lastchap+'\n'
	counter+=1
tdl=int(raw_input('Manga ID: '))
tdl=(tdl-1)*2
manganame=vsechny[tdl].split('>')[1]
manga=vsechny[tdl].split('"')[1]
base='http://mangable.com'
imgpref=base+'/files/images'+manga
manganame=manganame.strip()
if not os.path.exists(manganame):
	os.makedirs(manganame)
os.chdir(manganame)
link=urllib.urlopen(base+manga)
stranka=link.read()
x=re.compile('<div id="newlist">((.|\n)*?)</div>') 
vsechny=re.findall(x,stranka)
z=re.compile('<b>(.*?)</b>')
chapters=re.findall(z,vsechny[0][0])
maxchap=int(chapters[0].split(manganame)[1])
print str(maxchap)+' chapters of '+manganame+' available.'
temp=raw_input('Download all? [Y/n]').strip()
dlfrom=1
dlto=int(maxchap)
if temp=='n' or temp=='N':
	dlfrom=int(raw_input('Download from chapter: '))
	dlto=int(raw_input('Download to chapter: '))+1
print '--------------------'
for i in range(dlfrom, dlto):
	url=base+manga+'chapter-'+str(i)+'/'
	chapter=urllib.urlopen(url)
	chapter=chapter.read()
	header=re.compile('<ul id="breadcrumbs">((.|\n)*?)</ul>')
	chapname=re.findall(header,chapter)[0][0]
	headerli=re.compile('<li>(.*?)</li>')
	chapname=re.findall(headerli, chapname)[2].split(manganame)[1].split('</li>')[0].strip()
	if not os.path.exists(chapname):
		os.makedirs(chapname)
	os.chdir(chapname)
	repages=re.compile('<select id="select_chapter"((.|\n)*?)</select>')
	rempage=re.compile('option value="(.*?)"')
	#mpages=int(re.findall(rempage,re.findall(repages,chapter)[0][0])[0].split('"')[1])
	pages=re.findall(repages,chapter)[0][0]
	pages=re.findall(rempage,pages)[0].split('"')[0].strip()
	mpages=int(pages)
	print chapname+':'
	for f in range(1,mpages):
		if os.path.isfile('{0:02}.jpg'.format(f)):
			print 'Skip {0:02}/{1}'.format(f,mpages-1)
			continue
		of=open('{0:02}.jpg'.format(f),'wb')
		of.write(urllib.urlopen(imgpref+'chapter-'+str(i)+'/'+str(f)+'.jpg').read())
		of.close()
		print 'DL {0:02}/{1}'.format(f,mpages-1)
	os.chdir('..')
	print '--------------------'
	print
