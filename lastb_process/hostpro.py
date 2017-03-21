#!/usr/bin/python

def hostlist(mainlist):
	host = []
	for items in mainlist:
		if items not in host:
			host.append(items)
	print host
			
def userlist(mainlist):
	users = []
	for items in mainlist:
		if items not in users:
			users.append(items)
	print users