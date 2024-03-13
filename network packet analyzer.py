import scapy.all as scapy

def sniff_packets(interface):
    print("Sniffing packets on interface:", interface)
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol} | Payload: {payload}")
        else:
            print(f"Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol}")

def main():
    interface = input("Enter the interface to sniff packets…
