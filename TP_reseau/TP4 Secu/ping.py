from scapy.all import ICMP,IP,Ether,srp

ping = ICMP(type=8)
packet = IP(src="10.33.76.227", dst="10.33.76.229")
frame = Ether(src="4C:03:4F:88:B2:5B", dst="84:14:4d:0e:5e:b1")
final_frame = frame/packet/ping
answers, unanswered_packets = srp(final_frame, timeout=10)
print(f"Pong reçu : {answers[0]}")

# Execution vers une machine
# C:\Users\Bayle\B2_Matheo\TP4 Secu> python .\ping.py
# Begin emission:
# Finished sending 1 packets.
# .*
# Received 2 packets, got 1 answers, remaining 0 packets
# Pong reçu : QueryAnswer(query=<Ether  dst=84:14:4d:0e:5e:b1 src=4C:03:4F:88:B2:5B type=IPv4 |<IP  frag=0 proto=icmp src=10.33.76.227 dst=10.33.76.229 |<ICMP  type=echo-request |>>>, answer=<Ether  dst=4c:03:4f:88:b2:5b src=84:14:4d:0e:5e:b1 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=28 id=14437 flags= frag=0 ttl=128 proto=icmp chksum=0x5472 src=10.33.76.229 dst=10.33.76.227 |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 |>>>)