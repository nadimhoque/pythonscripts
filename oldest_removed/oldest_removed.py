#!/usr/bin/python

import subprocess
import re

kernellist = []
#subprocess.call(["rpm","-qa"])

def oldestkernel(kernellist):
	print "hello"


rpmout = subprocess.Popen(('rpm','-qa'),stdout=subprocess.PIPE)

#kernels = subprocess.Popen(('grep','kernel-[0-9]'),stdin=rpmout.stdout.read())

for items in iter(rpmout.stdout.readline, ''):
	print items
