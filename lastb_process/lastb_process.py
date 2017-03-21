#!/usr/bin/python
import hostpro


def printmenu():
	print "Please select the following"
	print "1: Get all the users who attempted to login"
	print "2: Get all of the hostnames/IP addresses who attempted to log in"
	print "3: Get the start time of the login attempt"
	print "4: Print the whole log as is"
	print "q: Exits the program"
	
def main():
	mainlist = []
	hostnames = []
	user = []
	time = []
	selection = "g"

# the below lines are simply parsing the colums
	log = open('lastb.log','r')

	for lines in log:
		mainlist.append(lines)
		hostnames.append(lines.split()[2])
		user.append(lines.split()[0])
		time.append(lines.split()[6])
		#date.append(lines.split()[4])

	while selection != "q":
		printmenu()
		selection = raw_input("Please enter your selection now:")

		if selection == "1":
			hostpro.userlist(user)

		if selection == "2":
			hostpro.hostlist(hostnames)

	log.close()

if __name__ == "__main__":
	main()