#!/usr/bin/python
import hostpro
import userpro

def hostlistprint():
    print "Please select One of the following options:"
    print "1: All hostnames and IP addresses"
    print "2: Only IP addresses"
    print "3: Only hostnames"
    print "4: Print number of occurances of IP and hostnames"
    print "5: Print numer of IP occurances"
    print "6: Print number of hostname occurances"

def printmenu():
    print "Please select the following"
    print "1: Get all the users who attempted to login"
    print "2: Hostname/IP information (This will display another menu)"
    print "3: Get the start time of the login attempt"
    print "4: Print the whole log as is"
    print "5: Print number of user occurances"
    print "q: Exits the program"


def main():
    mainlist = []
    hostnames = []
    user = []
    time = []
    selection = "g"
    hostsel = "g"

    # the below lines are simply parsing the colums
    log = open('lastb.log', 'r')

    for lines in log:
        mainlist.append(lines)
        hostnames.append(lines.split()[2])
        user.append(lines.split()[0])
        time.append(lines.split()[6])
    # date.append(lines.split()[4])

    while selection != "q":
        printmenu()
        selection = raw_input("Please enter your selection now:")

        if selection == "1":
            userpro.userlist(user)

        if selection == "2":
            hostlistprint()
            hostsel = raw_input("Please enter one of the following:")
            if hostsel == "1":
                hostpro.hostlist(hostnames)
            if hostsel == "2":
                hostpro.iponly(hostnames)
            if hostsel == "3":
                hostpro.hostonly(hostnames)
            if hostsel == "4":
                hostpro.occurofhostip(hostnames)
            if hostsel == "5":
                hostpro.occurofip(hostnames)
            if hostsel == "6":
                hostpro.occurofhost(hostnames)

        if selection == "4":
            log.seek(0)
            for lines in log:
                print lines

        if selection == "5":
            userpro.useroccur(user)

    log.close()


if __name__ == "__main__":
    main()
