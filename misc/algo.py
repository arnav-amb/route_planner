# Parameters
# Number of days
# Hor per day
# City limit calculation
# Cities choice

# Places
# Rating
# Type priority: Monument, Restaurant, Markets, Sanctuaries
# Lat Long: distance calculation
# Number of places fitting in a day. Time spent at each place Gauss(30,90)

import requests
import json

# Google Places API
# Google Geocoding API

new_api = 'https://maps.googleapis.com/maps/api/geocode/json?'

api_key = 'AIzaSyAD0tsB11_bi7ofAvU-M2S459wmPRkOlYY'
place_request= 'address={}&key={}'.format('hawa mahal, jaipur', api_key)

request = new_api + place_request
# response = urllib.request.urlopen(request).read()
r = requests.get(request)
print(r)
f= open('input.json','w+')
f.write(r.text)
f.close()
#using search place api

endpoint = 'https://maps.googleapis.com/maps/api/place/details/json?'
with open('input.json','r') as myfile:
	content=json.load(myfile)
print(content)			
#getObjects(content,"gemeotry","location")
#id=content[53][23:50]
#res_dic = json.loads(content.results)
#id = res_dict['place_id']

place_ask = 'key={}&place_id={}'.format(api_key,id)

request_2 = endpoint + place_ask

r_2=requests.get(request_2)
print(r_2)
f=open('user.json','w+')
f.write(r_2.text)
f.close()







