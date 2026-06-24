from datetime import datetime

class Comptes:
    def __init__(self, numero, name, solde_initial=0, historique=None):
        self.numero = numero
        self.name = name
        self.solde = solde_initial
        self.historique = [] if historique is None else list(historique)
    def depot(self, montant2depot):
        if montant2depot <= 0:
            print("Soyez un peu sérieux et veuillez rentrez un montant réel")
        else:
            self.solde += montant2depot
            print(f"Dépôt de {montant2depot} effectué. Nouveau solde: {self.solde}")
            self.historique.append(f"{datetime.now().strftime('%d/%m/%Y à %H:%M')} : Dépôt: {montant2depot}")
    def retrait(self, montant2retrait):
        if montant2retrait <= 0:
            print("Montant invalide")
        elif montant2retrait <= self.solde:
            self.solde -= montant2retrait
            print(f"Retrait de {montant2retrait} effectué. Nouveau solde: {self.solde}")
            self.historique.append(f"{datetime.now().strftime('%d/%m/%Y à %H:%M')} : Retrait :{montant2retrait}")
        else:
            print("Solde insuffisant")
    def detaille(self):
        print(f"Numéro du compte : {self.numero}")
        print(f"Titulaire du compte: {self.name}")
        print(f"Solde du compte: {self.solde}")
        print("Merci pour votre fidélité.")
    def afficher_historique(self):
        print("\n--- HISTORIQUE DES TRANSACTIONS ---")
        if not self.historique:
            print("Votre historique de transactions est vide.")
        else:
            for entree in self.historique:
                print(entree)
numero_id_actuel=1000
bd={}        
def create_compte():
    global numero_id_actuel
    
    name = input("Entrez le nom du client :").strip()
    try:
        solde = float(input("Entrez le solde de départ :"))
    except ValueError:
        print("Solde invalide, initialisé à 0.")
        solde = 0.0
    compte = Comptes(numero_id_actuel, name, solde)
    bd[numero_id_actuel] = compte
    print(f"Bienvenue {name}, votre compte a été créé avec succès. Votre numéro de compte est {numero_id_actuel}.")
    print(f"Votre solde initial est de {solde}.")
    numero_id_actuel+=1

while True:
    print("---- BIENVENUE DANS NOTRE BANQUE ----- ")
    print("--- Quel service désirez vous ? ---")
    print("1. Créer un compte")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Consulter le solde")
    print("5. Historique")
    print("6. Quitter")
    
    choix = input("Entrez votre choix (1-6) : ")
    
    if choix == "1":
        create_compte()
    elif choix == "2":
        num_compt =int(input("Entrez votre numéro de compte : "))
        try:
            if num_compt in bd:
                    montant2depot = float(input("Entrez le montant à déposer : "))
                    bd[num_compt].depot(montant2depot)
            else:
                print("Compte non trouvé.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre")
    elif choix == "3":
        num_compt = int(input("Entrez votre numéro de compte : "))
        try:
            if num_compt in bd:
                montant2retrait = float(input("Entrez le montant à retirer : "))
                bd[num_compt].retrait(montant2retrait)

            else:
                print("Compte non trouvé.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre")
    elif choix == "4":
        num_compt = int(input("Entrez votre numéro de compte : "))
        if num_compt in bd:
            bd[num_compt].detaille()
        else:
            print("Compte non trouvé.")
    elif choix == "5":
        num_compt = int(input("Entrez votre numéro de compte : "))
        if num_compt in bd:
            bd[num_compt].afficher_historique()
        else:
            print("Compte non trouvé.")
    elif choix == "6":
        print("Merci d'avoir utilisé notre service bancaire. Au revoir !")
        break
    
    else:
        print("Choix invalide, veuillez réessayer.")
