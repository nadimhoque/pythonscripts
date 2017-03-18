#!/usr/bin/python
import hostpro

log = open('lastb.log','r')

for lines in log:
	hostpro.addtomainiplist(lines.split()[2])

log.close()
