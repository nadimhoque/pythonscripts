#!/usr/bin/python
import re
def hostlist(mainlist):
	host = []
	for items in mainlist:
		if items not in host:
			host.append(items)
	for output in host:
		print output

def iponly(mainlist):
	ips =[]
	pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
	for items in mainlist:
		if items not in ips:
			if pattern.match(items):
				ips.append(items)
	for output in ips:
		print output
			
def userlist(mainlist):
	users = []
	for items in mainlist:
		if items not in users:
			users.append(items)
	print users