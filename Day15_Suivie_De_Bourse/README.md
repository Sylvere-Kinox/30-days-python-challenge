# Suivi de la Météo

## Description

Application Python permettant de récupérer et analyser les données météorologiques en temps réel pour différentes villes. Le programme utilise l'API OpenWeatherMap pour obtenir les informations actuelles sur la température, l'humidité, la vitesse du vent et la description météorologique. Il propose également la génération de graphiques pour visualiser et comparer les températures entre plusieurs villes.

## Fonctionnalités

- Récupération des données météorologiques en temps réel pour une ville spécifiée
- Affichage des informations météorologiques complètes (température, humidité, vitesse du vent)
- Génération de graphiques en barres pour afficher la température d'une ville
- Comparaison des températures entre plusieurs villes avec visualisation graphique
- Interface interactive par menu en ligne de commande
- Gestion des erreurs de connexion à l'API

## Prérequis

- Python 3.7 ou supérieur
- Bibliothèques requests et matplotlib
- Clé API OpenWeatherMap (gratuite)

## Installation

1. Clonez ou téléchargez le projet
2. Installez les dépendances requises :

```bash
pip install requests matplotlib
```

3. Obtenez une clé API gratuite sur https://openweathermap.org/api
4. Remplacez la valeur de `API_KEY` dans le fichier main.py par votre clé personnelle

## Utilisation

Exécutez le programme avec la commande suivante :

```bash
python main.py
```

Le programme affichera un menu interactif vous permettant de :

1. Récupérer les données météo pour une ville
2. Afficher un graphique de la température pour une ville
3. Comparer les températures de plusieurs villes
4. Quitter l'application

## Exemple d'Exécution

```text
Bienvenue dans le programme de suivi de la météo !

Menu :
1. Récupérer les données météo pour une ville
2. Afficher un graphique de la température pour une ville
3. Comparer les températures de plusieurs villes
4. Quitter

Entrez le numéro correspondant à votre choix : 1
Entrez le nom de la ville : Paris
Ville : Paris
Température : 22 °C
Humidité : 65 %
Description : Partly cloudy
Vitesse du vent : 4.5 m/s
```

## Structure du Projet

```text
Day15_Suivie_De_Bourse/
├── main.py              # Script principal
├── README.md            # Documentation
└── screenshots/         # Captures d'écran (optionnel)
```

## Fonctions Principales

### recupere_donnees_meteo(ville)
Récupère les données météorologiques pour une ville donnée via l'API OpenWeatherMap.

**Paramètres :**
- `ville` (str) : Nom de la ville

**Retour :**
- Dictionnaire contenant les données météorologiques si la requête réussit
- None en cas d'erreur

### affiche_donnees_meteo(donnees)
Affiche les informations météorologiques extraites des données API.

**Paramètres :**
- `donnees` (dict) : Dictionnaire des données météorologiques

**Affichage :**
- Nom de la ville
- Température en degrés Celsius
- Humidité en pourcentage
- Description de la condition météorologique
- Vitesse du vent en m/s

### trace_graphique_temperature(ville)
Génère et affiche un graphique en barres de la température pour une ville.

**Paramètres :**
- `ville` (str) : Nom de la ville

**Fonctionnement :**
- Récupère les données météorologiques
- Crée un graphique en barres
- Affiche le graphique avec titre et labels

### comparer_temperatures(villes)
Compare et visualise les températures de plusieurs villes sous forme de graphique.

**Paramètres :**
- `villes` (list) : Liste des noms des villes à comparer

**Fonctionnement :**
- Récupère les données pour chaque ville
- Trace les points sur un graphique
- Affiche un graphique avec légende

### main()
Lance l'application et gère le menu interactif.

**Fonctionnement :**
- Affiche le menu principal
- Traite les choix de l'utilisateur
- Exécute les fonctions correspondantes
- Boucle jusqu'à la sélection de la sortie

## Notes Importantes

- La clé API fournie dans le code est publique et limitée en nombre de requêtes
- Pour une utilisation en production, utilisez votre propre clé API
- Certaines villes peuvent ne pas être trouvées si le nom n'est pas exact
- Les données affichées correspondent à la situation météorologique actuelle au moment de l'appel

## Limitations

- L'API OpenWeatherMap gratuite est limitée à 60 requêtes par minute
- Les données sont en temps réel et ne conservent pas d'historique
- La version gratuite ne fournit pas de prévisions météorologiques avancées
