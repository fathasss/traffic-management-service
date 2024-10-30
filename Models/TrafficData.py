# TrafficData.py

class TrafficData:
    def __init__(self):
        self.data = []

    def add_data(self, location, vehicle_count):
        self.data.append({'location': location, 'count': vehicle_count})

    def get_data(self):
        return self.data
