#from place import Place
import numpy as np
import operator
from misc.api_call import get_places, find_distance

# PARAMETERS FOR FINE TUNING
alpha= 15
beta= 80000

class Place:
    name= None
    lat = None
    lng = None
    rating = None
    type_of = None
    city = None
    score= None
    photo= None
    place_id = None

    def __init__(self, name, lat, lng, rating, type_of, city, place_id, photo = None):
        self.name= name
        self.lat = lat
        self.lng = lng
        self.rating= rating
        self.type_of= type_of
        self.city= city
        self.place_id = place_id
        self.photo = photo

    def set_score(self, score):
        self.score= score


def fetch_filter():
    # Fetch data from user's choice
    filt = {}
    MONUMENT = True
    MUSEUM = False
    PLACES_OF_WORSHIP = False
    ZOO = True
    FAMOUS = False
    filt['monument'] = MONUMENT
    filt['museum'] = MUSEUM
    filt['famous'] = FAMOUS
    filt['places_of_worship'] = PLACES_OF_WORSHIP
    filt['zoo'] = ZOO
    return filt

def fetch_priori():
    # Priority is hardcoded
    priority = {}
    priority['famous'] = 1
    priority['monument'] = 2
    priority['museum'] = 15
    priority['places_of_worship'] = 10
    priority['zoo'] = 12


    return priority
#
# def fetch_places(city):
#     places = []
#     if city == 'Jaipur':
#         places.append(Place('Jal Mahal',(26.965604, 75.859205), 4.5, 'monument', 'Jaipur'))
#         places.append(Place('Nehru Bazaar',(26.918636, 75.818895), 4.0, 'market', 'Jaipur'))
#         places.append(Place('City Palace',(26.925771, 75.82658), 4.4, 'museum', 'Jaipur'))
#         places.append(Place('Jantar Mantar',(26.924762,75.824560), 4.4, 'monument', 'Jaipur'))
#         places.append(Place('Hawa Mahal',(26.923936, 75.826744), 4.2, 'monument', 'Jaipur'))
#     elif city == 'Ajmer':
#         places.append(Place('Ajmer Sharif Dargah',(26.456118, 74.628201), 4.4, 'monument', 'Ajmer'))
#         places.append(Place('Adhai Din Ka Jhonpra',(26.455216, 74.625146), 4.2, 'monument', 'Ajmer'))
#         places.append(Place('Ana Sagar Lake',(26.474592, 74.619547), 4.3, 'lake', 'Ajmer'))
#         places.append(Place('Ajmer Jain Temple',(26.464499, 74.632018), 4.1, 'temple', 'Ajmer'))
#         places.append(Place('Daulat Bagh',(26.469087, 74.631626), 4.0, 'park', 'Ajmer'))
#     return places


# def find_distance(current_location, location):
#     # Use Google Maps API to calculate distance
#     K = 0.5 # Speed scaling factor
#     return K*np.sqrt(np.sum(np.square(np.sum(current_location, -1*location))))

def assign_score(places, priority, filt):
    # print(priority)
    # print(filt)
    for place in places:
        R= place.rating
        try:
            P = priority[place.type_of]
        except:
            P = 10

        try:
            F = filt[place.type_of]
        except:
            F = False

        # Cost Assigning Algorithm
        if F:
            SCORE = alpha*(R**2) + beta/((P**2)*(1+np.log(P+10))**2)
        else:
            SCORE = 0
        # print(F,SCORE)
        place.set_score(SCORE)
        # print(SCORE)
    return places

# Get Route recommendation for travelling one city
def get_route(number_of_places, city, filt):
    places = get_places(city)
    priority = fetch_priori()
    places = assign_score(places, priority, filt)

    # Sort in descending order (Rank)
    places.sort(key=operator.attrgetter('score'))
    places= places[::-1]

    # TEST
    # for place in places:
    #     print(place.name+", score: "+str(place.score))

    if number_of_places > len(places):
        number_of_places = len(places) #override
    shortlisted= places[0:number_of_places]

    # Creating a distance matrix for later frequent use
    dist_matrix = np.zeros((len(shortlisted), len(shortlisted)))
    for pos in range(len(shortlisted)):
        for pos2 in range(len(shortlisted)):
            if pos!=pos2:
                dist_matrix[pos, pos2]= find_distance(shortlisted[pos].name+", "+city, shortlisted[pos2].name+", "+city)

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

    # # Adding the distance from current location if available
    # current_location = get_user_location()
    # start_node= current_location
    # if current_location != None:
    #     all_routes = [all_routes[i] + find_distance(current_location, shortlisted[i].location) for i in range(len(shortlisted))]

    start_node = all_routes.index(min(all_routes))

    route=[]
    unvisited = list(range(len(shortlisted)))
    unvisited.remove(start_node)
    pos1 = start_node
    route.append(pos1)
    while len(unvisited)>0:
        temp_dist= [dist_matrix[pos1,pos2] for pos2 in unvisited ]
        closest = min(temp_dist)
        pos1 = unvisited[temp_dist.index(closest)]
        route.append(pos1)
        unvisited.remove(pos1)
        route_dist = route_dist + closest

    # Feedback through initial ranking
    I = list(range(1,len(route)+1))
    I = np.power(I,10)

    rev_route = route[::-1]

    # TEST
    # print(route)
    # print(rev_route)

    sum_route= np.sum(np.multiply(route, I))
    sum_rev_route = np.sum(np.multiply(rev_route, I))

    if sum_rev_route>sum_route:
        route= rev_route

    route = [shortlisted[i] for i in route]
    return route

def get_plan(number_of_days, cities, filt):
    hours_each_day = 8
    NLF = 1.8    # Number limiting factor
    number_of_cities = len(cities)
    hours_for_each_city = (hours_each_day*number_of_days*1.0)/number_of_cities
    number_of_places_per_city = int(hours_for_each_city/NLF)
    plan = {}
    for city in cities:
        plan[city] = get_route(number_of_places_per_city, city, filt)

    #Finding clusters in each City
    # cluster={}
    return plan

# n_days = 1
# cities = ['Jaipur','Ajmer']
# custom_plan = get_plan(n_days, cities, fetch_filter())

# for city in cities:
#     print(city)
#     print('==============================')
#     for place in custom_plan[city]:
#         print(place.name+"|"+str(place.lat)+"|"+str(place.lng))
#     print('------------------------------')
