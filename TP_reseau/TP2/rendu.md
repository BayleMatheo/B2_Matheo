# TP2 : Environnement virtuel

# I. Topologie réseau

## Compte-rendu

☀️ Sur **`node1.lan1.tp2`**

```bash
[node1lan1@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:eb:7e:e2 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:feeb:7ee2/64 scope link
       valid_lft forever preferred_lft forever
```
```bash
[node1lan1@node1 ~]$ ip route show
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3
```
```bash
[node1lan1@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=1.64 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=1.25 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=1.28 ms
64 bytes from 10.1.2.12: icmp_seq=4 ttl=63 time=1.12 ms
^C
--- 10.1.2.12 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 1.116/1.320/1.643/0.195 ms
```
```bash
[node1lan1@node1 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  0.971 ms  0.658 ms  0.435 ms
 2  10.1.2.12 (10.1.2.12)  1.283 ms !X  1.022 ms !X  1.358 ms !X
```

# II. Interlude accès internet


☀️ **Sur `router.tp2`**

```bash
[router@router ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=23.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=24.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=115 time=24.2 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=115 time=23.3 ms
^C
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
```
```bash
[router@router ~]$ ping google.com
PING google.com (142.250.75.238) 56(84) bytes of data.
64 bytes from par10s41-in-f14.1e100.net (142.250.75.238): icmp_seq=1 ttl=116 time=24.3 ms
64 bytes from par10s41-in-f14.1e100.net (142.250.75.238): icmp_seq=2 ttl=116 time=36.8 ms
64 bytes from par10s41-in-f14.1e100.net (142.250.75.238): icmp_seq=3 ttl=116 time=27.0 ms
64 bytes from par10s41-in-f14.1e100.net (142.250.75.238): icmp_seq=4 ttl=116 time=24.5 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3010ms
```

☀️ **Accès internet LAN1 et LAN2**

- sur le lan 1
```bash
[node2lan1@node2 ~]$ sudo ip route add default via 10.1.1.254
```
```bash 
[node2lan1@node2 ~]$ sudo echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```
```bash
[node2lan1@node2 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=24.8 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=114 time=24.4 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=114 time=25.1 ms
^C
--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2008ms
rtt min/avg/max/mdev = 24.392/24.757/25.057/0.275 ms
[node2lan1@node2 ~]$ ping ynov.com
PING ynov.com (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=1 ttl=54 time=24.7 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=2 ttl=54 time=24.4 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=3 ttl=54 time=24.5 ms
^C
--- ynov.com ping statistics ---
```

# III. Services réseau

---

☀️ **Sur `dhcp.lan1.tp2`**

```bash
[node2lan1@node2 ~]$ ip a
[...]
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    inet 10.1.1.253/24 brd 10.1.1.255 scope global secondary noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe65:1837/64 scope link
       valid_lft forever preferred_lft forever
```
```bash
[node2lan1@node2 ~]$ sudo dnf -y install dhcp-server
```

```bash
[node2lan1@node2 ~]$ sudo cat /etc/dhcp/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
# specify domain name
option domain-name "srv.world";
# specify DNS server's hostname or IP address
option domain-name-servers 1.1.1.1;
# default lease time
default-lease-time 600;
# max lease time
max-lease-time 7200;
# this DHCP server to be declared valid
authoritative;
# specify network address and subnetmask
subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range 10.1.1.100 10.1.1.200;
    # specify broadcast address
    option broadcast-address 10.1.1.255;
    # specify gateway
    option routers 10.1.1.254;
```
```bash
[node2lan1@node2 ~]$ sudo systemctl status dhcpd
● dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; enabled; vendor preset: disabled)
     Active: active (running) since Mon 2023-10-23 21:33:46 CEST; 3min 11s ago
[...]
```

☀️ **Sur `node1.lan1.tp2`**

```bash
[node1lan1@node1 ~]$ sudo dnf intall -y dhcp-client
[...]
[node1lan1@node1 ~]$ sudo nmcli connection modify enp0s3 ipv4.method auto
[node1lan1@node1 ~]$ sudo nmcli connection down enp0s3; nmcli connection up enp0s3
```
```bash
[node1lan1@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:eb:7e:e2 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 580sec preferred_lft 580sec
    inet6 fe80::a00:27ff:feeb:7ee2/64 scope link noprefixroute
       valid_lft forever preferred_lft forever

[node1lan1@node1 ~]$ ip route
default via 10.1.1.254 dev enp0s3 proto dhcp src 10.1.1.100 metric 100
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.100 metric 100
```
```bash
[node1lan1@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=1.34 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=1.09 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=1.07 ms
^C
--- 10.1.2.12 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2123ms
rtt min/avg/max/mdev = 1.070/1.166/1.339/0.122 ms
```

## 2. Web web web

---

☀️ **Sur `web.lan2.tp2`**

```bash
[node2lan2@node2 ~]$ sudo dnf install nginx
```
```bash
[node2lan2@node2 ~]$ sudo mkdir -p /var/www/site_nul/
```
```bash
[node2lan2@node2 ~]$ sudo mkdir /etc/nginx/sites-available
[node2lan2@node2 ~]$ sudo mkdir /etc/nginx/sites-enabled
```
```bash
[node2lan2@node2 ~]$ sudo nano /etc/nginx/sites-available/site_nul
server {
    listen 80;
    server_name site_nul.tp2;

    location / {
        root /var/www/site_nul;
        index index.html;
    }
}
```

```bash
[node2lan2@node2 ~]$ sudo systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; disabled; vendor preset: disabled)
     Active: active (running) since Mon 2023-10-23 22:16:43 CEST; 1s ago
    Process: 14411 ExecStartPre=/usr/bin/rm -f /run/nginx.pid (code=exited, status=0/SUCCESS)
    Process: 14412 ExecStartPre=/usr/sbin/nginx -t (code=exited, status=0/SUCCESS)
```
```bash
[node2lan2@node2 ~]$ sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
success
[node2lan2@node2 ~]$ sudo firewall-cmd --reload
success
```
```bash
[node2lan2@node2 ~]$ ss -tuln | grep ':80'
tcp   LISTEN 0      511          0.0.0.0:80        0.0.0.0:*
tcp   LISTEN 0      511             [::]:80           [::]:*
```
```bash
[node2lan2@node2 ~]$ sudo firewall-cmd --list-ports
80/tcp
```

☀️ **Sur `node1.lan1.tp2`**

```bash
[node1lan1@node1 ~]$ sudo cat /etc/hosts
10.1.2.11    site_nul.tp2
[node1lan1@node1 ~]$ ping site_nul.tp2
PING site_nul.tp2 (10.1.2.11) 56(84) bytes of data.
64 bytes from site_nul.tp2 (10.1.2.11): icmp_seq=1 ttl=63 time=1.41 ms
64 bytes from site_nul.tp2 (10.1.2.11): icmp_seq=2 ttl=63 time=1.12 ms
64 bytes from site_nul.tp2 (10.1.2.11): icmp_seq=3 ttl=63 time=1.12 ms
```



