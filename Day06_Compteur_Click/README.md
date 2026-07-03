# Compteur de Clicks - Application GUI

## Description

Application de comptage interactive développée en Python avec Tkinter. Cette application permet de gérer un compteur avec des retours visuels dynamiques et un système d'objectifs.

## Fonctionnalités

- Incrémenter le compteur
- Décrémenter le compteur (avec minimum à zéro)
- Réinitialiser le compteur
- Retours visuels dynamiques (changement de couleur selon la valeur)
- Système de notification lorsque l'objectif est atteint
- Interface utilisateur intuitive et responsive

## Technologies

- Python 3.x
- Tkinter (framework GUI)
- messagebox (pour les notifications)

## Prérequis

Tkinter est inclus avec la plupart des installations Python. En cas d'absence sur Linux :

```bash
sudo apt-get install python3-tk
```

## Installation et utilisation

1. Cloner ou télécharger le projet
2. Naviguer vers le répertoire Day06_Compteur_Click
3. Exécuter l'application :

```bash
python main.py
```

## Architecture et structure du code

Le code est organisé selon une structure standard d'application Tkinter :

- **Imports** : Déclaration des dépendances (tkinter, messagebox)
- **Configuration** : Initialisation de la fenêtre principale
- **Variables globales** : Déclaration du compteur et de l'objectif
- **Fonctions** : Tous les handlers d'événements et les mises à jour
- **Widgets** : Création et placement des éléments GUI
- **Lancement** : Démarrage de la boucle d'événements

## Concepts de programmation couverts

- Programmation orientée événements avec Tkinter
- Gestion d'état avec variables globales
- Callbacks et binding d'événements
- Mise à jour dynamique des widgets
- Boîtes de dialogue modales
- Gestion des styles (couleurs, polices)

## Captures d'écran

Des captures d'écran de l'application sont disponibles dans le dossier `screenshots/`.

## Améliorations futures envisagées

- Persistance des données (sauvegarde du compteur)
- Configuration flexible de l'objectif
- Historique des modifications
- Thème personnalisable
- Effectes sonores
- Statistiques d'utilisation
 