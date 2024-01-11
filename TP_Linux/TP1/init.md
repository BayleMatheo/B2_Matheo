# I. Init

- [I. Init](#i-init)
  - [1. Installation de Docker](#1-installation-de-docker)
  - [2. Vérifier que Docker est bien là](#2-vérifier-que-docker-est-bien-là)
  - [3. sudo c pa bo](#3-sudo-c-pa-bo)
  - [4. Un premier conteneur en vif](#4-un-premier-conteneur-en-vif)
  - [5. Un deuxième conteneur en vif](#5-un-deuxième-conteneur-en-vif)

## 1. Installation de Docker


## 2. Vérifier que Docker est bien là


## 3. sudo c pa bo


🌞 **Ajouter votre utilisateur au groupe `docker`**

```bash
[matheo@docker ~]$ sudo usermod -aG docker $USER
```

## 4. Un premier conteneur en vif


🌞 **Lancer un conteneur NGINX**

- avec la commande suivante :

```bash
[matheo@docker ~]$ docker run -d -p 9999:80 nginx
```
```bash
$ docker run -d -p 9999:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
af107e978371: Pull complete
[SNIP...]
7b73345df136: Pull complete
Digest: sha256:2bdc49f2f8ae8d8dc50ed00f2ee56d00385c6f8bc8a8b320d0a294d9e3b49026
Status: Downloaded newer image for nginx:latest
667542cbc66ccb28e20f8cc840c10c4bd816e7c4adf859423d105403597c48b3
```

🌞 **Visitons**

- vérifier que le conteneur est actif avec une commande qui liste les conteneurs en cours de fonctionnement
```bash
[matheo@docker ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
667542cbc66c   nginx     "/docker-entrypoint.…"   33 seconds ago   Up 32 seconds   0.0.0.0:9999->80/tcp, :::9999->80/tcp   charming_edison
```
- afficher les logs du conteneur
```bash
[matheo@docker ~]$ docker logs 66
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
[SNIP...]
```

- afficher toutes les informations relatives au conteneur avec une commande `docker inspect`
```bash
[matheo@docker ~]$ docker inspect 66
[
    {
        "Id": "667542cbc66ccb28e20f8cc840c10c4bd816e7c4adf859423d105403597c48b3",
        "Created": "2024-01-11T22:48:58.299612844Z",
        [SNIP...]
    }
]
```

- afficher le port en écoute sur la VM avec un `sudo ss -lnpt`
```bash
[matheo@docker ~]$ sudo ss -ltnp | grep docker
[sudo] password for matheo:
LISTEN 0      4096         0.0.0.0:9999      0.0.0.0:*    users:(("docker-proxy",pid=3872,fd=4))
LISTEN 0      4096            [::]:9999         [::]:*    users:(("docker-proxy",pid=3878,fd=4)) 
```
- ouvrir le port `9999/tcp` (vu dans le `ss` au dessus normalement) dans le firewall de la VM
```
$ [matheo@docker ~]$ sudo firewall-cmd --add-port=9999/tcp
```
- depuis le navigateur de votre PC, visiter le site web sur `http://IP_VM:9999`
```bash
$ curl localhost:9999
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

🌞 **On va ajouter un site Web au conteneur NGINX**


```html
<h1>MEOOOW</h1>
```

- config NGINX minimale pour servir un nouveau site web dans `site_nul.conf` :

```nginx
server {
    listen        8080;

    location / {
        root /var/www/html/index.html;
    }
}
```


```bash
[matheo@docker nginx]$ docker run -d -p 9999:8080 -v /home/matheo/nginx/index.html:/var/www/html/index.html -v /home/matheo/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
2344df0a9cf0f992124a52a8b6243be0f2a925fd04f1abad7173ab9470b7b2b5
```

🌞 **Visitons**

- vérifier que le conteneur est actif
```bash
[matheo@docker nginx]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                               NAMES
2344df0a9cf0   nginx     "/docker-entrypoint.…"   9 seconds ago   Up 7 seconds   80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   nervous_einstein
```
- aucun port firewall à ouvrir : on écoute toujours port 9999 sur la machine hôte (la VM)
- visiter le site web depuis votre PC

```
$ curl localhost:9999
<h1>MEOMEO</h1>
```

## 5. Un deuxième conteneur en vif



🌞 **Lance un conteneur Python, avec un shell**

```
[matheo@docker nginx]$ cd
[matheo@docker ~]$ docker run -it python bash
Unable to find image 'python:latest' locally
latest: Pulling from library/python
1b13d4e1a46e: Pull complete
[SNIP...]
c924028f9b63: Pull complete
Digest: sha256:f964ddcb8416013f62f4b7a8c72a332ba4ccd284e39c263ea7bc0375ca8f2c4b
Status: Downloaded newer image for python:latest
root@a3c11fcc0e87:/#
```

🌞 **Installe des libs Python**

- une fois que vous avez lancé le conteneur, et que vous êtes dedans avec `bash`
- installez deux libs, elles ont été choisies complètement au hasard (avec la commande `pip install`):
- `aiohttp`
```
root@a3c11fcc0e87:/# pip install aiohttp
```
  - `aioconsole`
```
root@a3c11fcc0e87:/# pip install aioconsole
```
- tapez la commande `python` pour ouvrir un interpréteur Python
- taper la ligne `import aiohttp` pour vérifier que vous avez bien téléchargé la lib
```
root@a3c11fcc0e87:/# python
Python 3.12.1 (main, Jan 11 2024, 09:52:34) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import aiohttp
```

> *Notez que la commande `pip` est déjà présente. En effet, c'est un conteneur `python`, donc les mecs qui l'ont construit ont fourni la commande `pip` avec !*

➜ **Tant que t'as un shell dans un conteneur**, tu peux en profiter pour te balader. Tu peux notamment remarquer :

- si tu fais des `ls` un peu partout, que le conteneur a sa propre arborescence de fichiers
- si t'essaies d'utiliser des commandes usuelles un poil évoluées, elles sont pas là
  - genre t'as pas `ip a` ou ce genre de trucs
  - un conteneur on essaie de le rendre le plus léger possible
  - donc on enlève tout ce qui n'est pas nécessaire par rapport à un vrai OS
  - juste une application et ses dépendances