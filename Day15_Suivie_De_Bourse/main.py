import requests
import matplotlib.pyplot as plt


API_KEY = "55520942fb3e6554b07f7b9f70355ca4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def recupere_donnees_meteo(ville):
    params = {
        "q": ville,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des données météo : {response.status_code}")
        return None
def affiche_donnees_meteo(donnees):
        print(f"Ville : {donnees['name']}")
        print(f"Température : {donnees['main']['temp']} °C")
        print(f"Humidité : {donnees['main']['humidity']} %")
        print(f"Description : {donnees['weather'][0]['description']}")
        print(f"Vitesse du vent : {donnees['wind']['speed']} m/s")
        
        
def trace_graphique_temperature(ville):
    donnees = recupere_donnees_meteo(ville)
    if donnees:
        temperature = donnees['main']['temp']
        plt.figure(figsize=(6, 4))
        plt.bar([ville], [temperature], color='blue')
        plt.xlabel('Ville')
        plt.ylabel('Température (°C)')
        plt.title(f'Température actuelle à {ville}')
        plt.grid(True)
        plt.show()
        
def comparer_temperatures(villes):
    plt.figure(figsize=(10, 6))
    for ville in villes:
        donnees = recupere_donnees_meteo(ville)
        if donnees:
            temperature = donnees['main']['temp']
            plt.plot([ville], [temperature], marker='o', label=f'Température à {ville}')
    plt.xlabel('Ville')
    plt.ylabel('Température (°C)')
    plt.title('Comparaison des températures')
    plt.grid(True)
    plt.legend()
    plt.show()
    

def main():
    print("Bienvenue dans le programme de suivi de la météo !")
    while True:
        print("\nMenu :")
        print("1. Récupérer les données météo pour une ville")
        print("2. Afficher un graphique de la température pour une ville")
        print("3. Comparer les températures de plusieurs villes")
        print("4. Quitter")
        
        choix = input("Entrez le numéro correspondant à votre choix : ")
        
        if choix == "1":
            ville = input("Entrez le nom de la ville : ")
            donnees = recupere_donnees_meteo(ville)
            if donnees:
                affiche_donnees_meteo(donnees)
        elif choix == "2":
            ville = input("Entrez le nom de la ville : ")
            trace_graphique_temperature(ville)
        elif choix == "3":
            villes = input("Entrez les noms des villes séparés par des virgules : ").split(",")
            villes = [ville.strip() for ville in villes]
            comparer_temperatures(villes)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
            
if __name__ == "__main__":
    main()