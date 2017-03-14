#!/usr/bin/python

import subprocess
import re
import string

kernellist = []

#subprocess.call(["rpm","-qa"])

def oldestkernel(kernellist):
		print kernellist



rpmout = subprocess.Popen(('rpm','-qa'),stdout=subprocess.PIPE)


for items in iter(rpmout.stdout.readline, ''):
	#kernellist.append(re.findall('^kernel-[0-9].+',items))
	temp = re.findall('^kernel-[0-9].+',items)
	if temp:
		kernellist.append(temp[0])

oldestkernel(kernellist)
