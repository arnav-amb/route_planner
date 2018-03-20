from googleplaces import GooglePlaces, types, lang


API_KEY = 'AIzaSyAD0tsB11_bi7ofAvU-M2S459wmPRkOlYY'

google_places = GooglePlaces(API_KEY)

query_result = google_places.nearby_search(
    location='Mumbai', keyword='Restaurants',
    radius=1000, types=[types.TYPE_RESTAURANT])

if query_result.has_attributions:
   print (query_result.html_attributions)


for place in query_result.places:
    print (place.name)
    print (place.geo_location)
    print (place.place_id)
    print(place.rating)  