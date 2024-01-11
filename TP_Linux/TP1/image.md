# II. Images

- [II. Images](#ii-images)
  - [1. Images publiques](#1-images-publiques)
  - [2. Construire une image](#2-construire-une-image)

## 1. Images publiques

🌞 **Récupérez des images**


```bash
[matheo@docker]$ history
[SNIP...]
   72  docker pull python
   73  docker pull python:3.11
   74  docker pull mysql:5.7
   75  docker pull wordpress:latest
   76  docker pull linuxserver/wikijs
```
```bash
[matheo@docker ~]$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
linuxserver/wikijs   latest    218ef3649e4d   6 days ago     441MB
mysql                5.7       5107333e08a8   4 weeks ago    501MB
python               latest    ddb6e9772fb2   4 weeks ago    1.02GB
wordpress            latest    9071407ed1c0   5 weeks ago    740MB
python               3.11      1a88ceb967e0   5 weeks ago    1.01GB
nginx                latest    d453dd892d93   2 months ago   187MB
hello-world          latest    d2c94e258dcb   8 months ago   13.3kB
```

🌞 **Lancez un conteneur à partir de l'image Python**

```bash
[matheo@docker ~]$ docker run -it python:3.11 bash
root@ff4eb5c4b12c:/# python --version
Python 3.11.7
```
## 2. Construire une image

Pour construire une image il faut :

- créer un fichier `Dockerfile`
- exécuter une commande `docker build` pour produire une image à partir du `Dockerfile`

🌞 **Ecrire un Dockerfile pour une image qui héberge une application Python**
```
FROM debian

RUN apt-get update -y && apt install -y python3

RUN apt install -y python3-emoji

COPY app.py /home/app.py

ENTRYPOINT ["python3", "/home/app.py"]
```

🌞 **Build l'image**

```bash
[matheo@docker python_app_build]$ docker build . -t python_app:1
[+] Building 13.8s (9/9) FINISHED                                                                                                docker:default
[SNIP...]
```

🌞 **Lancer l'image**

```
[matheo@docker python_app_build]$ docker run python_app:1
Cet exemple d'application est vraiment naze 👎
```