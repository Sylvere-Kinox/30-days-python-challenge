# Application de Suivi de Dépenses

## Description

Application Python permettant d'enregistrer, de consulter et d'analyser des dépenses personnelles. Le programme utilise un fichier CSV pour conserver les données et propose une interface simple en ligne de commande pour ajouter des dépenses, afficher un résumé par catégorie et visualiser les tendances des dépenses.

## Fonctionnalités

- Ajout d'une nouvelle dépense
- Validation de la date au format `YYYY-MM-DD`
- Enregistrement des dépenses dans un fichier CSV
- Résumé des dépenses par catégorie
- Génération d'un graphique circulaire des dépenses par catégorie
- Affichage des tendances mensuelles sous forme de graphique en barres
- Rechargement automatique des données après l'ajout d'une dépense

## Prérequis

- Python 3.7 ou supérieur
- Bibliothèques pandas et matplotlib

## Installation

1. Clonez ou téléchargez le projet
2. Installez les dépendances requises :

```bash
pip install pandas matplotlib
```

## Utilisation

Exécutez le programme avec la commande suivante :

```bash
python main.py
```

Le programme vous guidera à travers les options suivantes :

1. Ajouter une dépense
2. Résumer les dépenses par catégorie
3. Afficher un graphique des dépenses par catégorie
4. Afficher les tendances mensuelles des dépenses
5. Quitter l'application

Lors de l'ajout d'une dépense, saisissez la date, la catégorie, le montant et une description.

## Exemple d'Exécution

```text
Menu :
1. Ajouter une dépense
2. Résumer les dépenses par catégorie
3. Afficher un graphique des dépenses par catégorie
4. Afficher les tendances mensuelles des dépenses
5. Quitter

Entrez le numéro correspondant à votre choix : 1
Entrez la date (YYYY-MM-DD) : 2026-03-01
Entrez la catégorie : Alimentation
Entrez le montant : 25000
Entrez la description : Courses
```

## Structure du Projet

```text
Day16_App_Suivi_Depense/
├── main.py              # Script principal
├── README.md            # Documentation
├── expenses.csv         # Données des dépenses
└── screenshort/         # Captures d'écran (optionnel)
```

## Fonctions Principales

### log_expense(date, category, amount, description)
Enregistre une dépense dans le fichier `expenses.csv`.

**Paramètres :**
- `date` (str) : Date de la dépense au format `YYYY-MM-DD`
- `category` (str) : Catégorie de la dépense
- `amount` (float) : Montant de la dépense
- `description` (str) : Description de la dépense

### load_expenses()
Charge les dépenses enregistrées dans un DataFrame pandas.

**Retour :**
- DataFrame contenant les colonnes `Date`, `Categorie`, `Compte` et `Description`

### summarize_expenses(df)
Calcule et affiche le total des dépenses pour chaque catégorie.

### plot_expenses_by_category(df)
Génère un graphique circulaire représentant la répartition des dépenses par catégorie.

### plot_monthly_trends(df)
Convertit les dates et génère un graphique en barres présentant l'évolution mensuelle des dépenses.

### main()
Lance l'application et gère le menu principal ainsi que les interactions avec l'utilisateur.

## Format du Fichier CSV

Le fichier CSV doit contenir quatre colonnes dans l'ordre suivant :

```csv
Date,Categorie,Compte,Description
2026-03-01,Alimentation,25000,Courses
2026-03-02,Transport,5000,Titre de transport
```

- `Date` : date de la dépense
- `Categorie` : catégorie de la dépense
- `Compte` : montant de la dépense
- `Description` : détail de la dépense

## Considérations Importantes

- Les dates doivent respecter le format `YYYY-MM-DD`.
- Le fichier `expenses.csv` doit être présent dans le même dossier que `main.py`.
- Les montants doivent être saisis sous forme numérique.
- Les graphiques s'affichent dans une fenêtre Matplotlib.
- Une nouvelle dépense est ajoutée à la fin du fichier CSV sans supprimer les données existantes.

## Auteur

Défi 30 Jours Python - Jour 16

## Licence

Consultez le fichier LICENSE pour plus d'informations.
