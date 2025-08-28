# CHRONOS - Gestion des Heures Supplémentaires

## Description

**ChronosRH** est un système moderne de gestion des heures supplémentaires développé avec FastAPI (backend) et React (frontend). Il offre une interface intuitive pour la gestion complète des demandes d'heures supplémentaires avec un workflow d'approbation robuste.

## Fonctionnalités

- 🔐 **Authentification** : Système de login sécurisé avec JWT
- 👥 **Gestion des employés** : CRUD complet des employés
- 🏢 **Gestion des services** : Organisation hiérarchique des départements
- ⏰ **Demandes d'heures supplémentaires** : Création et gestion des demandes
- ✅ **Workflow d'approbation** : Système de validation à plusieurs niveaux
- 🎯 **Tableau de bord** : Vue d'ensemble avec statistiques
- 📱 **Interface responsive** : Design adaptatif avec Tailwind CSS
- 🔄 **Migrations automatiques** : Gestion des versions de base de données avec Alembic
- 🐳 **Containerisation** : Déploiement facile avec Docker
- 📊 **Monitoring** : Health checks et logs structurés

## Architecture

### Backend (FastAPI)
- **Framework** : FastAPI avec Python 3.11+
- **Base de données** : MySQL avec SQLAlchemy ORM
- **Authentification** : JWT avec python-jose
- **Validation** : Pydantic schemas
- **Documentation** : Swagger UI automatique
- **Migrations** : Alembic pour la gestion des versions DB

### Frontend (React)
- **Framework** : React 18 avec hooks
- **Routing** : React Router DOM
- **State management** : React Query pour les données serveur
- **Styling** : Tailwind CSS
- **Forms** : React Hook Form
- **Notifications** : React Hot Toast
- **Build** : Vite pour un développement rapide

## Installation

### Prérequis
- Docker et Docker Compose
- Node.js 18+ (pour développement local)
- Python 3.11+ (pour développement local)
- MySQL 8.0+ (si installation manuelle)

### Démarrage rapide avec Docker

1. **Cloner le projet**
   ```bash
   git clone <repo-url>
   cd chronos-rh
   ```

2. **Configurer les variables d'environnement**
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   # Modifier les fichiers .env selon vos besoins
   ```

3. **Démarrer avec Docker**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

   Ou manuellement :
   ```bash
   docker-compose up --build -d
   ```

### Installation manuelle

#### Backend

1. **Créer un environnement virtuel**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement**
   ```bash
   cp .env.example .env
   # Modifier le fichier .env avec vos paramètres
   ```

4. **Initialiser la base de données**
   ```bash
   # Créer la base de données MySQL
   mysql -u root -p -e "CREATE DATABASE ghs_db;"
   
   # Appliquer les migrations
   alembic upgrade head
   ```

5. **Démarrer le serveur**
   ```bash
   uvicorn app.main:app --reload
   ```

#### Frontend

1. **Installer les dépendances**
   ```bash
   cd frontend
   npm install
   ```

2. **Configurer les variables d'environnement**
   ```bash
   cp .env.example .env
   # Modifier le fichier .env si nécessaire
   ```

3. **Démarrer le serveur de développement**
   ```bash
   npm start
   ```

## Utilisation

### Accès à l'application
- **Frontend** : http://localhost:3000
- **Backend API** : http://localhost:8000
- **Documentation API** : http://localhost:8000/docs
- **Base de données** : localhost:3306

### Comptes par défaut

Pour créer un compte administrateur initial :
```bash
# Via l'API (voir documentation Swagger)
# Ou directement en base de données
```

### Workflow des demandes

1. **Création** : Un employé crée une demande d'heures supplémentaires
2. **Soumission** : La demande passe au statut "soumise"
3. **Validation N1** : Premier niveau d'approbation
4. **Validation N2** : Second niveau d'approbation
5. **Acceptation/Rejet** : Décision finale

### Gestion des migrations

```bash
# Créer une nouvelle migration
alembic revision --autogenerate -m "Description de la migration"

# Appliquer les migrations
alembic upgrade head

