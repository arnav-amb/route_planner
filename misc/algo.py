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
from place import Place



CITY_NAME = 'jaipur'

# Google Places API
# Google Geocoding API

new_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = 'AIzaSyAD0tsB11_bi7ofAvU-M2S459wmPRkOlYY'



place_request= 'address={}&key={}'.format(CITY_NAME, api_key)

request = new_api + place_request
print(request)
r = requests.get(request)
print(r)
f = open('input.json','w+')
f.write(r.text)
f.close()
#using search place api

with open('input.json','r') as myfile:
	content=json.load(myfile)
newcontent=content['results'][0]
more=newcontent['geometry']
late=more['location']
latitude = late['lat']
longitute = late['lng']
place_id= newcontent["place_id"]


#api for getting places to visit nearby

near_by='https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

places=['restaurant','market','monument','temples','mosque']

for i in range(len(places)):
	#print(places[i])
	nearby_ask = 'key={}&location={},{}&radius={}&keyword={}'.format(api_key,latitude,longitute,'10000',places[i])
	#print(nearby_ask)
	request_4 = near_by + nearby_ask
	#print(request_4)
	r_4=requests.get(request_4)
	f=open('near_places'+str(i)+'.json','w+')
	f.write(r_4.text)
	f.close()



list_of_places=[]
for i in range(len(places)):
	with open('near_places'+str(i)+'.json', 'r') as data_file:
		data= json.load(data_file)

	l= len(data['results'])
	for k in range(l):
		place_id = data['results'][k]['place_id']
		name = data['results'][k]['name']
		lat = data['results'][k]['geometry']['location']['lat']
		lng = data['results'][k]['geometry']['location']['lng']
		photo_reference=data['results'][k]['photos']['photo_reference']
		photo_height=data['results'][k]['photos']['height']
		try:
			rating = data['results'][k]['rating']
		except:
			rating = 1
		type_of = data['results'][k]['types']
		# Creating a Place object and storing it in a list
		list_of_places.append(Place(name, lat, lng, rating, rating, type_of, CITY_NAME, place_id))

print(len(list_of_places))




def get_places(CITY_NAME):
	# INIT  only
	# place_request= 'address={}&key={}'.format(CITY_NAME, api_key)
	#
	# request = new_api + place_request
	# r = requests.get(request)
	# print(r)
	# f= open('input.json','w+')
	# f.write(r.text)
	# f.close()

	#using search place api

	with open('input.json','r') as myfile:
		content=json.load(myfile)
	newcontent=content['results'][0]
	more=newcontent['geometry']
	late=more['location']
	latitude = late['lat']
	longitute = late['lng']
	place_id= newcontent["place_id"]


	#api for getting places to visit nearby

	near_by='https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

	places=['restaurant','market','monument','temples','mosque']

	for i in range(len(places)):
		#print(places[i])
		nearby_ask = 'key={}&location={},{}&radius={}&keyword={}'.format(api_key,latitude,longitute,'10000',places[i])
		#print(nearby_ask)
		request_4 = near_by + nearby_ask
		#print(request_4)
		r_4=requests.get(request_4)
		f=open('near_places'+str(i)+'.json','w+')
		f.write(r_4.text)
		f.close()



	list_of_places=[]
	for i in range(len(places)):
		with open('near_places'+str(i)+'.json', 'r') as data_file:
			data= json.load(data_file)

		l= len(data['results'])
		for k in range(l):
			place_id = data['results'][k]['place_id']
			name = data['results'][k]['name']
			lat = data['results'][k]['geometry']['location']['lat']
			lng = data['results'][k]['geometry']['location']['lng']
			try:
				rating = data['results'][k]['rating']
			except:
				rating = 1
			type_of = data['results'][k]['types']
			# Creating a Place object and storing it in a list
			list_of_places.append(Place(name, lat, lng, rating, rating, type_of, CITY_NAME, place_id))

	print(len(list_of_places))
	return(list_of_places)


x= get_places('Jaipur')


#api for getting directions between two places

# path='https://maps.googleapis.com/maps/api/directions/json?'

# path_var='origin={}&destination={}&key={}'.format('hawa mahal','jal mahal',api_key)

# request_3 = path + path_var
# r_3=requests.get(request_3)
# f=open('places.json','w+')
# f.write(r_3.text)
# f.close()

picture ='https://maps.googleapis.com/maps/api/place/photo?'
parameter= 'key={}&photo_reference={},maxheight={}'.format(api_key,photo_reference,photo_height)

request_5 = picture + parameter
r_5 =requests.get(request_5)
r_5.save()



#api ends
