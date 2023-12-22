from scapy.all import sniff

def print_it_please(packet):
        packet_source_ip = packet['IP'].src
        packet_dst_ip = packet['IP'].dst
        port_src = packet['TCP'].sport
        port_dst = packet['TCP'].dport
        print(f"""
TCP SYN ACK reçu !
- Adresse IP src : {packet_source_ip}
- Adresse IP dst : {packet_dst_ip}
- Port TCP src : {port_src}
- Port TCP dst : {port_dst}
        """)

sniff(filter="tcp and src host 1.1.1.1", prn=print_it_please, count=1)

# PS C:\Users\Bayle\B2_Matheo\TP4 Secu> py.exe .\tcp_cap.py
# recherche internet 1.1.1.1

# TCP SYN ACK reçu !
# - Adresse IP src : 1.1.1.1
# - Adresse IP dst : 10.33.76.227
# - Port TCP src : 80
# - Port TCP dst : 56902