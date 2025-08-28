# CHRONOS - Gestion des Heures Supplémentaires

## Description

Système de gestion des heures supplémentaires développé avec FastAPI (backend) et React (frontend).

## Fonctionnalités

- 🔐 **Authentification** : Système de login sécurisé avec JWT
- 👥 **Gestion des employés** : CRUD complet des employés
- 🏢 **Gestion des services** : Organisation hiérarchique des départements
- ⏰ **Demandes d'heures supplémentaires** : Création et gestion des demandes
- ✅ **Workflow d'approbation** : Système de validation à plusieurs niveaux
- 🎯 **Tableau de bord** : Vue d'ensemble avec statistiques
- 📱 **Interface responsive** : Design adaptatif avec Tailwind CSS

## Architecture

### Backend (FastAPI)
- **Framework** : FastAPI avec Python 3.11+
- **Base de données** : MySQL avec SQLAlchemy ORM
- **Authentification** : JWT avec python-jose
- **Validation** : Pydantic schemas
- **Documentation** : Swagger UI automatique

### Frontend (React)
- **Framework** : React 18 avec hooks
- **Routing** : React Router DOM
- **State management** : React Query pour les données serveur
- **Styling** : Tailwind CSS
- **Forms** : React Hook Form
- **Notifications** : React Hot Toast

## Installation

### Prérequis
- Docker et Docker Compose
- Node.js 18+ (pour développement local)
- Python 3.11+ (pour développement local)

### Démarrage rapide avec Docker

1. **Cloner le projet**
   ```bash
   git clone <repo-url>
   cd ghs-project
   ```

2. **Configurer les variables d'environnement**
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```

3. **Démarrer avec Docker**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

### Installation manuelle

#### Backend

1. **Créer un environnement virtuel**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer la base de données**
   ```bash
   # Créer la base de données MySQL
   mysql -u root -p < ../ghs.sql
   ```

4. **Démarrer le serveur**
   ```bash
   uvicorn app.main:app --reload
   ```

#### Frontend

1. **Installer les dépendances**
   ```bash
   cd frontend
   npm install
   ```

2. **Démarrer le serveur de développement**
   ```bash
   npm start
   ```

## Utilisation

### Accès à l'application
- **Frontend** : http://localhost:3000
- **Backend API** : http://localhost:8000
- **Documentation API** : http://localhost:8000/docs

### Comptes par défaut
Vous devrez créer des comptes via l'API ou directement en base de données.

### Workflow des demandes

1. **Création** : Un employé crée une demande d'heures supplémentaires
2. **Soumission** : La demande passe au statut "soumise"
3. **Validation N1** : Premier niveau d'approbation
4. **Validation N2** : Second niveau d'approbation
5. **Acceptation/Rejet** : Décision finale

## Structure du projet

```
ghs-project/
├── backend/
│   ├── app/
│   │   ├── models/          # Modèles SQLAlchemy
│   │   ├── schemas/         # Schémas Pydantic
│   │   ├── routers/         # Routes API
│   │   ├── services/        # Logique métier
│   │   └── utils/           # Utilitaires
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

### Build de production
```bash
# Backend
docker build -t ghs-backend ./backend

# Frontend
cd frontend
npm run build
```

## Contribuer

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Licence

Distribué sous licence MIT. Voir `LICENSE` pour plus d'informations.
