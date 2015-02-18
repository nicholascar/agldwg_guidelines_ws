import re
import settings
import pprint
import operator

rules = {}
d = open(settings.HOME_DIR + 'test/webpage-v0.1.html').read()

pattern = '<strong>\[no[\s]*([\da-f]*)\]</strong>[\s]*</td>[\s]*<td[\w\"=\s]*>[\s]*(.*)</td>'
results = re.findall(pattern, d)

for match in results:
    rules[match[0].zfill(2)] = match[1]

pattern = '<b>\[no[\s]*([\da-f]*)\]</b>[\s]*</td>[\s]*<td[\w\"=\s]*>[\s]*(.*)</td>'
results = re.findall(pattern, d)

for match in results:
    rules[match[0].zfill(2)] = match[1]

sorted_x = sorted(rules.items(), key=operator.itemgetter(0))
pprint.pprint(rules)