FROM nginx:alpine

# Supprime le fichier par défaut (optionnel) et copie votre index.html
RUN rm /usr/share/nginx/html/index.html
COPY index.html /usr/share/nginx/html/index.html

# Exposition du port 80
EXPOSE 80
