#!/usr/bin/python

import subprocess

#subprocess.call(["rpm","-qa"])

rpmout = subprocess.Popen(('rpm','-qa'),stdout=subprocess.PIPE)

subprocess.Popen(('grep','kernel-[0-9]'),stdin=rpmout.stdout)
