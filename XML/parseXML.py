# Importing and Reading data
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')

# We can read a xml file by two ways:
# This way:
root = tree.getroot()
# or this other:
# data = ET.fromstring(tree)

'''# As an Element, root has a tag and a dictionary of attributes:
print(root.tag)
'''

''' # It also has children nodes over which we can iterate:
for child in root:
	print(child.tag, child.attrib)
'''

''' # Children are nested, and we can access specific child nodes by index:
print(root[0][1].text)
'''

''' # Finding Interesting ELements by specific child tag (.ITER()):
for neighbor in root.iter('neighbor'):
	print(neighbor.attrib)
'''

''' # Modyfing an Xml File (.WRITE()):
for rank in root.iter('rank'):
	new_rank = int(rank.text) + 1
	rank.text = str(new_rank)
	rank.set('updated', 'yes')

tree.write('output.xml')
'''

# For removing elements (.REMOVE()):
for country in root.findall('country'):
	# Using root.findall() to avoid removal during traversal
	rank = int(country.find('rank').text)
	if rank > 50:
		root.remove(country)
tree.write('output2.xml')
