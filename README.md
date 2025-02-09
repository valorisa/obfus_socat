# obfus_socat

`obfus_socat` est un projet qui encapsule des connexions via SSL ou SSH, dans le but de fournir des tunnels de communication sécurisés.

## Installation

### Création de l'image Docker

Pour installer les dépendances et créer l'image Docker, commencez par créer un fichier `Dockerfile` dans votre répertoire de projet avec le contenu suivant :

```Dockerfile
# Utiliser une image Python de base
FROM python:3.9-slim

# Installer socat et autres dépendances nécessaires
RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans l'image
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 1080

# Commande par défaut
CMD ["python", "obfus_socat.py"]
```

Ensuite, construisez l'image Docker en exécutant la commande suivante :

```bash
docker build -t obfus_socat .
```

### Exécution du conteneur Docker

Une fois l'image Docker construite, vous pouvez exécuter un conteneur avec la commande suivante :

```bash
docker run -d --name obfus_socat_container -p 1080:1080 -v $(pwd)/config:/app/config obfus_socat
```

Cette commande lance le conteneur en arrière-plan (`-d`), mappe le port 1080 du conteneur sur l'hôte (`-p 1080:1080`) et monte le répertoire de configuration (`-v $(pwd)/config:/app/config`).

## Fichiers de configuration nécessaires

Pour que obfus_socat fonctionne correctement, vous devez disposer des fichiers SSL suivants dans le répertoire `config/` de votre projet :

- `config/server.crt` : Certificat SSL
- `config/server.key` : Clé privée SSL

Ces fichiers sont utilisés pour établir une connexion sécurisée via SSL dans `obfus_socat.py`.

Si vous n'avez pas ces fichiers, vous pouvez les générer en utilisant OpenSSL avec les commandes suivantes :

### Créer une clé privée
```bash
openssl genpkey -algorithm RSA -out config/server.key
```

### Créer un certificat auto-signé
```bash
openssl req -new -key config/server.key -out config/server.csr
openssl x509 -req -in config/server.csr -signkey config/server.key -out config/server.crt
```

Cela générera une clé privée (`server.key`) et un certificat auto-signé (`server.crt`).

## Configuration

Assurez-vous que vous avez les certificats SSL dans le répertoire `config/` comme indiqué ci-dessus.

Ajustez votre `obfus_socat.py` selon les besoins pour différents environnements.

## Utilisation

Voici un exemple d'utilisation de `obfus_socat.py` :

```bash
python obfus_socat.py --mode ssl --local_port 1080 --remote_host example.com --remote_port 443
```

Ce script encapsule une connexion locale sur le port 1080 à une connexion distante via SSL vers `example.com` sur le port 443.

