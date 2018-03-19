from place import Place
import numpy as np

alpha= 5
beta= 2
gamma= 10

priority={}
priority['Monument']=1
priority['Market']=3

places=[]
places.append(Place('Jal Mahal',(100,156), 4.5, 'Monument', 'Jaipur'))
places.append(Place('Nehru Bazaar',(96, 473), 4.0, 'Market', 'Jaipur'))
places.append(Place('Hawa Mahal',(50, 73), 4.2, 'Monument', 'Jaipur'))

current_location= (70,23)

def find_distance(current_location, location):
    # Use Google Maps API to calculate distance
    return np.sqrt(np.sum(np.square(np.sum(current_location, -1*location))))

def assign_costs(places):
    for place in places:
        R= place.rating
        T= find_distance(place.location, current_location)
        P= priority[place.type_of]
        # Cost Assigning Algorithm
        COST = alpha*R**3 + beta/T**2 + (gamma/P)**2
        place.set_cost(COST)
        print(COST)
    return places

places = assign_costs(places)

for place in places:
    print(place.name+", cost: "+str(place.cost))

# Sort no working
places.sort(key = Place.cost)

for place in places:
    print(place.name+", cost: "+str(place.cost))
