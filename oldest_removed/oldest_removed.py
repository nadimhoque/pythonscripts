#!/usr/bin/python

import subprocess
import re
import string

kernellist = []
listver = []
#subprocess.call(["rpm","-qa"])

def getkernelversion(kernellist):
	verlist = []
	for version in kernellist:
		verlist.append(version[7:-11])
	return verlist

def findnewest(versionlist):
	#print versionlist[0]
	oldest = versionlist[0]
	for package in versionlist:
		if package < oldest:
			package = oldest
	print oldest


rpmout = subprocess.Popen(('rpm','-qa'),stdout=subprocess.PIPE)


for items in iter(rpmout.stdout.readline, ''):
	#kernellist.append(re.findall('^kernel-[0-9].+',items))
	temp = re.findall('^kernel-[0-9].+',items)
	if temp:
		kernellist.append(temp[0])

listver=getkernelversion(kernellist)
findnewest(listver)
