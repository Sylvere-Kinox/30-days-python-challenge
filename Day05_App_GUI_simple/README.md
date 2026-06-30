# Application GUI Simple - Day05

## Description

Application de bureau simple réalisée avec Tkinter, la librairie graphique native de Python. Cette application permet aux utilisateurs de saisir leur nom et prénom pour recevoir un message de salutation personnalisé.

## Fonctionnalités

Interface utilisateur intuitive
- Fenêtre avec fond bleu clair
- Champs de saisie pour le nom et le prénom
- Affichage dynamique du message de salutation
- Boutons d'action et interaction utilisateur

Fonctionnalités principales
- Salutation personnalisée basée sur les informations saisies
- Gestion flexible acceptant le nom seul, le prénom seul, ou les deux
- Réinitialisation des champs et du message d'accueil
- Gestion des erreurs avec capture et affichage des exceptions

## Prérequis

- Python 3.6 ou supérieur
- Tkinter (inclus par défaut dans Python sur Windows et macOS)

### Installation de Tkinter

Sur Ubuntu/Debian:
```bash
sudo apt-get install python3-tk
```

Sur macOS:
```bash
brew install python-tk
```

Sur Windows: Tkinter est inclus automatiquement

## Utilisation

1. Naviguez vers le répertoire du projet:
```bash
cd Day05_App_GUI_simple
```

2. Exécutez l'application:
```bash
python main.py
```

3. L'application affichera une fenêtre avec:
   - Un champ pour entrer votre Nom
   - Un champ pour entrer votre Prénom
   - Un bouton "Saluer" pour générer le message
   - Un bouton "Réinitialiser" pour effacer les champs

## Comportement de l'application

| Cas | Résultat |
|-----|----------|
| Nom et Prénom remplis | "Bonjour, Nom Prénom !" |
| Seulement Nom | "Bonjour, Nom ! Veuillez entrer votre prénom." |
| Seulement Prénom | "Bonjour, Prénom ! Veuillez entrer votre nom." |
| Champs vides | "Bonjour ! Veuillez entrer votre nom et prénom." |

## Structure du code

```python
# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")

# Widgets d'interface
- title_label : Titre de l'application
- name_label + name_entry : Champ pour le nom
- surname_label + surname_entry : Champ pour le prénom
- greeting_label : Affichage du message
- greet_button : Bouton de salutation
- reset_button : Bouton de réinitialisation

# Fonctions
- greet_user() : Traite la salutation
- reset_fields() : Réinitialise les champs
```

## Concepts clés couverts

Concepts Python et Tkinter
- Création de fenêtres avec Tkinter
- Widgets (Label, Entry, Button)
- Gestionnaires de disposition (pack)
- Gestion d'événements (command)
- Manipulation de texte et validation
- Gestion des exceptions

## Améliorations possibles

Extensions potentielles de l'application:
- Sauvegarde de l'historique des salutations
- Support de plusieurs langues
- Personnalisation des couleurs et polices
- Base de données pour enregistrer les utilisateurs
- Validation plus avancée des entrées
- Export des données en fichier

## Captures d'écran

Les captures d'écran sont disponibles dans le dossier /screenshots/

## Licence

Voir le fichier LICENSE
