# III. Docker compose

Pour la fin de ce TP on va manipuler un peu `docker compose`.

🌞 **Créez un fichier `docker-compose.yml`**

- dans un nouveau dossier dédié `/home/<USER>/compose_test`
- le contenu est le suivant :

```yml
version: "3"

services:
  conteneur_nul:
    image: debian
    entrypoint: sleep 9999
  conteneur_flopesque:
    image: debian
    entrypoint: sleep 9999
```


🌞 **Lancez les deux conteneurs** avec `docker compose`

```bash
[matheo@docker compose_test]$ docker compose up -d
[+] Running 3/3
 ✔ conteneur_nul 1 layers [⣿]      0B/0B      Pulled                                                                                       2.7s
   ✔ 1b13d4e1a46e Already exists                                                                                                           0.0s
 ✔ conteneur_flopesque Pulled                                                                                                              2.7s
[+] Running 3/3
 ✔ Network compose_test_default                  Created                                                                                   0.2s
 ✔ Container compose_test-conteneur_nul-1        Started                                                                                   0.1s
 ✔ Container compose_test-conteneur_flopesque-1  Started
```

🌞 **Vérifier que les deux conteneurs tournent**

```bash
[matheo@docker compose_test]$ docker ps
CONTAINER ID   IMAGE     COMMAND        CREATED          STATUS          PORTS     NAMES
c372e5a12d65   debian    "sleep 9999"   19 seconds ago   Up 18 seconds             compose_test-conteneur_nul-1
abb004554e25   debian    "sleep 9999"   19 seconds ago   Up 18 seconds             compose_test-conteneur_flopesque-1
```

🌞 **Pop un shell dans le conteneur `conteneur_nul`**
```bash
[matheo@docker compose_test]$ docker exec -it compose_test-conteneur_nul-1 bash
root@c372e5a12d65:/#
```
```
root@c372e5a12d65:/# apt update && apt install iputils-ping
```
```
root@c372e5a12d65:/# ping -c 1 compose_test-conteneur_flopesque-1
PING compose_test-conteneur_flopesque-1 (172.18.0.3) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.3): icmp_seq=1 ttl=64 time=0.083 ms

--- compose_test-conteneur_flopesque-1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.083/0.083/0.083/0.000 ms

```