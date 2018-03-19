from place import Place
import numpy as np
import operator

alpha= 20
beta= 500
priority={}
priority['Monument']=1
priority['Market']=3

places=[]
places.append(Place('Jal Mahal',(100,156), 4.5, 'Monument', 'Jaipur'))
places.append(Place('Nehru Bazaar',(96, 473), 4.0, 'Market', 'Jaipur'))
places.append(Place('Hawa Mahal',(50, 73), 4.2, 'Monument', 'Jaipur'))

# current_location= (50,63)

def find_distance(current_location, location):
    # Use Google Maps API to calculate distance
    return np.sqrt(np.sum(np.square(np.sum(current_location, -1*location))))

def assign_costs(places):
    for place in places:
        R= place.rating
        P= priority[place.type_of]
        # Cost Assigning Algorithm
        SCORE = alpha*(R**2) + beta/np.log(P+1)
        place.set_score(SCORE)
        print(SCORE)
    return places

places = assign_costs(places)

for place in places:
    print(place.name+", score: "+str(place.score))

# Sort in descending order
places.sort(key=operator.attrgetter('score'))
places= places[::-1]

for place in places:
    print(place.name+", score: "+str(place.score))
