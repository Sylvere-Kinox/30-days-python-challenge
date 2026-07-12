import pandas as pd
import matplotlib.pyplot as plt

def chargeur_donnee(chemin_fichier):
    """Chargement des fichiers de température à partir d'un fichier CSV."""
    try:
        data = pd.read_csv(chemin_fichier, parse_dates=['Date'])
        if 'Temperature' not in data.columns:
            raise ValueError("La colonne 'Temperature' est introuvable dans le fichier CSV.")
        data['Temperature'] = pd.to_numeric(data['Temperature'], errors='raise')
        print("Données chargées avec succès !")
        return data
    except Exception as e:
        print("Erreur de chargement de données:", e)
        return None
    
def traceur_temp(data, save_file=None):
    """Tracer les tendances de températeurs avec des options pour la moyenne mobile et les anomalies"""
    #ajouter la moyenne mobile
    
    data["Moyenne sur 7 Jours"] = data['Temperature'].rolling(window=7).mean()
    mean_temp = data['Temperature'].mean()
    std_temp  = data['Temperature'].std()
    data["Anomalie"] = (data["Temperature"] > mean_temp + 2 * std_temp)|(data["Temperature"] < mean_temp - 2 * std_temp)
    
    #Tracage
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Temperature"], label="Température quotidienne", color="blue")
    plt.plot(data["Moyenne sur 7 Jours"], label="Moyenne sur 7 Jours", linestyle="--", color="orange")
    plt.scatter(data[data["Anomalie"]]["Date"], data[data["Anomalie"]]["Temperature"], color="red", label="Anomalies")
    plt.title("Tendances de température")
    plt.xlabel("Date")
    plt.ylabel("Température")
    plt.legend()
    plt.grid(True)
    #Sauvegarde de graphique
    if save_file:
        plt.savefig(save_file)
        print(f"Graphique enregistré comme {save_file}")
    else:
        plt.show()
        
def main():
    print("Bienvenue dans notre traceur de température")
    #Chargement
    chemin_fichier =input("Entrez le chemin du fichier CSV contenant les données de température :  ")
    data = chargeur_donnee(chemin_fichier)
    if data is None:
        return
    save_choice = input("Voulez-vous enregistrer le graphique (Oui/Non): ").strip().lower()
    if save_choice in {"oui", "o", "yes", "y"}:
        nom_fichier = input("Entrer le nom du fichier (avec .png): ").strip()
        traceur_temp(data, save_file=nom_fichier)
    else:
        traceur_temp(data)
if __name__ =="__main__":
    main()