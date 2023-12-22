# TP1 : Maîtrise réseau du poste

## I. Basics

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**

```
PS C:\Users\Bayle> ipconfig /all
[...]
   Adresse physique . . . . . . . . . . . : 4C-03-4F-88-B2-5B
[...]
   Adresse IPv4. . . . . . . . . . . . . .: 172.20.10.2(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.255.240
[...]
```

- ```Adresse physique . . . . . . . . . . . : 4C-03-4F-88-B2-5B```
- ```Adresse IPv4. . . . . . . . . . . . . .: 172.20.10.2(préféré)```
- ``Masque de sous-réseau. . . . . . . . . : 255.255.255.240``
  - en notation CIDR, par exemple `255.255.255.240/28`
  - ET en notation décimale, par exemple `255.255.255.240`

---

☀️ **Déso pas déso**

```
- ``172.20.10.0``
- ``172.20.10.15``
- ``14``
```
---

☀️ **Hostname**

```
PS C:\Users\Bayle> hostname
Ynov-Matheo
```


---

☀️ **Passerelle du réseau**


```
PS C:\Users\Bayle> ipconfig /all
[...]
Passerelle par défaut. . . . . . . . . : fe80::1494:6cff:fe95:d364%10
                                       172.20.10.1
[...]
PS C:\Users\Bayle> arp -a

Interface : 172.20.10.2 --- 0xa
  Adresse Internet      Adresse physique      Type
  172.20.10.1           16-94-6c-95-d3-64     dynamique
```
- `172.20.10.1`
- `16-94-6c-95-d3-64`


---

☀️ **Serveur DHCP et DNS**

```
PS C:\Users\Bayle> ipconfig /all
[...]
Serveur DHCP . . . . . . . . . . . . . : 172.20.10.1
[...]
PS C:\Users\Bayle> arp -a

Interface : 172.20.10.2 --- 0xa
  Adresse Internet      Adresse physique      Type
  172.20.10.1           16-94-6c-95-d3-64     dynamique

```

- `172.20.10.1`
- `16-94-6c-95-d3-64`

---

☀️ **Table de routage**

```
PS C:\Users\Bayle>  netstat -r
[...]
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0      172.20.10.1      172.20.10.2     50
[...]

```
---

# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

```
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

	192.168.64.138  mon-super-site-local
	1.1.1.1         b2.hello.vous
```
```
PS C:\Users\Bayle> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
```


> Vous pouvez éditer en GUI, et juste me montrer le contenu du fichier depuis le terminal pour le compte-rendu.

---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

```
PS C:\Users\Bayle> nslookup youtube.com
Nom :    youtube.com
Addresses:  2a00:1450:4007:80c::200e
          172.217.20.174

PS C:\Users\Bayle> netstat -
[...]
TCP    10.33.76.186:54008     172.217.20.174:443     TIME_WAIT
```

> Il est **fortement** recommandé de couper toutes vos autres connexions internet pour identifier facilement ce trafic (fermez Discord, tous les onglets de vos navigateurs ouverts, etc. Fermez tout ce qui sollicite le réseau.

---

☀️ **Requêtes DNS**

Déterminer...

```
PS C:\Users\Bayle> nslookup www.ynov.com

Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          172.67.74.226
          104.26.10.233
          104.26.11.233
```

> Ca s'appelle faire un "lookup DNS".

```
PS C:\Users\Bayle> nslookup 174.43.238.89

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

> Ca s'appelle faire un "reverse lookup DNS".

---

☀️ **Hop hop hop**

Déterminer...

```
PS C:\Users\Bayle> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [172.67.74.226]
avec un maximum de 30 sauts :

  1     3 ms     1 ms     1 ms  10.33.79.254
  2     1 ms     1 ms     1 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     2 ms     2 ms     4 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     3 ms     5 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    10 ms    11 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    11 ms    18 ms    12 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    11 ms    15 ms    14 ms  141.101.67.48
  8     9 ms    10 ms    10 ms  172.71.124.4
  9    11 ms    10 ms    11 ms  172.67.74.226

Itinéraire déterminé.
```

---

☀️ **IP publique**

```
195.7.117.146

```
---

☀️ **Scan réseau**

Déterminer...


```
PS C:\Users\Bayle> arp -a | select-string 10.33

Interface : 10.33.76.227 --- 0xa
  10.33.65.156          b4-8c-9d-74-d6-27     dynamique
  10.33.68.212          28-cd-c4-ae-00-0f     dynamique
  10.33.69.1            08-d2-3e-35-00-a2     dynamique
  10.33.69.34           c8-58-c0-63-5a-92     dynamique
  10.33.69.48           28-d0-ea-6b-3d-f2     dynamique
  10.33.69.50           70-cd-0d-81-43-d6     dynamique
  10.33.69.103          1c-bf-c0-6d-5d-09     dynamique
  10.33.69.177          d8-c0-a6-26-98-03     dynamique
  10.33.70.118          f8-e4-e3-4a-1a-b9     dynamique
  10.33.70.209          00-93-37-9d-52-7e     dynamique
  10.33.70.211          a0-88-69-de-d7-c6     dynamique
  10.33.71.23           74-4c-a1-d8-c2-59     dynamique
  10.33.71.26           00-41-0e-2b-91-5d     dynamique
  10.33.75.121          f4-26-79-3f-b9-66     dynamique
  10.33.75.126          14-13-33-e1-48-51     dynamique
  10.33.76.134          d8-f8-83-fc-a2-79     dynamique
  10.33.77.21           00-91-9e-4d-0c-7e     dynamique
  10.33.79.138          c4-03-a8-c8-54-97     dynamique
  10.33.79.194          2c-8d-b1-d9-6c-55     dynamique
  10.33.79.197          90-e8-68-d3-6f-8f     dynamique
  10.33.79.198          4c-03-4f-e7-6e-d1     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
```
- soit 23 machines plus moi. 

# III. Le requin

---

☀️ **Capture ARP**


[ARP TRAME](./captures/arp.pcap)
- arp filtre


---

☀️ **Capture DNS**

[DNS TRAME](./captures/dns.pcap)
- dns filtre

---

☀️ **Capture TCP**

[TCP TRAME](./captures/tcp.pcap)
- tcp filtre

---

