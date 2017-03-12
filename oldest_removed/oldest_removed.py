#!/usr/bin/python

import subprocess
import re
import string

kernellist = []
#subprocess.call(["rpm","-qa"])

def oldestkernel(kernellist):
	#kernelout = re.search('(^kernel)',kernellist)
	#kernelout.group(0)
	print kernellist
	


rpmout = subprocess.Popen(('rpm','-qa'),stdout=subprocess.PIPE)

#kernels = subprocess.Popen(('grep','kernel-[0-9]'),stdin=rpmout.stdout.read())

for items in iter(rpmout.stdout.readline, ''):
	if "kernel" in items:
		kernellist.append(items.split("\n"))

oldestkernel(kernellist)
