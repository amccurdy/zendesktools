#!/usr/bin/env python
import json

file = open('tickets.json', 'r')
lines = [l.replace('\n','') for l in file.readlines()]
tickets_all = []
tickets_clean = []

for line in lines:
    ticket_json = json.loads(line)
    tickets_all.append(ticket_json)

for t in tickets_all:
    ticket_id = t['id']
    ticket_created = t['created_at'].split('T')[0]
    ticket_updated = t['updated_at'].split('T')[0]
    ticket_subject = t['subject']
    ticket_desc = t['description']
    ticket_status = t['status'].title()
    ticket_url = t['url']
    ticket_custom = t['custom_fields']

    for field in ticket_custom:
        if field['id'] == 23632565 and field['value'] is not None:
            ticket_jira = field['value']
        if field['id'] == 23543855 and field['value'] is not None:
            ticket_deployment = field['value']
        if  field['id'] == 23345365 and field['value'] is not None:
            ticket_product = field['value']

    if 'ticket_jira' not in locals():
        ticket_jira = ''
    if 'ticket_deployment' not in locals():
        ticket_deployment = ''
    if 'ticket_product' not in locals():
        ticket_product = ''

    # some cleanup
    ticket_product = ticket_product.replace('resource_manager', 'Resource Manager')
    ticket_product = ticket_product.replace('resourcemanagerzenossenterprise', 'Resource Manager')
    ticket_product = ticket_product.replace('control_center', 'Control Center')
    ticket_product = ticket_product.replace('analytics', 'Analytics')
    ticket_product = ticket_product.replace('zenpack', 'ZenPack')
    ticket_product = ticket_product.replace('impact', 'Impact')
    ticket_product = ticket_product.replace('other', 'Other')
    ticket_deployment = ticket_deployment.replace('_deployment', '').title()

    ticket_dict = {'id': ticket_id,
                    'created': ticket_created,
                    'updated': ticket_updated,
                    'subject': ticket_subject,
#                    'desc': ticket_desc,
                    'status': ticket_status,
#                    'url': ticket_url,
                    'jira': ticket_jira,
                    'deployment': ticket_deployment,
                    'product': ticket_product
                    }

    tickets_clean.append(ticket_dict)
    del(ticket_jira)
    del(ticket_deployment)
    del(ticket_product)

if len(tickets_clean) > 0:
    print 'Ticket ID|Created At|Updated At|Subject|Status|JIRA Ticket|Deployment|Product'
    for ticket in tickets_clean:
        print '%s|%s|%s|%s|%s|%s|%s|%s' % (ticket['id'], ticket['created'], ticket['updated'],
                                              ticket['subject'], ticket['status'], ticket['jira'],
                                              ticket['deployment'], ticket['product'])
