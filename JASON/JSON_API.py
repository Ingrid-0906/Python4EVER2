import urllib.request, urllib.parse, urllib.error
import json

api_key = False

if api_key is False:
    api_key = 42
    serurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = 'Purdue University Indianapolis'
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        break

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    plac= js['results'][0]['place_id']
    loc = js['results'][0]['formatted_address']
    print('| Latitude: {} \n| Longitude: {} \n| Place Id: {} \n| Location: {}'.format(lat, lng, plac, loc))
    break