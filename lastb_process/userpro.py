from collections import Counter

# this function prints all the users who attempted to log in
def userlist(mainlist):
    users = []
    for items in mainlist:
        if items not in users:
            users.append(items)
    for items in users:
		print items

def useroccur(mainlist):
    listm = Counter(mainlist)
    for key, value in listm.items():
        print(key, value)