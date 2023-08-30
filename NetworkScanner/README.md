# Network Scanner 🔍

This Python script utilizes the power of the `scapy` library to identify devices on your local network. Whether you're a network administrator, a security researcher, or just curious about the devices on your local network, this tool provides valuable insights.

## Description

The Network Scanner script probes devices on the local network to retrieve their IP and MAC addresses. It's a great way to get a snapshot of devices connected to your network, potentially identifying unwanted intruders or simply getting an overview of all connected devices.

## Features

- **Quick Scan**: Efficiently identifies all devices on the local network.
- **Clean Output**: Presents results in a readable format, showcasing IP and MAC addresses.
  
## Prerequisites

This project requires the `npcap` driver/library, which enables packet sniffing on Windows:

- [Download npcap](https://nmap.org/npcap/). During installation, ensure you check the option "Install Npcap in WinPcap API-compatible Mode" for compatibility with the `scapy` library.

## Setup

1. Clone the repository or download the Network Scanner script.
2. Navigate to the project directory.
3. Install the necessary Python libraries:
   
   ```pip install -r requirements.txt```

4. Ensure `npcap` is installed (see Prerequisites above).

## Usage

1. Run the script with administrative privileges (necessary for packet sniffing):

   ```py network_scanner.py```

2. The on-screen prompt will ask for IP range, default should work.

3. View the list of devices on your network, complete with IP and MAC addresses.
