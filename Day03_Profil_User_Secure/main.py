# App de profilage d'utilisateur sécurisé 
class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password  
        self.set_password(password)  # Appel de la méthode pour définir le mot de passe
        
    def get_email(self):
        return self._email
    def set_email(self, nouveau_email):
        if "@" in nouveau_email and "." in nouveau_email:  
         self._email = nouveau_email
         print("Email mis à jour avec succès.")
        else:
            print("Adresse email invalide. Veuillez fournir une adresse email valide.")
            
    def set_password(self, nouveau_mot_de_passe):
        if len(nouveau_mot_de_passe) >= 8:  
            self.__password = nouveau_mot_de_passe
            print("Mot de passe mis à jour avec succès.")
        else:
            print("Le mot de passe doit contenir au moins 8 caractères.")
    def afficher_profil(self):
        print("=== Profil de l'utilisateur ===")
        print(f"Nom d'utilisateur: {self.username}")
        print(f"Email: {self._email}")
        print("Mot de passe: ********")  # Masquer le mot de passe pour la sécurité
        
        
        
    #Programme principal
utilisateurs = []
    
def creer_utilisateur():
    utilisateur = input("Entrez le nom d'utilisateur: ")
    email = input("Entrez l'adresse email: ")
    password = input("Entrez le mot de passe (au moins 8 caractères): ")
        
    utilisateur = UserProfile(utilisateur, email, password)
    utilisateurs.append(utilisateur)
    print("Utilisateur ajouté avec succès.")
        
def afficher_utilisateurs():
    if not utilisateurs:
        print("Aucun utilisateur enregistré.")
    else:
        for utilisateur in utilisateurs:
            utilisateur.afficher_profil()
                
def mise_a_jour_email():
    for utilisateur in utilisateurs:
        nom_utilisateur = input("Entrez le nom d'utilisateur pour mettre à jour l'email : ")
        if utilisateur.username == nom_utilisateur:
            nouveau_email = input("Entrez le nouvel email : ")
            utilisateur.set_email(nouveau_email)
            return

    print("Utilisateur non trouvé.")

    
    #menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Créer un utilisateur")
    print("2. Afficher tout les utilisateurs")
    print("3. Mettre à jour l'email d'un utilisateur")
    print("4. Quitter")
        
    choix = input("Choisissez une option (1-4): ")
        
    if choix == "1":
        creer_utilisateur()
    elif choix == "2":
        afficher_utilisateurs()
    elif choix == "3":
        mise_a_jour_email()
    elif choix == "4":
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
    
        
        