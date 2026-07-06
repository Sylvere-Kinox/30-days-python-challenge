# Calculateur d'IMC — Version scientifique

Résumé
-------
Outil pédagogique et d'illustration développé en Python (bibliothèque `tkinter`) pour calculer l'indice de masse corporelle (IMC) à partir du poids et de la taille d'un individu. Le présent document décrit la méthode de calcul, les conventions d'interprétation utilisées, les limites biométriques de l'IMC et les instructions d'exécution.

Contexte scientifique
---------------------
L'indice de masse corporelle (IMC, ou BMI en anglais) est un indicateur anthropométrique couramment utilisé pour estimer la corpulence d'un individu :

$$
\\mathrm{IMC} = \\frac{\\mathrm{poids\\ (kg)}}{\\left(\\mathrm{taille\\ (m)}\\right)^2}
$$

Cet indicateur est utilisé à l'échelle populationnelle pour surveiller la prévalence du surpoids et de l'obésité. Il ne constitue pas un diagnostic clinique : il ne distingue pas la masse grasse de la masse maigre, ni la distribution de la masse corporelle.

Interprétation et seuils
-----------------------
Les catégories d'interprétation présentées dans l'application suivent les seuils courants recommandés par les organismes de santé publique :

- IMC < 18,5 : insuffisance pondérale
- 18,5 ≤ IMC < 25,0 : corpulence normale
- 25,0 ≤ IMC < 30,0 : surpoids
- IMC ≥ 30,0 : obésité

Remarques méthodologiques
------------------------
- Un résultat chiffré est arrondi à deux décimales pour l'affichage.
- L'IMC n'est pas adapté pour certaines populations (athlètes très musclés, personnes âgées avec sarcopénie, femmes enceintes, enfants et adolescents — pour ces derniers, utiliser les courbes et percentiles spécifiques à l'âge et au sexe).
- Pour une évaluation corporelle plus précise, combiner l'IMC avec d'autres mesures : tour de taille, rapport taille/hanches, pourcentage de masse grasse (DEXA, impédancemétrie), etc.

Prérequis techniques
--------------------
- Python 3.8 ou supérieur
- `tkinter` (fourni par défaut sous Windows/macOS ; sous certaines distributions Linux, installer `python3-tk`)

Exécution
---------
1. Ouvrir un terminal et se placer dans le répertoire du projet :

```bash
cd 30-days-python-challenge/Day07_IMC_Calculator
```

2. Lancer l'application :

```bash
python main.py
```

Utilisation
-----------
- Saisir le poids en kilogrammes (kg) et la taille en mètres (m).
- Cliquer sur « Calculer l'IMC ».
- L'interface affiche l'IMC calculé (2 décimales) et la catégorie correspondante.

Structure du dépôt
------------------
- `main.py` : implémentation de l'interface et de la logique de calcul
- `README.md` : ce document
- `screenshots/` : captures d'écran (facultatif)

Conception et validation
------------------------
Le code réalise des contrôles de validité élémentaires : conversion numérique, valeurs strictement positives et gestion d'erreurs d'entrée. Pour des usages scientifiques, on recommandera :

- de quantifier l'incertitude des mesures (précision des pèses-personnes et mesures de taille),
- d'ajouter des tests unitaires pour les fonctions de calcul et de validation,
- d'enregistrer les entrées/sorties pour audit (format CSV/JSON) si nécessaire.

Extensions possibles
-------------------
- Persistance des résultats dans un fichier CSV/JSON ou une base SQLite
- Export des séries de mesures pour analyse (p. ex. évolution temporelle)
- Ajout de métriques complémentaires (tour de taille, ratio taille/hanches)
- Module d'aide clinique avec références et recommandations personnalisées

Références
----------
- Organisation mondiale de la santé (OMS) — définition et seuils de l'IMC pour les adultes.

Licence et mentions
-------------------
Consulter le fichier `LICENSE` à la racine du dépôt pour les conditions d'utilisation.

Contact
-------
Voir le README principal du dépôt pour les informations de contact et les modalités de contribution.
