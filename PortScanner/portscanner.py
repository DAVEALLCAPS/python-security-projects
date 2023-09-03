import socket

def scan_ports(target_ip, start_port, end_port):
    """Scan ports of a target IP from start_port to end_port."""
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        # Create a new socket using the combined IP and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the socket to prevent hanging
        s.settimeout(1)
        # Attempt to establish a connection
        result = s.connect_ex((target_ip, port))
        
        # If the result is 0, the connection was successful
        if result == 0:
            open_ports.append(port)
        
        s.close()
        
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP to scan: ")
    start = int(input("Enter start port number: "))
    end = int(input("Enter end port number: "))

    open_ports_list = scan_ports(target, start, end)
    
    if open_ports_list:
        print(f"Open ports on {target} are: {', '.join(map(str, open_ports_list))}")
    else:
        print(f"No open ports found on {target} between ports {start} and {end}.")
