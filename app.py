#%%

from flask import Flask, jsonify, request
import threading
import time
from Sensors.TrafficSensor import TrafficSensor
from Models.TrafficData import TrafficData
from Controllers.TrafficController import TrafficController

app = Flask(__name__)

# Global değişkenler
traffic_data = TrafficData()
sensor1 = TrafficSensor("Intersection A")
sensor2 = TrafficSensor("Intersection B")

def run_sensor(sensor):
    while True:
        vehicle_count = sensor.get_vehicle_count()
        traffic_data.add_data(sensor.location, vehicle_count)
        time.sleep(5)

@app.route('/api/traffic_data', methods=['GET'])
def get_traffic_data():
    return jsonify(traffic_data.data)

@app.route('/api/analyze_traffic', methods=['POST'])
def analyze_traffic():
    alerts = TrafficController(traffic_data).analyze_traffic()
    return jsonify(alerts)

@app.route('/api/ddos_mitigation', methods=['GET'])
def handle_ddos_mitigation():
    alerts = mitigate_ddos()
    return jsonify(alerts)

def mitigate_ddos():
    alerts = []
    threshold = 100

    for location, count in traffic_data.data.items():
        if count > threshold:
            alerts.append(f"DDoS Alert: High traffic at {location} with {count} vehicles!")

    return alerts

if __name__ == "__main__":
    threading.Thread(target=run_sensor, args=(sensor1,), daemon=True).start()
    threading.Thread(target=run_sensor, args=(sensor2,), daemon=True).start()
    app.run(debug=True, host='0.0.0.0', port=5000)

# %%
