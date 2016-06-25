#!/usr/bin/env python
import json

file = open('users.json', 'r')
lines = [l.replace('\n','') for l in file.readlines()]
users_all = []
end_users={}

for line in lines:
    users_json = json.loads(line)
    for u in users_json['users']:
        users_all.append(u)

for u in users_all:
    if u['role'] == 'end-user':
        if u['suspended'] == False and 'suspended' not in u['name'].lower():
            if u['user_fields']['support_portal'] == True:
                if u['last_login_at'] != None and u['last_login_at'].startswith('2016'):
                    try:
                        name = u['name']
                        email = u['email']
                        last_login_at=u['last_login_at']
                        data = {'email': email, 'last_login_at': last_login_at}
                        end_users[name] = data
                    except:
                        pass

if len(end_users) > 0:
    print 'Username, Email, Last Login'
    for username, data in end_users.iteritems():
        username = username.encode('utf-8').strip()
        email = data['email'].encode('utf-8').strip()
        last_login_at = data['last_login_at'].encode('utf-8').strip()
        print '%s, %s, %s' % (username, email, last_login_at)
