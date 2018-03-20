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

#new_api = 'https://maps.googleapis.com/maps/api/geocode/json?'

api_key = 'AIzaSyAD0tsB11_bi7ofAvU-M2S459wmPRkOlYY'
#place_request= 'address={}&key={}'.format('hawa mahal, jaipur', api_key)

#request = new_api + place_request
#r = requests.get(request)
# print(r)
# f= open('input.json','w+')
# f.write(r.text)
# f.close()
# #using search place api

#endpoint = 'https://maps.googleapis.com/maps/api/place/details/json?'
with open('input.json','r') as myfile:
	content=json.load(myfile)
newcontent=content['results'][0]
more=newcontent['geometry']
late=more['location']
latitude = late['lat']
longitute = late['lng']
place_id= newcontent["place_id"]

# 
# place_ask = 'key={}&place_id={}'.format(api_key,place_id)
#
# request_2 = endpoint + place_ask
#
# r_2=requests.get(request_2)
# print(r_2)
# f=open('user.json','w+')
# f.write(r_2.text)
# f.close()

#api for getting places to visit nearby

# near_by='https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

places=['restaurant','market','monument','temples','mosque']
# i=0
# while i < len(places):
# 	#print(places[i])
# 	nearby_ask = 'key={}&location={},{}&radius={}&keyword={}'.format(api_key,latitude,longitute,'10000',places[i])
# 	#print(nearby_ask)
# 	request_4 = near_by + nearby_ask
# 	#print(request_4)
# 	r_4=requests.get(request_4)
# 	f=open('near_places'+str(i)+'.json','w+')
# 	f.write(r_4.text)
# 	f.close()
# 	i+=1


# # print(r_3)

#api for getting directions between two places

# path='https://maps.googleapis.com/maps/api/directions/json?'

# app_key='AIzaSyAqwxsqZQbDezGD_V-egxM4kxzm-0bpQ_8'
# path_var='origin={}&destination={}&key={}'.format('hawa mahal','jal mahal',api_key)

# request_3 = path + path_var
# r_3=requests.get(request_3)
# f=open('places.json','w+')
# f.write(r_3.text)
# f.close()

#api ends
i=0
while i < len(places):
	with open('near_places'+str(i)+'.json', 'r') as data_file:
		data=json.load(data_file)
	for j in data:
		results = j{'results'}
		place_name = j{'name'}
		print(place_name)


	i+=1	
#
