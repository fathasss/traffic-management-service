# TrafficController.py

class TrafficController:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data

    def analyze_traffic(self):
        alerts = []
        for record in self.traffic_data.get_data():
            if record['count'] > 80:
                alerts.append(f"Alert: High traffic at {record['location']} with {record['count']} vehicles!")
            elif record['count'] < 20:
                alerts.append(f"Notice: Low traffic at {record['location']} with {record['count']} vehicles.")
        return alerts
