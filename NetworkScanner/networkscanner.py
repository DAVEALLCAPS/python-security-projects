import scapy.all as scapy

def scan(ip):
    # ARP request packet to get MAC address corresponding to an IP address
    arp_request = scapy.ARP(pdst=ip)
    # Ethernet frame to transport the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast/arp_request
    # Send the packet and capture the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_info)

    return devices_list

def display_result(devices_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices_list:
        print(device["ip"] + "\t\t" + device["mac"])

if __name__ == "__main__":
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.1/24): ")
    scan_result = scan(ip_range)
    display_result(scan_result)
