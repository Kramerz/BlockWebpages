## Idea of this website is to block websites from specific times,
## This will be able to be ran as an application on a local PC and or,
## attach this to a GUI interface for individuals who don't have,
## Python

##  Created by: Ryan William West

import time
from datetime import datetime as dt


##2016-11-30 @ 9:23 - Last Update Ryan William West
## Need to figure out how to make this python application run automatically when PC Starts up
## Also need to figure out why the "Hosts_Path = "/etc/hosts" is not working properly

##Additional, possibly add a GUI to allow Administrators the rights to modify the Dictionary I.E Lists
##Pending Arrival at home.


hosts_temp="hosts" #Temp folder so we don't ruin the orignal copy. 
hosts_path = "/etc/hosts"
redirect = "127.0.0.1" ##Where your Webpage will be re-directed towards

website_list=["www.facebook.com ","facebook.com","google.com","www.google.com","outlook.com","www.outlook.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,21):    
        print("Within working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
        time.sleep(5)

    else:
        with open (hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun hours")
    time.sleep(5)
    
