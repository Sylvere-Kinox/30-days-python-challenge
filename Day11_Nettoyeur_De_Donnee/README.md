# Nettoyeur de Données

## Description

Application Python pour le nettoyage et le traitement de données issues de fichiers CSV. Ce programme permet de charger des données, les nettoyer en supprimant les valeurs manquantes et les doublons, remplir les données manquantes avec des moyennes statistiques, et renommer les colonnes pour une meilleure lisibilité.

## Fonctionnalités

- Chargement de fichiers CSV
- Suppression des valeurs manquantes
- Suppression des doublons
- Remplissage intelligent des valeurs manquantes avec la moyenne de chaque colonne
- Renommage des colonnes
- Sauvegarde des données nettoyées dans un nouveau fichier CSV
- Affichage d'un aperçu des données avant et après le nettoyage

## Prérequis

- Python 3.7 ou supérieur
- Bibliothèque pandas

## Installation

1. Clonez ou téléchargez le projet
2. Installez les dépendances requises :

```bash
pip install pandas
```

## Utilisation

Exécutez le programme avec la commande suivante :

```bash
python main.py
```

Le programme vous guidera à travers les étapes suivantes :

1. Entrez le chemin du fichier CSV à charger
2. Visualisez un aperçu des données
3. Le programme nettoie automatiquement les données en supprimant :
   - Les lignes avec des valeurs manquantes
   - Les lignes dupliquées
4. Remplit les valeurs manquantes avec la moyenne des colonnes numériques
5. Optionnel : Renommez les colonnes en les séparant par des virgules
6. Entrez le chemin du fichier de sortie pour sauvegarder les données nettoyées

## Exemple d'Exécution

```
=== Nettoyeur de Données ===
Bienvenue dans le programme de nettoyage de données...
Entrez le chemin du fichier CSV à charger: test_data.csv
Données chargées avec succès.
Aperçu des données chargées:
   ID    Nom  Age Salaire  Departement
0   1  Alice   30   50000           IT
1   2    Bob   25   45000           HR

=== Nettoyage des Données ===
Taille initiale du DataFrame: (15, 5)
Suppression des valeurs manquantes...
Taille du DataFrame après suppression des valeurs manquantes: (12, 5)
Suppression des doublons...
Taille du DataFrame après suppression des doublons: (10, 5)

=== Remplissage des Valeurs Manquantes ===
Taille initiale du DataFrame: (10, 5)
Taille du DataFrame après remplissage des valeurs manquantes: (10, 5)

=== Renommage des Colonnes ===
Noms de colonnes avant renommage: ['ID', 'Nom', 'Age', 'Salaire', 'Departement']
Entrez les nouveaux noms de colonnes séparés par des virgules: Employee_ID, Employee_Name, Employee_Age, Salary, Department
Noms de colonnes après renommage: ['Employee_ID', 'Employee_Name', 'Employee_Age', 'Salary', 'Department']

Entrez le chemin du fichier CSV pour sauvegarder les données nettoyées: cleaned_data.csv
Données sauvegardées avec succès dans 'cleaned_data.csv'.
```

## Structure du Projet

```
Day11_Nettoyeur_De_Donnee/
├── main.py              # Script principal
├── README.md            # Documentation
└── screenshots/         # Captures d'écran (optionnel)
```

## Fonctions Principales

### chargement_donne(chemin_fichier)
Charge les données à partir d'un fichier CSV et retourne un DataFrame pandas.

**Paramètres :**
- `chemin_fichier` (str) : Chemin vers le fichier CSV

**Retour :**
- DataFrame pandas ou None en cas d'erreur

### nettoyage_donnees(df)
Supprime les valeurs manquantes et les doublons du DataFrame.

**Paramètres :**
- `df` (DataFrame) : DataFrame à nettoyer

**Retour :**
- DataFrame nettoyé

### remplissage_valeurs_manquantes(df)
Remplit les valeurs manquantes avec la moyenne de chaque colonne.

**Paramètres :**
- `df` (DataFrame) : DataFrame à traiter

**Retour :**
- DataFrame avec valeurs manquantes remplies

### renommage_colonnes(df, nouveaux_noms)
Renomme les colonnes du DataFrame.

**Paramètres :**
- `df` (DataFrame) : DataFrame à renommer
- `nouveaux_noms` (list) : Liste des nouveaux noms de colonnes

**Retour :**
- DataFrame avec colonnes renommées

### sauvegarde_donnees(df, chemin_fichier)
Sauvegarde le DataFrame nettoyé dans un fichier CSV.

**Paramètres :**
- `df` (DataFrame) : DataFrame à sauvegarder
- `chemin_fichier` (str) : Chemin du fichier de sortie

## Considérations Importantes

- Le programme supprime d'abord les lignes avec des valeurs manquantes avant de les remplir à la moyenne. Assurez-vous que ce comportement correspond à vos besoins.
- Le renommage des colonnes est optionnel et peut être ignoré en appuyant sur Entrée.
- Les données sauvegardées ne contiennent pas l'index du DataFrame.

## Auteur

Défi 30 Jours Python - Jour 11

## Licence

Consultez le fichier LICENSE pour plus d'informations.
