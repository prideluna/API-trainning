# import urllib3, sys
# from BeautifulSoup import BeautifulSoup

# url = "http://api.glassdoor.com/api/api.htm?t.p=yourID&t.k=yourkey&userip=8.28.178.133&useragent=Mozilla&format=json&v=1&action=employers&q="
# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = urllib2.Request(url,headers=hdr)
# response = urllib2.urlopen(req)
# soup = BeautifulSoup(response)

import requests
import json
# import pprint

url = "http://api.tvmaze.com/singlesearch/shows"
show = input("Input a show name:")
params = {"q":show}

response = requests.get(url,params=params)

if response.status_code == 200:
    data = json.loads(response.text)
    # pprint.pprint(data)
    # print(response.text)
    name = data["name"]
    premiered = data["premiered"]
    summary = data["summary"]

    print(f"{name} premiered on {premiered}.")
    print(summary)

else:
    print(f"error {response.status_code}")