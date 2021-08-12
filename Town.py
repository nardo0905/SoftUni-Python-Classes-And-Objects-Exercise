class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = ''
        self.longitude = ''

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __repr__(self):
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'
