import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

''' OPEN THE FILE WITH ETREE.PARSE:
tree = ET.parse('comments_1085150.xml')
'''

my_sum = list()
file = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1085150.xml').read()
tree = ET.fromstring(file)
for child in tree.iter('count'):
	my_sum.append(int(child.text))

print(sum(my_sum))
