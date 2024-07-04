from scapy.all import *

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

        # Check if the packet has a payload
        if packet.haslayer(Raw):
            payload = packet.getlayer(Raw).load
            print(f"Payload: {payload}")
        print("\n")

# Sniff packets and use the callback function
sniff(prn=packet_callback, store=0)
