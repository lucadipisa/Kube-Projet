# Image pour Python
FROM python:3.9-slim

# Créez et définir le répertoire de travail
WORKDIR /app

# Copiez le fichier des dépendances et installez-les
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste du code source
COPY . .

# Exposez le port sur lequel le serveur Flask fonctionnera
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]