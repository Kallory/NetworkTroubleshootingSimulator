
class Node:
    def __init__(self, ip_address, node_type):
        self.ip_address = ip_address
        self.node_type = node_type
        self.status = "up"
        self.connections = []

    def change_status(self, status):
        self.status = status

    def add_connection(self, node):
        self.connections.append(node)

    def simulate_traffic(self):
        pass

    def check_service(self, service_name):
        return f"Service {service_name} is {'running' if self.status == 'up' else 'not running'}"
