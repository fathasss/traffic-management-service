# main.py

#%%

import threading
import tkinter as tk
from tkinter import scrolledtext
import time

from matplotlib import pyplot as plt
from Sensors.TrafficSensor import TrafficSensor
from Models.TrafficData import TrafficData
from Controllers.TrafficController import TrafficController
from graph import TrafficGraph

class TrafficManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Management System")

        self.traffic_data = TrafficData()
        self.traffic_graph = TrafficGraph()

        self.text_area = scrolledtext.ScrolledText(master, width=50, height=20)
        self.text_area.pack()

        self.sensor1 = TrafficSensor("Intersection A")
        self.sensor2 = TrafficSensor("Intersection B")

        self.start_sensors()

        self.analyze_button = tk.Button(master, text="Analyze Traffic", command=self.analyze_traffic)
        self.analyze_button.pack()

    def start_sensors(self):
        threading.Thread(target=self.run_sensor, args=(self.sensor1,), daemon=True).start()
        threading.Thread(target=self.run_sensor, args=(self.sensor2,), daemon=True).start()

    def run_sensor(self, sensor):
        while True:
            vehicle_count = sensor.get_vehicle_count()
            self.traffic_data.add_data(sensor.location, vehicle_count)
            self.traffic_graph.update_graph(sensor.location, vehicle_count)
            time.sleep(5)

    def analyze_traffic(self):
        alerts = TrafficController(self.traffic_data).analyze_traffic()
        self.text_area.delete(1.0, tk.END)
        for alert in alerts:
            self.text_area.insert(tk.END, alert + '\n')

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficManagementApp(root)

    plt.ion()
    plt.figure()

    root.mainloop()

# %%
