# Générateur de Graphiques

## Description

Application Python permettant de créer différents types de graphiques à partir de données saisies manuellement ou importées depuis un fichier CSV. Ce programme offre une interface simple en ligne de commande pour générer, visualiser et enregistrer des graphiques.

## Fonctionnalités

- Génération de graphiques en ligne
- Génération de graphiques en barres
- Génération de graphiques en nuage de points
- Génération d’histogrammes
- Génération de diagrammes circulaires
- Saisie manuelle des données
- Importation de données depuis un fichier CSV
- Définition d’un titre personnalisé pour le graphique
- Enregistrement du graphique au format PNG

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

Le programme vous guidera à travers les étapes suivantes :

1. Choisissez le type de graphique à générer
2. Choisissez la méthode d’entrée des données :
   - saisie manuelle
   - importation depuis un fichier CSV
3. Saisissez les valeurs ou indiquez le chemin du fichier CSV
4. Entrez le titre du graphique
5. Choisissez si vous souhaitez enregistrer le graphique

## Exemple d’Exécution

```text
Bienvenue dans le Générateur de graphique
Veuillez entrer le type de graphique que vous souhaitez générer (ex: 'line', 'bar', 'scatter'):
1-Graphe en ligne (line)
2-Graphe en barres (bar)
3-Graphe en nuage de points (scatter)
4-Histogramme (hist)
5-Diagramme circulaire (pie)
```

## Structure du Projet

```text
Day12_Generateur_Graphique/
├── main.py              # Script principal
├── README.md            # Documentation
├── test_data.csv        # Fichier CSV d'exemple
└── screenshots/         # Captures d'écran (optionnel)
```

## Fonctions Principales

### plot_graph()
Lance l’application et gère l’ensemble du processus de génération du graphique.

**Fonctionnement :**
- Affiche le menu de sélection du graphique
- Gère la saisie manuelle ou l’importation CSV
- Génère et affiche le graphique
- Propose l’enregistrement du graphique

### resolve_csv_path(chemin_fichier)
Résout le chemin d’un fichier CSV, que ce soit un chemin absolu ou relatif.

**Paramètres :**
- `chemin_fichier` (str) : Chemin du fichier CSV

**Retour :**
- Chemin valide du fichier CSV ou le chemin saisi si aucune correspondance n’est trouvée

## Format du Fichier CSV

Le fichier CSV doit contenir au moins deux colonnes de données. La première colonne sera utilisée pour l’axe X et la seconde pour l’axe Y.

Exemple :

```csv
x,y
1,5
2,8
3,6
4,10
```

## Considérations Importantes

- Vérifiez que les données saisies ont la même taille pour les axes X et Y.
- Le programme nécessite des valeurs numériques pour générer les graphiques.
- Si vous choisissez d’enregistrer le graphique, indiquez un nom de fichier avec l’extension .png.

## Auteur

Défi 30 Jours Python - Jour 12

## Licence

Consultez le fichier LICENSE pour plus d’informations.
