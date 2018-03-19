# Parameters
# Number of days
# Hour per day
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
place_request= 'address={}&key={}'.format('jaipur', api_key)

request = new_api + place_request
# response = urllib.request.urlopen(request).read()
r = requests.get(request)
print(r)
JSONObject js = new JSONObject(r)
id = js.getString("place_id")
endpoint = 'https://maps.googleapis.com/maps/api/place/details/json?'
places= 'name={}&key={}'.format(id,api_key)
request_2 = endpoint + places
new_res = requests.get(request_2)
f= open('input.txt','w+')
f.write(new_res.text)
f.close()
