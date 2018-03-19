
class Place:
    name= None
    location = None
    rating = None
    type_of = None
    city = None
    cost= None

    def __init__(self, name, location, rating, type_of, city):
        self.name= name
        self.location= location
        self.rating= rating
        self.type_of= type_of
        self.city= city

    def set_cost(self, cost):
        self.cost= cost
