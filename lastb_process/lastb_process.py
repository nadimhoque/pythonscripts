#!/usr/bin/python
import hostpro


def printmenu():
	print "Please select the following"
	print "1: Get all the users who attempted to login"
	print "2: Get all of the hostnames/IP addresses who attempted to log in"
	print "3: Get the start time of the login attempt"
	print "4: Print the whole log as is"
	

mainlist = []
hostnames = []
user = []
time = []
#date = []

#the below lines are simply parsing the colums
log = open('lastb.log','r')

for lines in log:
	mainlist.append(lines)
	hostnames.append(lines.split()[2])
	user.append(lines.split()[0])
	time.append(lines.split()[6])
	#date.append(lines.split()[4])
	
printmenu()	
selection = raw_input("Please enter your selection now:")

print selection

#print "hello world"
		
#hostpro.addtomainiplist(lines.split()[2])

log.close()
