from xml.dom import minidom
from collections import Counter
import re
import json

xmldoc = minidom.parse('20110415_VAST11MC2_SecurityLog-rev2.xml')

events = xmldoc.getElementsByTagName('Events')[0]

e = events.getElementsByTagName('Event')

ic = 0
l = []
q = 0

for b in e:
	i = b.getElementsByTagName('EventID')[0].firstChild.data
	t = b.getElementsByTagName('TimeCreated')

	for fu in t:
		st = fu.attributes['SystemTime']
		stv = st.value

	if i == '4624':
		l.append(stv)
		

newList = [q.split(':', 1)[0] for q in l]


myDict = {j:newList.count(j) for j in newList}

print (json.dumps(myDict, indent=4, sort_keys=True))

	



		
		


