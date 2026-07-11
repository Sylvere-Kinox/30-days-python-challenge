import pandas as pd
import matplotlib.pyplot as plt

def chargement_donnees(chemin_fichier):
    """Charger les données de ventes à partir d'un fichier CSV."""
    try:
        df = pd.read_csv(chemin_fichier)
        print("Données chargées avec succès.")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        return None

def nettoyage_donnees(df):
    """Nettoyer les données en supprimant les valeurs manquantes et en convertissant les types de données."""
    print("Nettoyage des données...")
    #Replace missing values with 0
    df['Product_Category'] = df['Product_Category'].fillna("Néant")
    df=df.dropna()
    # Convertir les colonnes de date en datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Sales_Amount'] = pd.to_numeric(df['Sales_Amount'], errors='coerce')
    
    #ajouter de nouvelles colonnes
    df['Year_Month'] = df['Date'].dt.to_period('M')
    if 'Quantity' in df.columns and 'Price' in df.columns:
        df['Revenue'] = df['Quantity'] * df['Price']
        
    print("Nettoyage terminé.")
    return df

def analyse_donnees(df):
    """Analyser les données et générer des statistiques."""
    print("Analyse des données...")
    # Statistiques de base
    stats = df.describe(include='all')
    print("Statistiques de base :")
    print(stats)
    
    # Ventes totales par catégorie de produit
    ventes_par_categorie = df.groupby('Product_Category')['Sales_Amount'].sum()
    print("\nVentes totales par catégorie de produit :")
    print(ventes_par_categorie)
    
    # Ventes mensuelles
    ventes_mensuelles = df.groupby('Year_Month')['Sales_Amount'].sum()
    print("\nVentes mensuelles :")
    print(ventes_mensuelles)
    
    return stats, ventes_par_categorie, ventes_mensuelles
    #Top 5 produits les plus vendus
def top_produits(df):
    """Identifier les 5 produits les plus vendus."""
    top_produits = df.groupby('Product_Name')['Quantity'].sum().nlargest(5)
    print("\nTop 5 des produits les plus vendus :")
    print(top_produits)
    return top_produits
#Visualisation des données
def visualisation_donnees(df):
    """Visualiser les données à l'aide de graphiques."""
    print("Visualisation des données...")
    # Ventes mensuelles
    ventes_mensuelles = df.groupby('Year_Month')['Sales_Amount'].sum()
    ventes_mensuelles.plot(kind='line', title='Ventes Mensuelles', xlabel='Mois', ylabel='Montant des Ventes')
    plt.show()
    
    # Ventes par catégorie de produit
    ventes_par_categorie = df.groupby('Product_Category')['Sales_Amount'].sum()
    ventes_par_categorie.plot(kind='bar', title='Ventes par Catégorie de Produit', xlabel='Catégorie de Produit', ylabel='Montant des Ventes')
    plt.show()
    
    # Visualisation circulaire des ventes par catégorie de produit
    ventes_par_categorie.plot(kind='pie', title='Répartition des Ventes par Catégorie de Produit', autopct='%1.1f%%', startangle=90)
    plt.ylabel('')  # Supprimer le label de l'axe Y pour le graphique
    plt.show()
    
def main():
    chemin_fichier = input("Entrez le chemin du fichier CSV contenant les données de ventes : ")
    df = chargement_donnees(chemin_fichier)
    if df is not None:
        df = nettoyage_donnees(df)
        stats, ventes_par_categorie, ventes_mensuelles = analyse_donnees(df)
        top_produits(df)
        visualisation_donnees(df)

if __name__ == "__main__":
    main()