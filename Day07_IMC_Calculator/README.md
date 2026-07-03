# Calculateur d'IMC

## Description

Ce projet est une application graphique simple développée en Python avec Tkinter. Elle permet à un utilisateur de saisir son poids et sa taille, de calculer automatiquement son indice de masse corporelle (IMC), puis d'afficher un résultat interprété selon les seuils couramment utilisés en santé publique.

## Objectif

L'objectif de cette application est de montrer comment créer une interface utilisateur simple avec Python, tout en mettant en pratique plusieurs notions fondamentales :

- saisie de données,
- validation des entrées,
- calculs mathématiques,
- affichage dynamique de résultats,
- gestion des erreurs utilisateur.

## Fonctionnalités

- Saisie du poids en kilogrammes
- Saisie de la taille en mètres
- Calcul automatique de l'IMC à partir des valeurs saisies
- Affichage du résultat numérique avec deux décimales
- Interprétation du résultat selon la catégorie correspondante
- Bouton permettant de réinitialiser les champs
- Messages d'erreur si les valeurs saisies sont invalides

## Prérequis

Pour exécuter ce projet, vous aurez besoin de :

- Python 3.8 ou une version supérieure
- Tkinter, généralement installé par défaut avec Python sur Windows, macOS et Linux

## Installation

1. Ouvrez votre terminal ou votre invite de commandes.
2. Accédez au dossier du projet :

```bash
cd Day07_IMC_Calculator
```

3. Lancez l'application avec la commande suivante :

```bash
python main.py
```

## Utilisation

Une fois l'application lancée :

1. Entrez votre poids en kilogrammes dans le champ prévu.
2. Entrez votre taille en mètres dans le champ correspondant.
3. Cliquez sur le bouton "Calculer l'IMC".
4. Le programme affiche votre IMC ainsi que sa catégorie interprétative.

## Interprétation de l'IMC

L'application classe l'IMC selon les valeurs suivantes :

- Inférieur à 18,5 : insuffisance pondérale
- Entre 18,5 et 24,9 : poids normal
- Entre 25 et 29,9 : surpoids
- Supérieur ou égal à 30 : obésité

Ces catégories sont fournies à titre indicatif et ne remplacent pas un avis médical.

## Structure du projet

- main.py : contient la logique du programme ainsi que l'interface graphique
- screenshots/ : dossier contenant les captures d'écran du projet

## Logique du programme

Le script principal réalise les étapes suivantes :

1. Crée la fenêtre principale avec Tkinter.
2. Affiche les champs de saisie pour le poids et la taille.
3. Récupère les valeurs entrées par l'utilisateur.
4. Vérifie que les données sont valides et positives.
5. Calcule l'IMC avec la formule :

$$
IMC = \frac{poids}{taille^2}
$$

6. Affiche le résultat et la catégorie correspondante.

## Gestion des erreurs

L'application affiche un message d'erreur si :

- le poids ou la taille n'est pas un nombre valide,
- une valeur négative ou nulle est saisie,
- les champs sont laissés vides.

## Améliorations possibles

Voici quelques idées pour enrichir ce projet :

- ajouter une validation plus détaillée des données saisies,
- améliorer l'interface graphique avec des couleurs et des polices plus modernes,
- enregistrer l'historique des calculs,
- intégrer une version avec base de données ou fichier JSON,
- ajouter des conseils personnalisés selon le résultat.

## Licence

Ce projet est fourni à titre éducatif et peut être utilisé librement dans un cadre d'apprentissage.
