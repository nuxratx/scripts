
"""
Created on Sun Jun  10 21:41:08 2024

@author: nuxratx
    
"""
import argparse
import socket
import pprint


parser = argparse.ArgumentParser(description = 'Using this to manually input hostnames')
parser.add_argument('-s','--hostnames', help='Input the hostnames' , nargs ='+', default=[])
args= parser.parse_args()


# Here setting up an empty dictionary to map hostname to Ipaddresses 
mappings = {}

for hostname in args.hostnames:
    ipaddress = socket.gethostbyname(hostname)
    mappings[hostname] = ipaddress

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(mappings)


    
    








    
    
            
        