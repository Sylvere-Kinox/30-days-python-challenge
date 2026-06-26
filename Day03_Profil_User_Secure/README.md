# Profil utilisateur sécurisé

Petit projet Python réalisé dans le cadre du challenge "30 Days Python".

## Description

Cette application permet de créer et de gérer un profil utilisateur depuis la console. Elle montre comment organiser un programme en POO, valider des données saisies et protéger certaines informations sensibles comme le mot de passe.

## Objectif

L'objectif de ce projet est de pratiquer la programmation orientée objet en Python tout en mettant en place des principes de base de sécurité :

- masquage du mot de passe à l'affichage
- validation de l'adresse email
- validation de la longueur du mot de passe
- gestion simple d'utilisateurs en mémoire

## Fonctionnalités

- Créer un utilisateur avec un nom, une adresse email et un mot de passe
- Valider l'email avant de l'enregistrer
- Vérifier que le mot de passe contient au moins 8 caractères
- Afficher les informations du profil sans révéler le mot de passe
- Mettre à jour l'email d'un utilisateur existant
- Afficher la liste des utilisateurs enregistrés

## Prérequis

- Python 3.8 ou version supérieure

## Exécution

1. Ouvrir un terminal dans le dossier du projet.
2. Exécuter la commande suivante :

```bash
python main.py
```

## Utilisation

Au lancement, le programme affiche un menu interactif avec plusieurs options :

1. Créer un utilisateur
2. Afficher tous les utilisateurs
3. Mettre à jour l'email d'un utilisateur
4. Quitter

Suivez les instructions affichées à l'écran pour utiliser l'application.

## Structure du dossier

- `main.py` : contient la logique du programme et l'interface en ligne de commande
- `screenshots/` : captures d'écran du projet
- `README.md` : documentation du projet

## Améliorations possibles

- Ajouter une sauvegarde des utilisateurs dans un fichier
- Crypter les mots de passe
- Ajouter une validation plus stricte des emails
- Introduire une interface graphique ou web

## Note

Ce projet est conçu comme un exercice pédagogique pour apprendre les bases de la programmation orientée objet et de la sécurité logicielle simple en Python.
