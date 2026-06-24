# Simulateur de compte bancaire

Ce projet propose un simulateur de compte bancaire développé en Python. Il offre une interface en ligne de commande permettant de gérer des comptes clients, d'effectuer des opérations courantes et de suivre l'historique des transactions.

## Objectif

L'objectif de cette application est de fournir un prototype simple et fonctionnel de gestion de comptes bancaires, adapté à l'apprentissage des structures de données, des classes et des interactions utilisateur en Python.

## Fonctionnalités

- Création d'un compte client avec attribution automatique d'un numéro de compte
- Enregistrement d'un solde initial
- Dépôt d'argent sur un compte existant
- Retrait d'argent avec vérification de la disponibilité du solde
- Consultation du solde d'un compte
- Affichage de l'historique des transactions
- Gestion des erreurs de saisie et des cas de solde insuffisant

## Fichier principal

- `main.py` : implémente la logique métier et l'interface utilisateur du simulateur.

## Prérequis

- Python 3.8 ou version supérieure

## Exécution

1. Ouvrir un terminal depuis le répertoire du projet.
2. Exécuter la commande suivante :

```bash
python main.py
```

## Utilisation

Une fois le programme lancé, sélectionner l'une des options proposées :

1. Créer un compte
2. Déposer de l'argent
3. Retirer de l'argent
4. Consulter le solde
5. Consulter l'historique
6. Quitter

### Exemple d'utilisation

- Créer un compte en renseignant le nom du titulaire et le solde initial.
- Noter le numéro de compte attribué.
- Pour effectuer une opération, saisir le numéro de compte puis le montant.
- Consulter le solde ou l'historique pour suivre l'évolution du compte.

## Comportement applicatif

- Les montants invalides ou négatifs sont rejetés avec un message explicite.
- Les dépôts augmentent le solde et ajoutent une entrée dans l'historique.
- Les retraits sont autorisés uniquement si le solde est suffisant.
- L'historique des transactions inclut la date et l'heure de chaque opération.

## Limitations

- Les données sont conservées uniquement en mémoire : elles sont perdues à la fermeture du programme.
- L'application ne gère pas la persistance des comptes sur disque.
- La validation des numéros de compte est limitée à la vérification de leur existence.

## Améliorations possibles

- Ajouter une persistance des données (fichier JSON, CSV ou base de données).
- Renforcer la validation des entrées utilisateur.
- Proposer une interface graphique ou une application web.
- Implémenter des fonctionnalités supplémentaires : taux d'intérêt, virements, gestion multi-devises.
- Ajouter des tests unitaires pour couvrir la logique métier.

## Notes

Le simulateur est conçu comme un outil pédagogique pour comprendre les principes de la programmation orientée objet et la gestion d'état dans une application Python.
