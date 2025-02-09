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
