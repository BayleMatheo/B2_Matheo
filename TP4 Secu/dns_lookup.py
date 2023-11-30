from scapy.all import Ether, IP, UDP, DNS, DNSQR, srp

def dns_lookup(query_domain):
    eth_layer = Ether()
    ip_layer = IP(src="10.33.76.227", dst="10.1.1.15")
    udp_layer = UDP(sport=12345, dport=53)
    dns_layer = DNS(rd=1, qd=DNSQR(qname=query_domain, qtype="A"))
    packet = eth_layer / ip_layer / udp_layer / dns_layer
    response, _ = srp(packet, timeout=2)
    response.show()

dns_lookup("ynov.com")
