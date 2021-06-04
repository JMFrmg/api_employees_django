# Projet réalisé dans le cadre de la formation Microsoft Simplon IA

## API de gestion d'employés au sein d'une entreprise

L'application a été mise en ligne sur Heroku :
https://frozen-tor-79057.herokuapp.com/

### Préparer l'environnement
En console se placer à la racine du projet
```bash
python -m venv mon_env
```

Installation des packages requis :
```bash
pip install -r requirements.txt
```

### Créer la structure de la BDD
L'application utilise une base de données sqlite3 en local
Génération des fichiers de migration :
```bash
python manage.py makemigrations
```
Création de la structure de la BDD :
```bash
python manage.py migrate
```

### Créer un super utilisateur
```bash
python manage.py createsuperuser
```
Renseigner les informations demandées

### Lancement du serveur local
```bash
python manage.py runserver
```
