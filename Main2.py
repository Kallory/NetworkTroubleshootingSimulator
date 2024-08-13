from Node import Node
from NetworkTechnician import NetworkTechnician
from NetworkTopology import NetworkTopology
from ProgramAdmin import ProgramAdmin

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
            print("\nNetwork Technician Mode active")
            print("Type /help for help or /help <tool name> for help about a particular tool.")
            
            commandInput = input("")
            commandParts = commandInput.split(' ', 1)
            command = commandParts[0]

            if command == "/help"
                # display help file
            elif command == "/ping"
                # ping command, check for args and process with network_technician.ping(args)
               
          #  print("command was: " + commandParts[0]) 
          #  print("first argument was: " + commandParts[1])    
          
          #  print("\nSelect tool:")
          #  print("1. Ping")
          #  print("2. Tracert")
          #  print("3. NSLookup")
          #  print("4. Check Service")
          #  command = input("Enter choice: ")
          #  
          #  if command == "1":
          #      ip = input("Enter IP address to ping: ")
          #      network_technician.ping(ip)
          #  elif command == "2":
          #      ip = input("Enter IP address to tracert: ")
          #      network_technician.tracert(ip)
          #  elif command == "3":
          #      domain = input("Enter domain name for NSLookup: ")
          #      network_technician.nslookup(domain)
          #  elif command == "4":
          #      ip = input("Enter IP address to check service: ")
          #      service = input("Enter service name: ")
          #      network_technician.check_service(ip, service)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

