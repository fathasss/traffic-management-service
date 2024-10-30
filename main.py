#%%

import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
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
        self.master.geometry("600x500") 

        self.traffic_data = TrafficData()
        self.traffic_graph = TrafficGraph()

        # Metin alanı
        self.text_area = scrolledtext.ScrolledText(master, width=50, height=15, font=("Arial", 10))
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Sensörler
        self.sensor1 = TrafficSensor("Intersection A")
        self.sensor2 = TrafficSensor("Intersection B")

        # Düğmeler
        self.analyze_button = tk.Button(master, text="Analyze Traffic", command=self.analyze_traffic, bg="lightblue")
        self.analyze_button.grid(row=1, column=0, padx=10, pady=10)

        self.ddos_button = tk.Button(master, text="Mitigate DDoS", command=self.handle_ddos_mitigation, bg="lightcoral")
        self.ddos_button.grid(row=1, column=1, padx=10, pady=10)

        self.start_sensors()

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

    def handle_ddos_mitigation(self):
        alerts = self.mitigate_ddos()
        if alerts:
            self.text_area.delete(1.0, tk.END)
            for alert in alerts:
                self.text_area.insert(tk.END, alert + '\n')
        else:
            messagebox.showinfo("DDoS Mitigation", "No DDoS threats detected.")

    def mitigate_ddos(self):
        alerts = []
        threshold = 100

        for location, count in self.traffic_data.data.items():
            if count > threshold:
                alerts.append(f"DDoS Alert: High traffic at {location} with {count} vehicles!")

        return alerts

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficManagementApp(root)

    plt.ion()
    plt.figure()

    root.mainloop()

# %%
