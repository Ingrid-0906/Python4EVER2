import urllib.request, urllib.parse, urllib.error
import json

text = input('Enter Location: ')
file = urllib.request.urlopen(text).read().decode()
info = json.loads(file)

lib = list()
clock = 0

for item in info["comments"]:
	lib.append(int(item['count']))
	clock += 1

print('Retriving: {}'.format(text))
print('Count: {}'.format(clock))
print('Sum: {}'.format(sum(lib)))
