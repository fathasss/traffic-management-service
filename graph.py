# graph.py

import matplotlib.pyplot as plt

class TrafficGraph:
    def __init__(self):
        self.locations = []
        self.vehicle_counts = []

    def update_graph(self, location, count):
        if location not in self.locations:
            self.locations.append(location)
            self.vehicle_counts.append(count)
        else:
            index = self.locations.index(location)
            self.vehicle_counts[index] += count

        self.plot_graph()

    def plot_graph(self):
        plt.clf() 
        plt.bar(self.locations, self.vehicle_counts, color='blue')
        plt.xlabel('Location')
        plt.ylabel('Vehicle Count')
        plt.title('Traffic Volume by Location')
        plt.ylim(0, max(self.vehicle_counts) + 10)
        plt.pause(0.1)

