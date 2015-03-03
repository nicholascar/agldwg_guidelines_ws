import re
import settings
import pprint
import operator
import json
'''
rules = {}
#d = open(settings.HOME_DIR + 'test/webpage-v0.1.html').read()
d = open('/home/car587/ownCloud/code/AGLDWG_TR_wiki/URI-Guidelines-for-publishing-linked-datasets-on-data.gov.au-v0.1.html').read()

pattern = '<strong>\[no[\s]*([\da-f]*)\]</strong>[\s]*</td>[\s]*<td[\w\"=\s]*>([\s]*.*[\s]*.*[\s]*.*)</td>'
results = re.findall(pattern, d)

for match in results:
    rules[match[0].zfill(2)] = match[1]\
        .replace('\n', '')\
        .replace('  ', ' ')\
        .replace('  ', ' ')\
        .replace('  ', ' ')\
        .replace('  ', ' ')\
        .replace('  ', ' ')\
        .decode(encoding='utf-8')

#pattern = '<b>\[no[\s]*([\da-f]*)\]</b>[\s]*</td>[\s]*<td[\w\"=\s]*>[\s]*(.*)</td>'
#results = re.findall(pattern, d)

#for match in results:
#    rules[match[0].zfill(2)] = match[1]

sorted_x = sorted(rules.items(), key=operator.itemgetter(0))
pprint.pprint(rules)
print len(rules)
'''

import requests
import re


def rule_002(uri):
    headers = {'accept': 'text/turtle,application/rdf+xml,application/ld+json,*;q=0'}
    r = requests.get(uri, headers=headers)
    if r.status_code == 200 and ('text/turtle' in r.headers['content-type'] or
                                 'application/rdf+xml' in r.headers['content-type'] or
                                 'application/ld+json' in r.headers['content-type']):
        return True
    else:
        return False


def rule_017(uri):
    agift_subdomains = [
        "business",
        "communications",
        "communityservices",
        "culture",
        "defence",
        "education",
        "employment",
        "environment",
        "finance",
        "internationalrelations",
        "governance",
        "health",
        "immigration",
        "indigenous",
        "infrastructure",
        "justice",
        "maritime",
        "primaryindustry",
        "recreation",
        "resources",
        "science",
        "security",
        "tourism",
        "trade",
        "transport"
    ]
    subdomain = re.search('http://([a-z]*)\.data.gov.au.*', uri)
    if subdomain and subdomain.group(1) in agift_subdomains:
        return True
    else:
        return False

#uri = 'http://pig.data.gov.au:9009/example'
#print rule_017(uri)


def rule_019(subdomain_uri):
    r = requests.get(subdomain_uri, allow_redirects=True)
    print r.status_code
    if r.status_code == 200:
        return True
    else:
        return False

print rule_019('http://localhost:9009/example2')