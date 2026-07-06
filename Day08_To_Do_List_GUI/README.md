# Day 08 — To‑Do List (Interface graphique)

Résumé
-------
Application desktop légère développée en Python avec `tkinter` pour la gestion élémentaire de tâches (To‑Do). Ce document présente la conception, les choix techniques, les métriques d'évaluation et les extensions possibles pour un usage reproductible et scientifique.

Objectif et portée
------------------
Fournir un prototype démontrant les principes suivants : saisie structurée d'une tâche, affichage et modification d'un état local, suppression contrôlée, et possibilités de persistance minimale. Ce projet n'est pas destiné à la production, mais sert de base pour expérimenter des stratégies de stockage, des métriques d'usage et des interfaces utilisateur simples.

Conception logicielle
---------------------
- Langage : Python 3.8+
- Bibliothèque graphique : `tkinter` (standard)
- Modèle de données : entrée minimale par tâche (texte, timestamp facultatif)
- Architecture : interface graphique mono‑processus, logique UI dans `main.py`.

Modèle de données (exemple)
---------------------------
Représentation interne d'une tâche :

- id : int (identifiant séquentiel)
- title : string (texte de la tâche)
- created_at : ISO 8601 timestamp (optionnel)
- completed : bool (optionnel pour extensions)

Fonctionnalités implémentées
----------------------------
- Création d'une tâche via un champ de saisie
- Affichage séquentiel des tâches
- Suppression d'une tâche sélectionnée
- Réinitialisation des champs de saisie

Prérequis
---------
- Python 3.8 ou supérieur
- `tkinter` (installé par défaut sur la plupart des environnements desktop). Sous Debian/Ubuntu : `sudo apt install python3-tk` si nécessaire.

Exécution
---------
Se placer dans le répertoire du projet puis lancer :

```bash
cd 30-days-python-challenge/Day08_To_Do_List_GUI
python main.py
```

Interface et interactions
------------------------
- Champ texte pour la saisie d'une nouvelle tâche
- Liste affichée (Listbox) pour la sélection
- Bouton "Ajouter" / "Supprimer" / "Réinitialiser"

Considérations scientifiques
---------------------------
- Reproductibilité : enregistrer les entrées/sorties (CSV/JSON) permet d'auditer et d'analyser l'utilisation de l'interface.
- Cohérence des données : les tâches doivent porter un identifiant stable si l'on conserve l'historique.
- Mesures et métriques recommandées :
	- latence d'ajout (ms),
	- nombre d'opérations par session,
	- taux d'effacement (supprimer vs ajouter),
	- longueur moyenne des tâches (caractères).
- Tests : isoler la logique métier (extraction d'une fonction pure pour l'ajout/suppression) facilite l'écriture de tests unitaires.

Persistance et formats recommandés
----------------------------------
- JSON : pratique pour sérialiser la liste des tâches (lecture/écriture simple)
- CSV : adéquat pour l'analyse statistique avec tableurs ou scripts
- SQLite : si besoin d'un index et requêtes plus riches pour l'historique

Extension technique proposée (exemple JSON)
-----------------------------------------
Fichier `tasks.json` :

```json
[
	{"id": 1, "title": "Acheter du pain", "created_at": "2026-07-06T12:00:00Z", "completed": false}
]
```

Qualité du code et bonnes pratiques
----------------------------------
- Séparer la logique UI de la logique métier pour testabilité.
- Ajouter des tests unitaires pour : parsing des entrées, ajout/suppression, sérialisation.
- Gérer les erreurs d'E/S lors de la persistance.

Sécurité et confidentialité
--------------------------
L'application manipule uniquement du texte libre localement. Si vous ajoutez de la persistance, évitez d'y stocker des informations sensibles et documentez le format de stockage.

Évaluation et validation
-----------------------
- Écrire des tests automatisés pour garantir le comportement attendu.
- Collecter des métriques d'utilisation si vous expérimentez l'ergonomie (consentement requis pour données utilisateur).

Fichiers principaux
-------------------
- `main.py` : interface graphique et logique d'interaction
- `README.md` : ce document
- `screenshots/` : captures d'écran (optionnel)

Améliorations possibles
----------------------
- Édition d'une tâche existante (double‑clic pour éditer)
- Marquage de complétion et filtrage (actives/complétées)
- Sauvegarde automatique et chargement au démarrage
- Tests unitaires et CI (GitHub Actions)
- API REST minimale pour synchronisation multi‑client

Références et ressources
-----------------------
- Documentation Python `tkinter` — module standard pour UI simples
- Guides sur la conception de systèmes réplicables et la persistance JSON/SQLite

Licence et contribution
----------------------
Voir le fichier `LICENSE` à la racine du dépôt. Contributions : ouvrir une issue puis une pull request.

Contact
-------
Voir le README principal du dépôt pour les informations de contact.
