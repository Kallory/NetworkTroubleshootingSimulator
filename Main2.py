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


class NetworkTopology:
    def __init__(self):
        self.nodes = {}

    def add_node(self, ip_address, node_type):
        node = Node(ip_address, node_type)
        self.nodes[ip_address] = node

    def connect_nodes(self, ip_address1, ip_address2):
        node1 = self.nodes.get(ip_address1)
        node2 = self.nodes.get(ip_address2)
        if node1 and node2:
            node1.add_connection(node2)
            node2.add_connection(node1)

    def find_route(self, start_ip, end_ip):
        # For demonstration purposes, we'll return a simple route
        return [start_ip, "intermediate_node", end_ip]

    def simulate_congestion(self, ip_address):
        pass


class ProgramAdmin:
    def __init__(self, network):
        self.network = network

    def simulate_problem(self, command):
        ip_address, action = command.split()
        if action == "down":
            self.bring_node_down(ip_address)
        elif action == "up":
            self.bring_node_up(ip_address)

    def bring_node_down(self, ip_address):
        node = self.network.nodes.get(ip_address)
        if node:
            node.change_status("down")
            print(f"Node {ip_address} is now down.")

    def bring_node_up(self, ip_address):
        node = self.network.nodes.get(ip_address)
        if node:
            node.change_status("up")
            print(f"Node {ip_address} is now up.")


class NetworkTechnician:
    def __init__(self, network):
        self.network = network

    def ping(self, ip_address):
        node = self.network.nodes.get(ip_address)
        if node:
            status = "reachable" if node.status == "up" else "unreachable"
            print(f"Ping to {ip_address}: {status}")
        else:
            print(f"Node {ip_address} not found.")

    def tracert(self, ip_address):
        route = self.network.find_route("192.168.1.2", ip_address)
        print(f"Traceroute to {ip_address}: {' -> '.join(route)}")

    def nslookup(self, domain_name):
        # For demonstration, we'll just echo the domain name and a fake IP
        print(f"NSLookup {domain_name}: 192.168.1.3")

    def check_service(self, ip_address, service_name):
        node = self.network.nodes.get(ip_address)
        if node:
            result = node.check_service(service_name)
            print(result)
        else:
            print(f"Node {ip_address} not found.")


def main():
    # Initialize network topology
    network = NetworkTopology()

    # Add nodes
    network.add_node("192.168.1.1", "Router")
    network.add_node("192.168.1.2", "PC")
    network.add_node("192.168.1.3", "Server")

    # Connect nodes
    network.connect_nodes("192.168.1.1", "192.168.1.2")
    network.connect_nodes("192.168.1.1", "192.168.1.3")

    # Initialize program admin and technician
    program_admin = ProgramAdmin(network)
    network_technician = NetworkTechnician(network)

    while True:
        print("\nSelect mode:")
        print("1. Program Admin")
        print("2. Network Technician")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            command = input("Enter admin command (e.g., '192.168.1.2 down'): ")
            program_admin.simulate_problem(command)

        elif choice == "2":
            print("\nSelect tool:")
            print("1. Ping")
            print("2. Tracert")
            print("3. NSLookup")
            print("4. Check Service")
            tool_choice = input("Enter choice: ")

            if tool_choice == "1":
                ip = input("Enter IP address to ping: ")
                network_technician.ping(ip)
            elif tool_choice == "2":
                ip = input("Enter IP address to tracert: ")
                network_technician.tracert(ip)
            elif tool_choice == "3":
                domain = input("Enter domain name for NSLookup: ")
                network_technician.nslookup(domain)
            elif tool_choice == "4":
                ip = input("Enter IP address to check service: ")
                service = input("Enter service name: ")
                network_technician.check_service(ip, service)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

