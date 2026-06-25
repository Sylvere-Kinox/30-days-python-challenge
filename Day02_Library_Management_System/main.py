class Books:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.est_emprunter = False
    
    def info(self):
        status = "Emprunté" if self.est_emprunter else "Disponible"
        print(f"Nom du livre : {self.titre} ")
        print(f"Auteur du livre : {self.auteur}")
        print(f"Status du livre : {status}") 

class Librairie:
    def __init__(self):
        self.librairie=[]
    
    def add_book(self, new_titre, new_auteur):
        for livre in self.librairie:
            if livre.titre.lower() == new_titre.lower():
                print("Ce livre existe déjà.")
                return

        new_book = Books(new_titre, new_auteur)
        self.librairie.append(new_book)
        print(f"Le livre {new_titre} a été ajouté avec succès.")
    
    def emprunt(self, nom_livre):
        for livre in self.librairie:
            if livre.titre == nom_livre and not livre.est_emprunter:
                livre.est_emprunter= True
                print(f"Vous venez d'emprunté le livre {nom_livre}")
                return
        print(f"Le livre {nom_livre} n'est pas disponible")
    
    def voir_livre(self):
        if not self.librairie :
            print("La librairie est vide, faites le premier pas et ajoutez-en un")
        else:
            print("--- CATALOGUE DE LA LIBRAIRIE ----")
            for livre in self.librairie:
                livre.info()
    def rechercher(self, nom):
        for livre in self.librairie:
            if livre.titre.lower() == nom.lower():
                livre.info()
                return
        print("Livre introuvable.")
    
               
    def retour_livre(self, nom_livre):
        for livre in self.librairie:
            if livre.titre == nom_livre and livre.est_emprunter:
                livre.est_emprunter= False
                print(f"Vous venez de retourner le livre {nom_livre}")
                return
        print(f"Le livre {nom_livre} n'est pas dans notre librairie")
        
        
librairie = Librairie()
while True:
    print("---- BIENVENUE DANS NOTRE LIBRAIRIE ----- ")
    print("--- Quel service désirez vous ? ---")
    print("1. Ajouter un livre")
    print("2. Emprunter un livre")
    print("3. Retourner un livre")
    print("4. Rechercher un livre")
    print("5. Voir les livres disponibles")
    print("6. Quitter")
    choix = input("Entrez votre choix (1-5) : ")
    
    if choix == "1":
        titre = input("Entrez le titre du livre : ")
        auteur = input("Entrez l'auteur du livre : ")
        librairie.add_book(titre, auteur)
    elif choix == "2":
        nom_livre = input("Entrez le nom du livre à emprunter : ")
        librairie.emprunt(nom_livre)
    elif choix == "3":
        nom_livre = input("Entrez le nom du livre à retourner : ")
        librairie.retour_livre(nom_livre)
    elif choix == "4":
        nom_livre = input("Entrez le nom du livre à rechercher : ")
        librairie.rechercher(nom_livre)
    elif choix == "5":
        librairie.voir_livre()
    elif choix == "6":
        print("Merci d'avoir utilisé notre librairie.")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
    
    
    
    
    
    
