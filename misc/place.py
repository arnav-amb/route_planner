
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

    def __init__(self, name, lat, lng, rating, type_of, city, place_id = None, photo = None):
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
