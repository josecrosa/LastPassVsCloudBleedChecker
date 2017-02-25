import urllib.parse
import sys

compromised_file = sys.argv[1]
lastpass_file = sys.argv[2]

#import file data
list_of_sites = open(compromised_file).readlines()
list_of_passwords = open(lastpass_file).readlines()

#sanitze sites
for i in range(len(list_of_sites)):
    list_of_sites[i] = list_of_sites[i].rstrip()
for i in range(len(list_of_passwords)):
    simplified = "{0.netloc}".format(urllib.parse.urlsplit(list_of_passwords[i].split(",")[0])).replace("www.","")
    if simplified == "":
        print("unable to parse",list_of_passwords[i])
    list_of_passwords[i] = simplified

for password in list_of_passwords:
    if password == "":
        continue
    if password in list_of_sites:
        print("Site",password,"is affected")
