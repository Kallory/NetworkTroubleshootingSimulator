
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