# Revenir à une migration précédente
alembic downgrade -1
```

## Structure du projet

```
chronos-rh/
├── backend/
│   ├── app/
│   │   ├── models/          # Modèles SQLAlchemy
│   │   ├── schemas/         # Schémas Pydantic
│   │   ├── routers/         # Routes API
│   │   ├── services/        # Logique métier
│   │   └── utils/           # Utilitaires
│   ├── alembic/             # Migrations de base de données
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/      # Composants réutilisables
│   │   ├── pages/           # Pages de l'application
│   │   ├── hooks/           # Hooks personnalisés
│   │   └── services/        # Services API
│   ├── package.json
│   └── Dockerfile
├── ghs.sql                  # Schema de base de données
├── docker-compose.yml       # Configuration Docker
├── start.sh                 # Script de démarrage
└── README.md
```

## API Endpoints

### Authentification
- `POST /auth/login` - Connexion

### Employés
- `GET /employees` - Liste des employés
- `POST /employees` - Créer un employé
- `GET /employees/{id}` - Détails d'un employé
- `PUT /employees/{id}` - Modifier un employé
- `DELETE /employees/{id}` - Supprimer un employé

### Services
- `GET /services` - Liste des services
- `POST /services` - Créer un service
- `GET /services/{id}` - Détails d'un service
- `PUT /services/{id}` - Modifier un service
- `DELETE /services/{id}` - Supprimer un service

### Demandes
- `GET /requests` - Liste des demandes
- `POST /requests` - Créer une demande
- `GET /requests/my-requests` - Mes demandes
- `GET /requests/pending` - Demandes en attente
- `POST /requests/{id}/approve/{level}` - Approuver une demande
- `POST /requests/{id}/reject` - Rejeter une demande

### Santé de l'application
- `GET /health` - Vérification de l'état de l'API

## Développement

### Tests
```bash
# Backend
cd backend
python -m pytest

# Frontend
cd frontend
npm test
```

### Logs et monitoring
```bash
# Voir les logs de tous les services
docker-compose logs -f

# Logs d'un service spécifique
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f mysql
```

### Build de production
```bash
# Backend
docker build -t ghs-backend ./backend

# Frontend
cd frontend
npm run build
```

### Variables d'environnement importantes

#### Backend (.env)
- `DATABASE_URL` : URL de connexion à la base de données
- `SECRET_KEY` : Clé secrète pour JWT (à changer en production)
- `ACCESS_TOKEN_EXPIRE_MINUTES` : Durée de vie des tokens
- `BACKEND_CORS_ORIGINS` : Origines autorisées pour CORS

#### Frontend (.env)
- `REACT_APP_API_URL` : URL de l'API backend
- `REACT_APP_ENVIRONMENT` : Environnement (development/production)

## Sécurité

- 🔐 Authentification JWT avec expiration
- 🛡️ Validation des données avec Pydantic
- 🚫 Protection CORS configurée
- 🔒 Hachage sécurisé des mots de passe avec bcrypt
- 🏥 Health checks pour monitoring

## Performance

- ⚡ FastAPI avec performance native
- 🚀 Vite pour un build frontend optimisé
- 📦 Containerisation Docker pour déploiement
- 🗄️ Connexions de base de données optimisées
- 📊 Pagination sur les listes d'éléments

## Contribuer

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Dépannage

### Problèmes courants

1. **Erreur de connexion à la base de données**
   ```bash
   # Vérifier que MySQL est démarré
   docker-compose ps mysql
   
   # Vérifier les logs
   docker-compose logs mysql
   ```

2. **Port déjà utilisé**
   ```bash
   # Changer les ports dans docker-compose.yml
   # Ou arrêter les services qui utilisent les ports
   ```

3. **Problèmes de permissions**
   ```bash
   # Donner les permissions au script
   chmod +x start.sh
   ```

## Licence

Distribué sous licence MIT. Voir `LICENSE` pour plus d'informations.

## Support

Pour obtenir de l'aide :
1. Consultez la documentation API : http://localhost:8000/docs
2. Vérifiez les logs : `docker-compose logs -f`
3. Ouvrez une issue sur le repository

---

**ChronosRH** - Simplifiez la gestion de vos heures supplémentaires ! ⏰