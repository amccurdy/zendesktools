from xml.etree import ElementTree
users = ElementTree.parse('users.xml')
orgs = ElementTree.parse('organizations.xml')
users_root = users.getroot()
orgs_root = orgs.getroot()

users_list = []
active_orgs_dict = {}
merged_users_orgs = {}

for user in users_root.findall('user'):
    user_dict = {}
	# this will be either 'support_portal' or None, which is why I'm not bothering to evaluate the actual text
    if user.find('current-tags').text:
        user_dict['name'] = user.find('name').text
        user_dict['email'] = user.find('email').text
        user_dict['organization_id'] = user.find('organization-id').text
        user_dict['last_login'] = user.find('last-login').text
        user_dict['is_active'] = user.find('is-active').text
        users_list.append(user_dict)


for org in orgs_root.findall('organization'):
    if org.find('suspended').text == 'false':
        organization_id = org.find('id').text
        organization_name = org.find('name').text
        active_orgs_dict[organization_id] = organization_name

for user in users_list:
    org_id = user['organization_id']
    if org_id in active_orgs_dict.keys():
        org = active_orgs_dict[org_id]
        user_entry = (user['name'], user['email'], user['last_login'], user['is_active'])
        # create the entry if it's not there
        if org not in merged_users_orgs.keys():
            merged_users_orgs[org] = [user_entry]
        else:
            merged_users_orgs[org].append(user_entry)
