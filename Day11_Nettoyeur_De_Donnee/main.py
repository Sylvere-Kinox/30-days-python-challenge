import pandas as pd
import os

def chargement_donne(chemin_fichier):
    """Cette fonction charge les données à partir d'un fichier CSV et retourne un DataFrame pandas."""
    
    try:
        df = pd.read_csv(chemin_fichier)
        print("Données chargées avec succès.")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        return None
    
    
def nettoyage_donnees(df):
    """Cette fonction nettoie les données en supprimant les valeurs manquantes et les doublons."""
    print("=== Nettoyage des Données ===")
    print("Taille initiale du DataFrame:", df.shape)
    
    # Supprimer les valeurs manquantes
    print("Suppression des valeurs manquantes...")
    df = df.dropna()
    print("Taille du DataFrame après suppression des valeurs manquantes:", df.shape)

    # Supprimer les doublons
    print("Suppression des doublons...")
    df = df.drop_duplicates()
    print("Taille du DataFrame après suppression des doublons:", df.shape)

    return df

    #Remplissage des valeurs manquantes avec la moyenne de la colonne
def remplissage_valeurs_manquantes(df):
    """Cette fonction remplit les valeurs manquantes avec la moyenne de la colonne."""
    print("=== Remplissage des Valeurs Manquantes ===")
    print("Taille initiale du DataFrame:", df.shape)
    
    # Remplir les valeurs manquantes avec la moyenne de la colonne (seulement pour les colonnes numériques)
    df = df.fillna(df.select_dtypes(include=['number']).mean())
    print("Taille du DataFrame après remplissage des valeurs manquantes:", df.shape)
    return df

def sauvegarde_donnees(df, chemin_fichier):
    """Sauvegarde des données nettoyer dans un nouveau fichier CSV."""
    try:
        df.to_csv(chemin_fichier, index=False)
        print(f"Données sauvegardées avec succès dans '{chemin_fichier}'.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données: {e}")

#Renommage des colonnes pour une meilleure lisibilité
def renommage_colonnes(df, nouveaux_noms):
    """Renomme les colonnes du DataFrame avec les nouveaux noms fournis."""
    print("=== Renommage des Colonnes ===")
    print("Noms de colonnes avant renommage:", df.columns.tolist())
    
    if len(nouveaux_noms) != len(df.columns):
        print("Erreur: Le nombre de nouveaux noms ne correspond pas au nombre de colonnes.")
        return df
    
    df.columns = nouveaux_noms
    print("Noms de colonnes après renommage:", df.columns.tolist())
    return df
        
#Programme principal        
def main():
    print("=== Nettoyeur de Données ===")
    print("Bienvenue dans le programme de nettoyage de données. Vous pouvez charger un fichier CSV, nettoyer les données et sauvegarder le résultat.")
    
    # Obtenir le répertoire du script (pas le répertoire courant)
    repertoire_script = os.path.dirname(os.path.abspath(__file__))
    print(f"\nRépertoire du programme: {repertoire_script}")
    
    # Changer le répertoire courant vers celui du script
    os.chdir(repertoire_script)
    
    # Lister les fichiers CSV disponibles
    fichiers_csv = [f for f in os.listdir(repertoire_script) if f.endswith('.csv')]
    if fichiers_csv:
        print("Fichiers CSV disponibles dans ce dossier:")
        for fichier in fichiers_csv:
            print(f"  - {fichier}")
    else:
        print("Aucun fichier CSV trouvé dans ce dossier.")
    
    print()
    chemin_fichier = input("Entrez le chemin du fichier CSV à charger: ")
    df = chargement_donne(chemin_fichier)
    if df is None:
        return
    #Montrer les premières lignes du DataFrame
    print("Aperçu des données chargées:")
    print(df.head())
    
    # Nettoyage des données
    df = nettoyage_donnees(df)
    # Remplissage des valeurs manquantes
    df = remplissage_valeurs_manquantes(df)
    # Renommage des colonnes
    nouveaux_noms = input("Entrez les nouveaux noms de colonnes séparés par des virgules (ou appuyez sur Entrée pour ne pas renommer): ").split(",")
    if nouveaux_noms != ['']:
        df = renommage_colonnes(df, [nom.strip() for nom in nouveaux_noms])
    # Sauvegarde des données nettoyées
    chemin_sauvegarde = input("Entrez le chemin du fichier CSV pour sauvegarder les données nettoyées: ")
    sauvegarde_donnees(df, chemin_sauvegarde)
            
if __name__ == "__main__":
    main()
    
    
    
    
