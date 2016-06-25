#!/usr/bin/env python
from getpass import getpass
import requests
import json

username = 'amccurdy@zenoss.com'
password = getpass('Password: ')
api_url = 'https://zenoss.zendesk.com/api/v2/users.json'

with open('users.json', 'a') as file:
    initial_request = requests.get(api_url, auth=(username, password))
    initial_request_text = initial_request.text.encode('utf-8').strip()
    file.write(initial_request_text+'\n')
    initial_json = json.loads(str(initial_request_text))
    done = 100
    total = initial_json['count']
    reqs = 1

while done < total:
    reqs += 1
    url = api_url + '?page=%s' % (int(reqs))
    print 'Making request %s to %s' % (reqs, url)
    next_request = requests.get(url, auth=(username, password))
    next_request_text = next_request.text.encode('utf-8').strip()
    with open('users.json','a') as file:
        file.write(next_request_text+'\n')
    done += 100
