# Courbe de Température

## Description

Application Python qui charge des données de température depuis un fichier CSV et trace l'évolution quotidienne avec la moyenne mobile sur 7 jours. Le programme met aussi en évidence les anomalies lorsque la température s'écarte de plus de deux écarts-types par rapport à la moyenne.

## Fonctionnalités

- Lecture d'un fichier CSV avec les colonnes `Date` et `Temperature`
- Calcul de la moyenne mobile sur 7 jours
- Détection d'anomalies de température
- Tracé des données avec `matplotlib`
- Affichage du graphique ou enregistrement au format PNG

## Prérequis

- Python 3.7 ou supérieur
- Bibliothèques `pandas` et `matplotlib`

## Installation

1. Placez-vous dans le dossier du projet :

```bash
cd "Day14_Courbe_De_Temperature"
```

2. Installez les dépendances :

```bash
pip install pandas matplotlib
```

## Utilisation

Exécutez le script principal :

```bash
python main.py
```

Suivez les instructions :

1. Entrez le chemin du fichier CSV contenant les données de température.
2. Choisissez si vous souhaitez enregistrer le graphique.
3. Si demandé, entrez le nom du fichier PNG.

## Format du fichier CSV

Le fichier CSV doit contenir au moins deux colonnes :

- `Date` : date au format ISO (`YYYY-MM-DD`)
- `Temperature` : valeur numérique de la température

Exemple :

```csv
Date,Temperature
2024-01-01,2.6
2024-01-02,20.38
2024-01-03,-6.64
```

## Structure du projet

```text
Day14_Courbe_De_Temperature/
├── main.py              # Script principal
├── README.md            # Documentation du projet
├── temperature_data.csv # Exemple de données
└── screenshots/         # Captures d'écran
```

## Remarques

- Le tracé affiche la température quotidienne et la moyenne mobile sur 7 jours.
- Les anomalies sont définies par des valeurs supérieures ou inférieures à deux écarts-types de la moyenne.
- Si vous enregistrez le graphique, indiquez un nom de fichier valide avec l'extension `.png`.

## Auteur

Défi 30 Jours Python - Jour 14
