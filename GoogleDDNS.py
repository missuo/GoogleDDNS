'''
Author: Vincent
Date: 2022-05-26 03:46:30
LastEditors: Vincent
LastEditTime: 2022-05-26 04:47:10
FilePath: /GoogleDDNS/GoogleDDNS.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
import requests
import socket
import base64

# The domain name you want to update
HOSTNAME = "yourdomainname.com"
# Your Google Domains username(Not Google account)
USERNAME = "yourusername"
# Your Google Domains password
PASSWORD = "yourpassword"

"""
FOR EXAMPLE:
HOSTNAME = "example.domain.com"
USERNAME = "yourusername"
PASSWORD = "yourusername"
"""

# Get the current resolved IP of the domain name
def getResolvedIP(hostname):
    googleIP = socket.gethostbyname(hostname)
    return googleIP

# Get Current IP From IP.SB
def currentRealIP():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    }
    IPFromAPI = requests.get(url = "https://api-ipv4.ip.sb/ip", headers = headers).text
    IPFromAPI = IPFromAPI.strip()
    return IPFromAPI

# Update Lastest IP of the domain name
def updateIP(username, password, hostname, myip):
    userInfo = username + ":" + password
    auth = "Basic " + str(base64.b64encode(userInfo.encode('utf-8')),"utf-8")
    googleAPI = "https://domains.google.com/nic/update"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization" : auth
    }
    data = {
        "hostname": hostname,
        "myip": myip
    }
    googleAPIResponse = requests.post(url = googleAPI, headers = headers, data = data).text
    return googleAPIResponse

# Main function
def main():
    resolvedIP = getResolvedIP(HOSTNAME)
    currentIP = currentRealIP()
    if resolvedIP != currentIP:
        updateInfo = updateIP(USERNAME, PASSWORD, HOSTNAME, currentIP)
        if "good" in updateInfo:
            print("Successfully Updated!")
            print("Updated IP: " + currentIP)
        else:
            print("Failed Updated!", updateInfo)
    else:
        print("Current IP: {} is the latest, not need to update." % currentIP)

main()