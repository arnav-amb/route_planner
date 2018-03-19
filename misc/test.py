from place import Place
import numpy as np
import operator


# PARAMETERS FOR FINE TUNING
alpha= 20
beta= 500


def fetch_priori():
    priority={}
    priority['monument']=1
    priority['market']=3
    priority['museum']=2
    return priority

def fetch_places(city):
    places=[]
    if city == 'Jaipur':
        places.append(Place('Jal Mahal',(26.965604, 75.859205), 4.5, 'monument', 'Jaipur'))
        places.append(Place('Nehru Bazaar',(26.918636, 75.818895), 4.0, 'market', 'Jaipur'))
        places.append(Place('City Palace',(26.925771, 75.82658), 4.4, 'museum', 'Jaipur'))
        places.append(Place('Jantar Mantar',(26.924762,75.824560), 4.4, 'monument', 'Jaipur'))
        places.append(Place('Hawa Mahal',(26.923936, 75.826744), 4.2, 'monument', 'Jaipur'))
    elif city == 'Ajmer':
        places.append(Place('Ajmer Sharif Dargah',(26.456118, 74.628201), 4.4, 'monument', 'Ajmer'))
        places.append(Place('Adhai Din Ka Jhonpra',(26.455216, 74.625146), 4.2, 'monument', 'Ajmer'))
        places.append(Place('Ana Sagar Lake',(26.474592, 74.619547), 4.3, 'lake', 'Ajmer'))
        places.append(Place('Ajmer Jain Temple',(26.464499, 74.632018), 4.1, 'temple', 'Ajmer'))
        places.append(Place('Daulat Bagh',(26.469087, 74.631626), 4.0, 'park', 'Ajmer'))

    return places

# def get_user_location():
#     # None if user does not want to give his location or if user is too far away
#     return (26.914125, 75.804636)


def find_distance(current_location, location):
    # Use Google Maps API to calculate distance
    K = 0.5 # Speed scaling factor
    return K*np.sqrt(np.sum(np.square(np.sum(current_location, -1*location))))

def assign_score(places, priority):
    for place in places:
        R= place.rating
        try:
            P = priority[place.type_of]
        except:
            P = 5
        # Cost Assigning Algorithm
        SCORE = alpha*(R**2) + beta/np.log(P+1)
        place.set_score(SCORE)
        # print(SCORE)
    return places

# Get Route recommendation for travelling one city
def get_route(number_of_places, city, priority):
    priority = fetch_priori()
    places = fetch_places(city)
    places = assign_score(places, priority)

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

def get_plan(number_of_days, cities, priority):
    hours_each_day = 8
    NLF = 1.8    # Number limiting factor
    number_of_cities = len(cities)
    hours_for_each_city = (hours_each_day*number_of_days*1.0)/number_of_cities
    number_of_places_per_city = int(hours_for_each_city/NLF)
    plan = {}
    for city in cities:
        plan[city] = get_route(number_of_places_per_city, city, priority)
    return plan

cities = ['Jaipur', 'Ajmer']
custom_plan = get_plan(2, cities, fetch_priori())

for city in cities:
    print(city)
    print('==============================')
    for place in custom_plan[city]:
        print(place.name)
    print('------------------------------')
