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

# Google Places API
# Google Geocoding API

endpoint = 'https://maps.googleapis.com/maps/api/place/details/json?'
api_key = 'AIzaSyAD0tsB11_bi7ofAvU-M2S459wmPRkOlYY'
place_request= 'http://key={}&name={}'
request = endpoint = place_request
# response = urllib.request.urlopen(request).read()
response = requests.get(request)
details = json.load(response)
print(details)
