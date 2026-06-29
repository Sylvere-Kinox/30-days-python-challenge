# Distributeur Automatique de Billets (ATM)

## Description

Application d'un distributeur automatique de billets développée en Python. Ce projet simule un système bancaire simplifié avec gestion de comptes, authentification par PIN et opérations bancaires courantes.

**Niveau:** Intermédiaire  
**Durée:** Jour 4 du défi 30 jours Python

## Fonctionnalités

### Gestion des Comptes
- Création de nouveau compte bancaire
- Authentification sécurisée par PIN (4 chiffres)
- Gestion des soldes des comptes

### Opérations Bancaires
- **Vérification du solde** - Consultation du solde courant
- **Dépôt** - Ajout d'argent au compte
- **Retrait** - Retrait d'argent avec vérification du solde
- **Modification du PIN** - Changement du code PIN (4 chiffres)

### Sécurité
- Encapsulation des données sensibles (PIN et solde privés)
- Validation des montants (doivent être positifs)
- Vérification de la suffisance des fonds avant retrait
- PIN robuste (4 chiffres obligatoires)

## Installation

### Prérequis
- Python 3.6 ou supérieur

### Étapes
1. Clonez ou téléchargez le projet
2. Naviguez vers le dossier Day04 :

```bash
cd Day04_Distributeur_de_Billets_Automatiques
```

3. Exécutez le programme :

```bash
python main.py
```

## Utilisation

### Menu Principal
Au lancement, vous accédez à ce menu :

```
=== Menu Principal ===
1. Créer un compte
2. Se connecter à un compte
3. Quitter
```

### Créer un Compte
1. Sélectionnez l'option 1
2. Entrez un numéro de compte (ex: ACC001)
3. Créez un PIN à 4 chiffres
4. Confirmez la création

### Se Connecter
1. Sélectionnez l'option 2
2. Entrez votre numéro de compte
3. Entrez votre PIN
4. Accédez au menu de gestion de compte

### Menu de Compte
```
=== Menu du Compte ===
1. Vérifier le solde
2. Déposer de l'argent
3. Retirer de l'argent
4. Changer le code pin
5. Déconnexion
```

### Exemple de Session
```
=== Menu Principal ===
1. Créer un compte
2. Se connecter à un compte
3. Quitter

Choisissez une option : 1
Entrez un numero de compte : ACC001
Créer un code pin à 4 chiffres : 1234
Compte créer avec succes.

=== Menu Principal ===
1. Créer un compte
2. Se connecter à un compte
3. Quitter

Choisissez une option : 2
Entrez un numero de compte : ACC001
Entrez votre code pin : 1234
Authentification réussie.

=== Menu du Compte ===
1. Vérifier le solde
...
```

## Architecture du Code

### Classe Compte_bancaire
Représente un compte bancaire individuel.

**Attributs privés :**
- `__pin` : Code d'accès (4 chiffres)
- `__solde` : Solde du compte

**Méthodes :**
- `validation_pin(pin_entrer)` - Vérifie le PIN
- `verifiation_solde()` - Affiche le solde
- `depot(montant2depot)` - Ajoute un montant au solde
- `retrait(montant2retrait)` - Retire un montant du solde
- `modif_pin(old_pin, new_pin)` - Change le PIN

### Classe ATM
Gère l'interface et les interactions avec l'utilisateur.

**Attributs :**
- `compte` : Dictionnaire des comptes (clé : numéro de compte)

**Méthodes :**
- `creer_compte()` - Crée un nouveau compte
- `authent_coompte()` - Authentifie un utilisateur
- `menu_compte(compte)` - Affiche le menu de gestion de compte
- `main_menu()` - Menu principal du distributeur

## Concepts Python Utilisés

### Programmation Orientée Objet (POO)
- Classes et constructeurs
- Encapsulation (attributs privés avec `__`)
- Méthodes

### Structures de Données
- Dictionnaires pour stocker les comptes

### Contrôle de Flux
- Boucles while
- Instructions if/elif/else

### Gestion des Exceptions
- Try/except pour la saisie de nombres

### Validation des Données
- Vérification des PIN
- Validation des montants

## Améliorations Possibles

- Ajouter un historique des transactions
- Implémenter une persistance de données (fichier JSON/Base de données)
- Ajouter un taux d'intérêt pour les dépôts
- Implémenter des frais de retrait
- Ajouter un système de tentatives de connexion limitées
- Améliorer l'interface utilisateur
- Ajouter des logs d'audit pour chaque transaction
- Implémenter un système de cartes multiples par compte

## Notes sur le Code

### Points Forts
- Encapsulation correcte des données sensibles
- Validation des montants positifs
- Vérification de la suffisance des fonds
- Interface utilisateur intuitive
- Gestion des erreurs de saisie

### Points d'Attention
- Les données sont perdues à la fermeture du programme
- Pas de historique des transactions
- PIN stocké en mémoire non chiffré
- Pas de limite de tentatives de connexion  

## Ressources Utiles

- Documentation Python - Classes
- Encapsulation en Python
- Gestion des exceptions

## Auteur

Défi 30 Jours - Python Challenge

## Licence

Voir le fichier LICENSE à la racine du projet

## Objectifs d'Apprentissage

À la fin de ce projet, vous devriez comprendre :
- Comment créer et utiliser les classes
- L'importance de l'encapsulation
- Comment gérer l'authentification basique
- La validation des données utilisateur
- La création d'interfaces utilisateur interactives
