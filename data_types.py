class Purchase:
    def __init__(self, street, city, zip, state, beds, baths,
                 sq__ft, home_type, sale_date, price,
                 latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date
        self.home_type = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip = zip
        self.city = city
        self.street = street

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude']))


# class Purchase:
#     def __init__(self, street, city, zip, state, beds, baths,
#                  sq__ft, home_type, sale_date, price,
#                  latitude, longitude):
#         self.longitude = longitude
#         self.latitude = latitude
#         self.price = price
#         self.sale_date = sale_date
#         self.home_type = home_type
#         self.sq__ft = sq__ft
#         self.baths = baths
#         self.beds = beds
#         self.state = state
#         self.zip = zip
#         self.city = city
#         self.street = street
#
#     # this method works with the DictReader
#     @staticmethod
#     def create_from_dict(lookup):
#         return Purchase(
#             lookup['street'],
#             lookup['city'],
#             lookup['zip'],
#             lookup['state'],
#             int(lookup['beds']),
#             int(lookup['baths']),
#             int(lookup['sq__ft']),
#             lookup['type'],
#             lookup['sale_date'],
#             float(lookup['price']),
#             float(lookup['latitude']),
#             float(lookup['longitude']))
