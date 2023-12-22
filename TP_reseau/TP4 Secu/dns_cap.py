from scapy.all import sniff, DNS

def print_dns_response(packet):
    if DNS in packet and packet[DNS].qr:
        query_name = packet[DNS].qd.qname.decode()  
        response_ip = packet[DNS].an.rdata.decode()
        print(f"""
DNS Request and Response captured!
- Query Name: {query_name}
- Response IP: {response_ip}
        """)

sniff(filter="udp and port 53", prn=print_dns_response, count=2)
