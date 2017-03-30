#!/usr/bin/python
import re
from collections import Counter


# this function prints out all unique hostnames and ip addresses
def hostlist(mainlist):
    host = []
    for items in mainlist:
        if items not in host:
            host.append(items)
    for output in host:
        print output


# this function prints all unique ip adddresses
def iponly(mainlist):
    ips = []
    pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    for items in mainlist:
        if items not in ips:
            if pattern.match(items):
                ips.append(items)
    for output in ips:
        print output


def hostonly(mainlist):
    hosts = []
    pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    for items in mainlist:
        if items not in hosts:
            if not pattern.match(items):
                hosts.append(items)
    for output in hosts:
        print output


# this function prints all the users who attempted to log in
def userlist(mainlist):
    users = []
    for items in mainlist:
        if items not in users:
            users.append(items)
    for items in users:
		print items


def numberof(mainlist):
    # print "running numberof function"
    # print mainlist
    listm = Counter(mainlist)
    for key, value in listm.items():
        print(key, value)
    # for items in listm:
    # print items
    # counted = dict()
    # for items in mainlist:
    # if items not in counted:
    # counted[items] = 1
    # if items in counted:
    # counted[items] += 1
