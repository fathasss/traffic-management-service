# TrafficSensor.py

import random
import time

class TrafficSensor:
    def __init__(self, location):
        self.location = location

    def get_vehicle_count(self):
        return random.randint(0, 100)
