import requests
import socket
import dns.resolver
import tldextract
import urllib.request
# for internal pc information
import getpass
import os.path
import os
import re
import json
from urllib.request import urlopen 

url = input("Enter Your URL: ")
info = tldextract.extract(url)

def get_status():
    response = requests.get('https://'+url)
    try:
        status = response.status_code
        if status == 200:
            print("Website Exist")
        else:
            print("There is a problem on your website")
    except Exception as e:
        print(str(e))

def dnfresolver():
    answers = dns.resolver.query(url,'NS')
    try:
        for server in answers:
            print (server)
    except Exception as e:
        print(str(e))        
    

def get_ip_servername():
    IP = socket.gethostbyname(url)
    print("IP  Is:",IP )
    try:
        addr = socket.gethostbyaddr(IP)
        print("Addr  Is:",addr ) 
    except Exception as e:
        print(str(e))
    

get_status()
dnfresolver()
get_ip_servername()

#get domain sub domaine
print("Domain Name: ", info.domain)
print("Subdomain: ", info.subdomain)
print("Suffix: ", info.suffix)
print("Domain with suffix: ", info.registered_domain)
print("Full Domain: ", '.'.join(info))

req = requests.get('http://'+url)
headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code', 'Connection', 'Content-Type']
for header in headers:
    try:
        result = req.headers[header]
        print ('%s: %s' % (header, result))
    except Exception as e:
        print ('%s: Not found' % header)




