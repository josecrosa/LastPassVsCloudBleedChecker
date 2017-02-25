import urllib.parse


compromised_file = "PATH_TO/sorted_unique_cf.txt"
lastpass_file = "PATH_TO/lastpass.csv"

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
    if password in list_of_sites:
        print("Site",password,"is affected")
