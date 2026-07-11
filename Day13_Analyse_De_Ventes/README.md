# Analyse de Ventes

## Description

Application Python permettant de charger, nettoyer, analyser et visualiser des données de ventes à partir d’un fichier CSV. Ce projet offre une solution simple et pratique pour explorer des données commerciales, obtenir des statistiques utiles et générer des graphiques de synthèse.

## Fonctionnalités

- Chargement des données depuis un fichier CSV
- Nettoyage des données avec gestion des valeurs manquantes
- Conversion automatique des colonnes de dates et de montants
- Calcul de statistiques de base sur les ventes
- Analyse des ventes par catégorie de produit
- Analyse des ventes mensuelles
- Identification des 5 produits les plus vendus
- Visualisation des données avec des graphiques

## Prérequis

- Python 3.8 ou supérieur
- Bibliothèques : pandas et matplotlib

## Installation

1. Clonez ou téléchargez le projet.
2. Installez les dépendances nécessaires avec la commande suivante :

```bash
pip install pandas matplotlib
```

## Utilisation

Exécutez le programme avec la commande suivante :

```bash
python main.py
```

Lors de l’exécution, vous serez invité à saisir le chemin du fichier CSV contenant les données de ventes.

## Exemple d’Exécution

```text
Entrez le chemin du fichier CSV contenant les données de ventes : sales_data.csv
```

Le programme affichera ensuite :

- les statistiques de base,
- les ventes totales par catégorie,
- les ventes mensuelles,
- le top 5 des produits les plus vendus,
- ainsi que des graphiques de visualisation.

## Structure du Projet

```text
Day13_Analyse_De_Ventes/
├── main.py              # Script principal
├── README.md            # Documentation du projet
├── sales_data.csv       # Fichier CSV d’exemple
└── screenshorts/        # Captures d’écran du projet
```

## Fonctions Principales

### chargement_donnees(chemin_fichier)
Charge les données de ventes à partir d’un fichier CSV.

### nettoyage_donnees(df)
Nettoie les données en supprimant les valeurs manquantes, en convertissant les colonnes de date et de montant, puis en ajoutant des colonnes utiles pour l’analyse.

### analyse_donnees(df)
Génère des statistiques de base ainsi que des analyses par catégorie et par mois.

### top_produits(df)
Identifie les 5 produits les plus vendus selon la quantité.

### visualisation_donnees(df)
Affiche des graphiques pour visualiser les tendances de ventes.

## Format du Fichier CSV

Le fichier CSV doit contenir des colonnes telles que :

- Product_Name
- Product_Category
- Quantity
- Price
- Sales_Amount
- Date

Exemple :

```csv
Order ID,Product_Name,Product_Category,Quantity,Price,Sales_Amount,Date
10001,Shirt,Clothing,2,25.99,51.98,2023-01-01
```

## Notes Importantes

- Assurez-vous que le fichier CSV est bien formaté.
- Les colonnes de date et de montant doivent contenir des valeurs valides.
- Le programme fonctionne mieux avec un fichier contenant des données cohérentes et complètes.

## Auteur

Défi 30 Jours Python - Jour 13

## Licence

Consultez le fichier LICENSE pour plus d’informations.
