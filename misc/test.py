from place import Place
import numpy as np
import operator

alpha= 20
beta= 500
priority={}
priority['monument']=1
priority['market']=3
priority['museum']=2

places=[]
places.append(Place('Jal Mahal',(26.965604, 75.859205), 4.5, 'monument', 'Jaipur'))
places.append(Place('Nehru Bazaar',(26.918636, 75.818895), 4.0, 'market', 'Jaipur'))
places.append(Place('City Palace',(26.925771, 75.82658), 4.4, 'museum', 'Jaipur'))
places.append(Place('Jantar Mantar',(26.924762,75.824560), 4.4, 'monument', 'Jaipur'))
places.append(Place('Hawa Mahal',(26.923936, 75.826744), 4.2, 'monument', 'Jaipur'))
# current_location= (50,63)

def find_distance(current_location, location):
    # Use Google Maps API to calculate distance
    K = 0.5 # Speed scaling factor
    return K*np.sqrt(np.sum(np.square(np.sum(current_location, -1*location))))

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

# for place in places:
#     print(place.name+", score: "+str(place.score))

# Sort in descending order
places.sort(key=operator.attrgetter('score'))
places= places[::-1]

for place in places:
    print(place.name+", score: "+str(place.score))

hours_each_day = 8
number_of_days = 2
number_of_cities = 1
hours_for_each_city = (hours_each_day*number_of_days*1.0)/number_of_cities

NLF = 1.8    # Number limiting factor
number_of_places_per_city = int(hours_for_each_city/NLF)
if number_of_places_per_city > len(places):
    number_of_places_per_city = len(places) #override
shortlisted= places[0:number_of_places_per_city]

# Creating a distance matrix for later frequent use
dist_matrix = np.zeros((len(shortlisted), len(shortlisted)))
for pos in range(len(shortlisted)):
    for pos2 in range(len(shortlisted)):
        dist_matrix[pos, pos2]= find_distance(shortlisted[pos].location, shortlisted[pos2].location)

all_routes= []
# Plan all routes for a city
for pos in range(len(shortlisted)):
    route_dist = 0
    unvisited = list(range(len(shortlisted)))
    unvisited.remove(pos)
    pos1 = pos
    while len(unvisited)>0:
        temp_dist= [dist_matrix[pos1,pos2] for pos2 in unvisited ]
        closest = min(temp_dist)
        pos1 = unvisited[temp_dist.index(closest)]
        unvisited.remove(pos1)
        route_dist = route_dist + closest
    all_routes.append(route_dist)

# Adding the distance from current location if available
current_location = (26.914125, 75.804636) # None if user does not want to give his location
start_node= current_location
if current_location != None:
    all_routes = [all_routes[i] + find_distance(current_location, shortlisted[i].location) for i in range(len(shortlisted))]

print(all_routes)

start_node = all_routes.index(min(all_routes))

print(start_node)
