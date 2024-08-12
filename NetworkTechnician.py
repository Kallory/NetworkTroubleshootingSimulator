
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
