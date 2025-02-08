# Task Manager - Projet Final DevOps Data

## Contexte du Projet
Ce projet final a pour objectif de concevoir et déployer une application web simple de gestion de tâches (Task Manager) à l’aide d’un pipeline CI/CD.  
L’idée est de se familiariser avec les fondamentaux de l’intégration et de la livraison continues, la conteneurisation et le déploiement sur un cluster Kubernetes (local ou via un service managé tel qu'AWS EKS).  
Le projet intègre un frontend, un backend et une base de données, et offre des fonctionnalités avancées telles que la priorisation, le marquage en favori, la catégorisation par tags, ainsi qu’un tableau de bord interactif avec des graphiques de statistiques.

## Architecture du Projet

Le projet se compose de trois composants principaux, orchestrés via Docker et Docker Compose (avec la possibilité de déployer sur un cluster Kubernetes) et intégrés dans un pipeline CI/CD automatisé.

### 1. Frontend
- **Technologies :**
  - HTML, CSS (Bootstrap) et JavaScript.
  - Utilisation de Chart.js pour la visualisation graphique.
- **Fonctionnalités :**
  - Interface de gestion des tâches avec formulaire d'ajout, filtres avancés (par mot-clé, priorité, tags) et tableau de bord interactif.
  - Affichage de la liste des tâches avec options d’édition, suppression (individuelle et multiple), marquage en favori et basculement du statut "terminé".
- **Serveur :**
  - Servi par Nginx dans un conteneur Docker.

### 2. Backend
- **Technologies :**
  - Python et FastAPI pour le développement de l’API REST.
- **Fonctionnalités :**
  - Opérations CRUD sur les tâches.
  - Gestion avancée : priorisation (haute, moyenne, basse), marquage en favori, catégorisation par tags et recherche avancée.
  - Middleware CORS pour permettre l’accès depuis le frontend.
- **Containerisation :**
  - Déployé dans un conteneur Docker via un Dockerfile dédié.

### 3. Base de Données
- **Technologies :**
  - PostgreSQL pour la persistance des données.
- **Déploiement :**
  - Utilisation de l'image officielle PostgreSQL, conteneurisée et orchestrée avec Docker Compose.

---

## Orchestration et Déploiement

- **Conteneurisation :**
  - Chaque composant (frontend, backend, base de données) est conteneurisé à l’aide de Docker.
  
- **Orchestration :**
  - **Docker Compose** est utilisé pour lancer et gérer l’ensemble des conteneurs en local.
  - Possibilité de déploiement sur un cluster Kubernetes (via Minikube, AWS EKS, etc.) en adaptant les manifestes Kubernetes.

- **Pipeline CI/CD :**
  - Configuré avec GitHub Actions, le pipeline automatise :
    - La construction des images Docker pour le frontend et le backend.
    - L'exécution des tests unitaires (notamment pour le backend).
    - Le déploiement automatique sur un cluster Kubernetes (ou via Docker Compose en local) après chaque commit ou fusion.

---

## Schéma de l'Architecture

```plaintext
                   +-------------------------------+
                   |        Frontend               |
                   |  (Nginx, Bootstrap, Chart.js) |
                   +---------------+---------------+
                                   │ HTTP
                                   │
                                   ▼
                   +-------------------------------+
                   |          Backend              |
                   |       (FastAPI, Python)       |
                   +---------------+---------------+
                                   │ CRUD API
                                   │
                                   ▼
                   +-------------------------------+
                   |   Base de Données             |
                   |       (PostgreSQL)            |
                   +-------------------------------+
```


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
   cd task-manager 
    ```

2. **Construire et lancer les conteneurs  :**

    Depuis la racine du projet (contenant le fichier `docker-compose.yml`), exécutez les commandes suivantes :

    ```bash
    docker-compose up --build -d
    ```

Cette commande construit les images Docker (backend, frontend, etc.) et lance les conteneurs en mode détaché.

3. **Vérifier que les services sont actifs   :**

    Pour vérifier que les services sont actifs, utilisez :

    ```bash
    docker-compose ps
    ```

4. **Accéder à l'Application   :**
 
    **Frontend** :
    Ouvrez http://localhost dans votre navigateur.

    **Backend** :
    Accédez à http://localhost:8000/docs pour consulter la documentation interactive de l'API.

    **Déploiement sur Kubernetes**
    Si vous utilisez un cluster Kubernetes (par exemple via AWS EKS), appliquez vos manifestes avec :

    ```bash
    kubectl apply -f kubernetes-manifests/
    ```

## Pipeline CI/CD

Le pipeline CI/CD a été configuré pour automatiser :

### L'intégration continue (CI)
- **Construction des images Docker** pour le backend et le frontend.
- **Exécution des tests unitaires** pour le backend.

### La livraison continue (CD)
- **Déploiement automatique** sur le cluster Kubernetes (ou via Docker Compose en local) après chaque commit ou fusion de code.

### Démonstration du Pipeline
- **Screenshot 1 :** Vue d'ensemble du pipeline CI/CD dans GitHub Actions.
- **Screenshot 2 :** Logs du build et du déploiement montrant la réussite des tests et le déploiement sur le cluster.

*(Les screenshots seront intégrés ultérieurement dans ce document.)*

---

## Résultats

Ce projet final aboutit à une application web complète qui permet :

### Gestion des Tâches
- **Ajout, modification, suppression individuelle** et **suppression multiple** (via sélection de cases).
- **Recherche avancée** avec filtres par mot-clé, priorité et tags.

### Fonctionnalités Avancées
- **Priorisation des tâches** (haute, moyenne, basse) et **marquage en favori**.
- **Association de tags** pour la catégorisation et le filtrage par thème.

### Tableau de Bord et Statistiques
- **Affichage en temps réel** des indicateurs :
  - Nombre total de tâches.
  - Nombre de tâches terminées.
  - Nombre de tâches en cours.
  - Nombre de tâches en retard.
- **Graphique interactif** illustrant la répartition des tâches par priorité.

### Automatisation DevOps
- Un **pipeline CI/CD automatisé** assure la qualité du code et facilite le déploiement continu sur un cluster Kubernetes ou en local via Docker Compose.

---

Ce projet démontre l'intégration réussie des pratiques DevOps modernes : conteneurisation, automatisation et déploiement continu, tout en fournissant une application fonctionnelle et évolutive de gestion de tâches.
