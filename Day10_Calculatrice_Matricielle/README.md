# Calculatrice matricielle en Python

Ce projet implémente une application de calcul matriciel en environnement console, développée en Python avec la bibliothèque NumPy. Elle permet de saisir deux matrices, d'exécuter plusieurs opérations algébriques et de visualiser les résultats associés.

## Objectif scientifique

L'objectif de ce programme est de fournir un outil simple et pédagogique pour explorer les opérations fondamentales sur les matrices, notamment dans un cadre d'apprentissage de l'algèbre linéaire et du calcul numérique.

## Fonctionnalités principales

Le programme prend en charge les opérations suivantes :
- addition de matrices
- soustraction de matrices
- multiplication matricielle
- transposition de matrices
- calcul du déterminant
- calcul de l'inverse, lorsque la matrice est inversible

## Prérequis

Pour exécuter ce projet, il est nécessaire d'avoir :
- Python 3.8 ou une version ultérieure
- la bibliothèque NumPy installée

## Installation

Installez la dépendance requise avec la commande suivante :

```bash
pip install numpy
```

## Utilisation

Lancer le programme depuis le répertoire du projet :

```bash
python main.py
```

Le script guide l'utilisateur à travers les étapes suivantes :
1. saisie du nombre de lignes et de colonnes de la première matrice
2. saisie des éléments de la première matrice
3. saisie du nombre de lignes et de colonnes de la deuxième matrice
4. saisie des éléments de la deuxième matrice

Une fois les matrices renseignées, l'application affiche les résultats des opérations principales.

## Conditions mathématiques

Certaines opérations nécessitent des conditions spécifiques :
- l'addition et la soustraction exigent que les deux matrices aient les mêmes dimensions
- la multiplication matricielle exige la compatibilité dimensionnelle, c'est-à-dire que le nombre de colonnes de la première matrice corresponde au nombre de lignes de la deuxième
- l'inversion n'est possible que pour une matrice carrée et non singulière

## Structure du projet

- main.py : script principal contenant la logique du programme
- screenshots/ : dossier contenant les captures d'écran du projet

## Conclusion

Ce projet constitue une introduction pratique aux opérations matricielles en Python et illustre l'utilisation de NumPy pour le calcul scientifique de base.