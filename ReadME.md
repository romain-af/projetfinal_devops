# Task Manager - Projet Final DevOps Data

## Contexte du Projet
Ce projet final a pour objectif de concevoir et déployer une application web simple de gestion de tâches (Task Manager) à l’aide d’un pipeline CI/CD.  
L’idée est de se familiariser avec les fondamentaux de l’intégration et de la livraison continues, la conteneurisation et le déploiement sur un cluster Kubernetes (local ou via un service managé tel qu'AWS EKS).  
Le projet intègre un frontend, un backend et une base de données, et offre des fonctionnalités avancées telles que la priorisation, le marquage en favori, la catégorisation par tags, ainsi qu’un tableau de bord interactif avec des graphiques de statistiques.

## Architecture Générale
L'architecture du projet se décompose en plusieurs composants interconnectés :

- **Frontend**  
  - Application web statique servie par Nginx et stylisée avec Bootstrap.  
  - Interface moderne intégrant un formulaire d'ajout de tâches, des filtres avancés, une liste de tâches et un tableau de bord avec un graphique (via Chart.js).

- **Backend**  
  - API REST développée en Python avec FastAPI qui gère les opérations CRUD sur les tâches.  
  - Gestion des fonctionnalités avancées : priorisation (haute, moyenne, basse), marquage en favori et association de tags pour la catégorisation.

- **Base de Données**  
  - Conteneur PostgreSQL pour la persistance des données.

- **Conteneurisation et Orchestration**  
  - Chaque composant est conteneurisé à l'aide de Docker.  
  - Docker Compose orchestre le démarrage des services en local et facilite la reproduction de l'architecture.

- **Pipeline CI/CD**  
  - Un pipeline automatisé (configuré via GitHub Actions) assure la construction des images Docker, l'exécution des tests unitaires et le déploiement automatique sur un cluster Kubernetes (ou via Docker Compose en local).

### Schéma de l'Architecture

     [Frontend (Nginx, Bootstrap)]
                ↑
                │ (HTTP)
                ↓
     [Backend (FastAPI)]
                ↑
                │ (CRUD API)
                ↓
  [Base de Données (PostgreSQL)]


*Figure 1 : Schéma simplifié de l'architecture (screenshots à intégrer ultérieurement)*

## Étapes pour Lancer le Projet

### Prérequis
- Installation de **Docker** et **Docker Compose**.
- (Optionnel) Un cluster Kubernetes (Minikube ou AWS EKS) configuré pour le déploiement.
- Accès au dépôt GitHub pour déclencher le pipeline CI/CD.

### Installation et Lancement en Local
1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/task-manager.git
   cd task-manager ```

   ## Construire et Lancer les Conteneurs

Depuis la racine du projet (contenant le fichier `docker-compose.yml`), exécutez les commandes suivantes :

```bash
docker-compose up --build -d
 ```

Cette commande construit les images Docker (backend, frontend, etc.) et lance les conteneurs en mode détaché.

Pour vérifier que les services sont actifs, utilisez :

```bash
docker-compose ps
 ```