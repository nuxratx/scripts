import socket
import json
import argparse 

#Importing socket python module which provides access to the BSD socket interface, available on all modern Unix system, windows, MacOs


parser = argparse.ArgumentParser()
parser.add_argument('-t', --'TextFile', required=True)
args = parser.parse_args()

args.TextFile = r"~/python/scripts"

#Creating empty dictionary call mappings to later store unique key values in here 
mappings = {}
with open (r"{}".format(args.TextFile),'r') as ip_addresses:
    for line in ip_addresses:
        res = socket.gethostbyaddr(line.rstrip())
        mappings[res[0]] = res[2][0]

print(json.dump(mappings, sort_keys=True, indent=4, default=str))