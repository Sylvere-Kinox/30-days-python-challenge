import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_graph():
    def resolve_csv_path(chemin_fichier):
        chemin_fichier = chemin_fichier.strip()
        if os.path.isabs(chemin_fichier) and os.path.exists(chemin_fichier):
            return chemin_fichier

        repertoire_script = os.path.dirname(os.path.abspath(__file__))
        chemin_script = os.path.join(repertoire_script, chemin_fichier)
        if os.path.exists(chemin_script):
            return chemin_script

        return chemin_fichier

    print("Bienvenue dans le Générateur de graphique")
    print("Veuillez entrer le type de graphique que vous souhaitez générer (ex: 'line', 'bar', 'scatter'):")
    print("1-Graphe en ligne (line)")
    print("2-Graphe en barres (bar)")
    print("3-Graphe en nuage de points (scatter)")
    print("4-Histogramme (hist)")
    print("5-Diagramme circulaire (pie)")
    
    choix=int(input("Entrez le numéro correspondant à votre choix: "))
    if choix not in [1, 2, 3, 4, 5]:
        print("Choix invalide. Veuillez entrer un numéro valide.")
        return
    print("Choix de la méthode d'entrée des données:")
    print("1-Entrer les données manuellement")
    print("2-Importer les données depuis un fichier")
    
    methode=int(input("Entrez le numéro correspondant à votre choix: "))
    if methode == 1:
        x = list(map(float, input("Entrez les valeurs de l'axe X séparées par des espaces: ").split()))
        y = list(map(float, input("Entrez les valeurs de l'axe Y séparées par des espaces: ").split()))
    elif methode == 2:
        chemin_fichier = input("Entrez le chemin du fichier CSV: ")
        chemin_fichier = resolve_csv_path(chemin_fichier)
        try:
            df = pd.read_csv(chemin_fichier)
            print("Données chargées avec succès.")
            x = df.iloc[:, 0].tolist()
            y = df.iloc[:, 1].tolist()
        except Exception as e:
            print(f"Erreur lors du chargement des données: {e}")
            return
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")
        return
    
    if len(x) != len(y):
        print("Erreur : les listes X et Y doivent avoir la même taille.")
        return
    
    titre = input("Titre du graphique : ")
    
    if choix == 1:
        plt.plot(x, y, label="line", marker= "o")
    elif choix == 2:
        plt.bar(x, y, color="skyblue")
    elif choix == 3:
        plt.scatter(x, y, color="green", label="scatter")
    elif choix == 4:
        plt.hist(y, bins=10, color="orange", edgecolor="black")
    elif choix == 5:
        plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)

    plt.title(titre)
    if choix in [1, 3]:
        plt.xlabel("X-axes")
        plt.ylabel("Y-axes")
        plt.legend()
    plt.grid(True)
    
    enregistre_choix = input("Voulez-vous enrégristrer le graph ? (Oui/Non): ").lower()
    if enregistre_choix =="oui":
        chemin_fichier = input("Entrer le nom du fichier (avec .png): ")
        plt.savefig(chemin_fichier)
        
    else :
        plt.show()
        
if __name__ == "__main__":
    plot_graph()